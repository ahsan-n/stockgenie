"""
Stock and StockPrice models
"""
from sqlalchemy import Column, Integer, String, Numeric, BigInteger, DateTime, Date, ForeignKey, func, Index
from sqlalchemy.orm import relationship
from app.models.base import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(10), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    sector_id = Column(Integer, ForeignKey("sectors.id"), nullable=True)
    listing_date = Column(Date, nullable=True)
    market_cap = Column(BigInteger, nullable=True)
    shares_outstanding = Column(BigInteger, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    sector = relationship("Sector", backref="stocks")

    def __repr__(self):
        return f"<Stock(id={self.id}, symbol='{self.symbol}', name='{self.name}')>"


class StockPrice(Base):
    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False, index=True)
    open = Column(Numeric(10, 2))
    high = Column(Numeric(10, 2))
    low = Column(Numeric(10, 2))
    close = Column(Numeric(10, 2))
    volume = Column(BigInteger)
    created_at = Column(DateTime, server_default=func.now())

    # Composite index for efficient queries
    __table_args__ = (
        Index('idx_stock_prices_stock_timestamp', 'stock_id', 'timestamp'),
    )

    # Relationships
    stock = relationship("Stock", backref="prices")

    def __repr__(self):
        return f"<StockPrice(id={self.id}, stock_id={self.stock_id}, timestamp={self.timestamp}, close={self.close})>"

