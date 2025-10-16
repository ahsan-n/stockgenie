"""
Mock Sector Data for KSE100
Based on actual PSX sector composition
"""
from typing import List, Dict


# Major KSE100 sectors with approximate weights
MOCK_SECTORS = [
    {
        "id": 1,
        "name": "Commercial Banks",
        "market_cap": 2854000000000,  # PKR
        "weight_percent": 33.4,
        "companies_count": 18,
        "day_change_percent": -0.65,
        "avg_pe_ratio": 4.2,
        "color": "#0088FE"
    },
    {
        "id": 2,
        "name": "Oil & Gas Exploration Companies",
        "market_cap": 1456000000000,
        "weight_percent": 17.0,
        "companies_count": 9,
        "day_change_percent": -0.42,
        "avg_pe_ratio": 3.8,
        "color": "#00C49F"
    },
    {
        "id": 3,
        "name": "Oil & Gas Marketing Companies",
        "market_cap": 985000000000,
        "weight_percent": 11.5,
        "companies_count": 6,
        "day_change_percent": -0.55,
        "avg_pe_ratio": 5.1,
        "color": "#FFBB28"
    },
    {
        "id": 4,
        "name": "Fertilizer",
        "market_cap": 742000000000,
        "weight_percent": 8.7,
        "companies_count": 5,
        "day_change_percent": -1.12,
        "avg_pe_ratio": 3.5,
        "color": "#FF8042"
    },
    {
        "id": 5,
        "name": "Cement",
        "market_cap": 612000000000,
        "weight_percent": 7.2,
        "companies_count": 8,
        "day_change_percent": -0.89,
        "avg_pe_ratio": 6.8,
        "color": "#8884D8"
    },
    {
        "id": 6,
        "name": "Power Generation & Distribution",
        "market_cap": 528000000000,
        "weight_percent": 6.2,
        "companies_count": 12,
        "day_change_percent": -0.45,
        "avg_pe_ratio": 4.9,
        "color": "#82CA9D"
    },
    {
        "id": 7,
        "name": "Technology & Communication",
        "market_cap": 445000000000,
        "weight_percent": 5.2,
        "companies_count": 7,
        "day_change_percent": -0.78,
        "avg_pe_ratio": 7.2,
        "color": "#FFC658"
    },
    {
        "id": 8,
        "name": "Food & Personal Care Products",
        "market_cap": 389000000000,
        "weight_percent": 4.6,
        "companies_count": 9,
        "day_change_percent": -0.32,
        "avg_pe_ratio": 12.5,
        "color": "#FF6B9D"
    },
    {
        "id": 9,
        "name": "Automobile & Parts",
        "market_cap": 321000000000,
        "weight_percent": 3.8,
        "companies_count": 5,
        "day_change_percent": -1.25,
        "avg_pe_ratio": 8.3,
        "color": "#C084FC"
    },
    {
        "id": 10,
        "name": "Others",
        "market_cap": 215000000000,
        "weight_percent": 2.4,
        "companies_count": 21,
        "day_change_percent": -0.51,
        "avg_pe_ratio": 9.1,
        "color": "#94A3B8"
    }
]


# Top 30 KSE100 companies by market cap
MOCK_TOP_COMPANIES = [
    {
        "rank": 1,
        "symbol": "HBL",
        "name": "Habib Bank Limited",
        "sector": "Commercial Banks",
        "price": 187.50,
        "change": -1.25,
        "change_percent": -0.66,
        "market_cap": 385000000000,
        "pe_ratio": 3.8,
        "dividend_yield": 6.2,
        "eps": 49.34,
        "volume": 5420000,
        "year_high": 225.00,
        "year_low": 165.00
    },
    {
        "rank": 2,
        "symbol": "OGDC",
        "name": "Oil & Gas Development Company Limited",
        "sector": "Oil & Gas Exploration Companies",
        "price": 245.30,
        "change": -2.10,
        "change_percent": -0.85,
        "market_cap": 1056000000000,
        "pe_ratio": 4.2,
        "dividend_yield": 8.5,
        "eps": 58.40,
        "volume": 8950000,
        "year_high": 295.00,
        "year_low": 215.00
    },
    {
        "rank": 3,
        "symbol": "UBL",
        "name": "United Bank Limited",
        "sector": "Commercial Banks",
        "price": 245.80,
        "change": -1.60,
        "change_percent": -0.65,
        "market_cap": 342000000000,
        "pe_ratio": 4.1,
        "dividend_yield": 5.8,
        "eps": 59.95,
        "volume": 3210000,
        "year_high": 282.00,
        "year_low": 218.00
    },
    {
        "rank": 4,
        "symbol": "MCB",
        "name": "MCB Bank Limited",
        "sector": "Commercial Banks",
        "price": 289.40,
        "change": -1.85,
        "change_percent": -0.63,
        "market_cap": 328000000000,
        "pe_ratio": 4.5,
        "dividend_yield": 6.5,
        "eps": 64.31,
        "volume": 2850000,
        "year_high": 325.00,
        "year_low": 255.00
    },
    {
        "rank": 5,
        "symbol": "PPL",
        "name": "Pakistan Petroleum Limited",
        "sector": "Oil & Gas Exploration Companies",
        "price": 195.70,
        "change": -0.95,
        "change_percent": -0.48,
        "market_cap": 400000000000,
        "pe_ratio": 3.5,
        "dividend_yield": 9.2,
        "eps": 55.91,
        "volume": 6430000,
        "year_high": 235.00,
        "year_low": 175.00
    },
    {
        "rank": 6,
        "symbol": "MEBL",
        "name": "Meezan Bank Limited",
        "sector": "Commercial Banks",
        "price": 156.30,
        "change": -1.10,
        "change_percent": -0.70,
        "market_cap": 295000000000,
        "pe_ratio": 5.2,
        "dividend_yield": 4.8,
        "eps": 30.06,
        "volume": 4120000,
        "year_high": 185.00,
        "year_low": 140.00
    },
    {
        "rank": 7,
        "symbol": "PSO",
        "name": "Pakistan State Oil Company Limited",
        "sector": "Oil & Gas Marketing Companies",
        "price": 325.50,
        "change": -2.40,
        "change_percent": -0.73,
        "market_cap": 485000000000,
        "pe_ratio": 4.8,
        "dividend_yield": 7.8,
        "eps": 67.81,
        "volume": 1950000,
        "year_high": 395.00,
        "year_low": 285.00
    },
    {
        "rank": 8,
        "symbol": "ENGRO",
        "name": "Engro Corporation Limited",
        "sector": "Fertilizer",
        "price": 385.20,
        "change": -3.50,
        "change_percent": -0.90,
        "market_cap": 350000000000,
        "pe_ratio": 5.5,
        "dividend_yield": 6.0,
        "eps": 70.04,
        "volume": 2340000,
        "year_high": 445.00,
        "year_low": 335.00
    },
    {
        "rank": 9,
        "symbol": "BAFL",
        "name": "Bank Alfalah Limited",
        "sector": "Commercial Banks",
        "price": 89.50,
        "change": -0.65,
        "change_percent": -0.72,
        "market_cap": 278000000000,
        "pe_ratio": 4.3,
        "dividend_yield": 5.5,
        "eps": 20.81,
        "volume": 5680000,
        "year_high": 105.00,
        "year_low": 78.00
    },
    {
        "rank": 10,
        "symbol": "FFC",
        "name": "Fauji Fertilizer Company Limited",
        "sector": "Fertilizer",
        "price": 145.80,
        "change": -1.30,
        "change_percent": -0.88,
        "market_cap": 392000000000,
        "pe_ratio": 3.8,
        "dividend_yield": 8.9,
        "eps": 38.37,
        "volume": 7320000,
        "year_high": 175.00,
        "year_low": 128.00
    },
    {
        "rank": 11,
        "symbol": "LUCK",
        "name": "Lucky Cement Limited",
        "sector": "Cement",
        "price": 895.50,
        "change": -8.30,
        "change_percent": -0.92,
        "market_cap": 285000000000,
        "pe_ratio": 7.2,
        "dividend_yield": 4.5,
        "eps": 124.38,
        "volume": 1120000,
        "year_high": 1050.00,
        "year_low": 785.00
    },
    {
        "rank": 12,
        "symbol": "FCCL",
        "name": "Fauji Cement Company Limited",
        "sector": "Cement",
        "price": 42.35,
        "change": -0.45,
        "change_percent": -1.05,
        "market_cap": 127000000000,
        "pe_ratio": 6.5,
        "dividend_yield": 5.2,
        "eps": 6.51,
        "volume": 8950000,
        "year_high": 52.00,
        "year_low": 35.00
    },
    # Add more companies as needed...
    {
        "rank": 13,
        "symbol": "HUBC",
        "name": "Hub Power Company Limited",
        "sector": "Power Generation & Distribution",
        "price": 125.70,
        "change": -0.85,
        "change_percent": -0.67,
        "market_cap": 245000000000,
        "pe_ratio": 5.1,
        "dividend_yield": 7.2,
        "eps": 24.65,
        "volume": 3450000,
        "year_high": 148.00,
        "year_low": 110.00
    },
    {
        "rank": 14,
        "symbol": "TRG",
        "name": "TRG Pakistan Limited",
        "sector": "Technology & Communication",
        "price": 185.40,
        "change": -1.70,
        "change_percent": -0.91,
        "market_cap": 235000000000,
        "pe_ratio": 8.5,
        "dividend_yield": 3.2,
        "eps": 21.81,
        "volume": 1890000,
        "year_high": 215.00,
        "year_low": 155.00
    },
    {
        "rank": 15,
        "symbol": "NRL",
        "name": "National Refinery Limited",
        "sector": "Oil & Gas Marketing Companies",
        "price": 425.50,
        "change": -2.80,
        "change_percent": -0.65,
        "market_cap": 215000000000,
        "pe_ratio": 6.2,
        "dividend_yield": 6.5,
        "eps": 68.63,
        "volume": 895000,
        "year_high": 485.00,
        "year_low": 375.00
    }
]


def get_mock_sectors() -> List[Dict]:
    """Get mock sector data"""
    return MOCK_SECTORS


def get_mock_top_companies(limit: int = 30) -> List[Dict]:
    """Get mock top companies data"""
    return MOCK_TOP_COMPANIES[:limit]


def get_mock_sector_companies(sector_name: str) -> List[Dict]:
    """Get companies for a specific sector"""
    return [c for c in MOCK_TOP_COMPANIES if c["sector"] == sector_name]

