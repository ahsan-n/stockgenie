#!/usr/bin/env python3
"""
Seed initial data for StockGenie database
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

from app.models import Sector, Stock

# Database connection
DATABASE_URL = "postgresql://stockgenie:changeme_secure_password@localhost/stockgenie_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def seed_sectors():
    """Seed sector data"""
    session = SessionLocal()
    
    sectors_data = [
        {"name": "Cement", "description": "Cement manufacturing companies"},
        {"name": "Commercial Banks", "description": "Banking and financial services"},
        {"name": "Oil & Gas Exploration", "description": "Oil and gas exploration and production"},
        {"name": "Fertilizer", "description": "Fertilizer manufacturing"},
        {"name": "Power Generation", "description": "Power generation and distribution"},
    ]
    
    sectors = []
    for sector_data in sectors_data:
        # Check if exists
        existing = session.query(Sector).filter(Sector.name == sector_data["name"]).first()
        if not existing:
            sector = Sector(**sector_data)
            session.add(sector)
            sectors.append(sector)
            print(f"✅ Added sector: {sector_data['name']}")
        else:
            sectors.append(existing)
            print(f"⏭️  Sector already exists: {sector_data['name']}")
    
    session.commit()
    return {s.name: s.id for s in sectors}


def seed_stocks(sector_ids):
    """Seed stock data"""
    session = SessionLocal()
    
    stocks_data = [
        {
            "symbol": "FCCL",
            "name": "Fauji Cement Company Limited",
            "sector_id": sector_ids["Cement"],
            "listing_date": date(1992, 1, 15),
            "market_cap": 50_000_000_000,
            "shares_outstanding": 1_960_784_314,
        },
        {
            "symbol": "POWER",
            "name": "Power Cement Limited",
            "sector_id": sector_ids["Cement"],
            "listing_date": date(2005, 6, 20),
            "market_cap": 22_000_000_000,
            "shares_outstanding": 2_514_285_714,
        },
        {
            "symbol": "PIOC",
            "name": "Pioneer Cement Limited",
            "sector_id": sector_ids["Cement"],
            "listing_date": date(2004, 12, 1),
            "market_cap": 19_000_000_000,
            "shares_outstanding": 452_380_952,
        },
        {
            "symbol": "HBL",
            "name": "Habib Bank Limited",
            "sector_id": sector_ids["Commercial Banks"],
            "listing_date": date(1991, 10, 1),
            "market_cap": 145_000_000_000,
            "shares_outstanding": 1_375_000_000,
        },
        {
            "symbol": "OGDC",
            "name": "Oil & Gas Development Company Limited",
            "sector_id": sector_ids["Oil & Gas Exploration"],
            "listing_date": date(1997, 1, 1),
            "market_cap": 708_000_000_000,
            "shares_outstanding": 4_290_765_244,
        },
    ]
    
    for stock_data in stocks_data:
        # Check if exists
        existing = session.query(Stock).filter(Stock.symbol == stock_data["symbol"]).first()
        if not existing:
            stock = Stock(**stock_data)
            session.add(stock)
            print(f"✅ Added stock: {stock_data['symbol']} - {stock_data['name']}")
        else:
            print(f"⏭️  Stock already exists: {stock_data['symbol']}")
    
    session.commit()
    session.close()


if __name__ == "__main__":
    print("🌱 Seeding database...")
    print()
    
    try:
        # Seed sectors first
        print("📊 Seeding sectors...")
        sector_ids = seed_sectors()
        print()
        
        # Seed stocks
        print("📈 Seeding stocks...")
        seed_stocks(sector_ids)
        print()
        
        print("✅ Database seeding complete!")
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        sys.exit(1)

