"""
Mock stock data for development and testing
"""
from typing import List, Dict

# Mock KSE100 Index Data
MOCK_KSE100_INDEX = {
    "symbol": "KSE100",
    "value": 95234.50,
    "change": 287.30,
    "change_percent": 0.30,
    "market_cap": 8_547_000_000_000,  # PKR
    "timestamp": "2024-01-15T14:30:00Z",
    "volume": 245_000_000,
}

# Mock Sectors Data
MOCK_SECTORS = [
    {
        "name": "Cement",
        "market_cap": 523_000_000_000,
        "change_percent": 2.15,
        "stock_count": 18,
        "avg_pe_ratio": 4.82,
        "top_contributor": "FCCL",
    },
    {
        "name": "Commercial Banks",
        "market_cap": 1_245_000_000_000,
        "change_percent": -0.85,
        "stock_count": 21,
        "avg_pe_ratio": 6.45,
        "top_contributor": "HBL",
    },
    {
        "name": "Oil & Gas Exploration",
        "market_cap": 987_000_000_000,
        "change_percent": 1.45,
        "stock_count": 8,
        "avg_pe_ratio": 5.20,
        "top_contributor": "OGDC",
    },
    {
        "name": "Fertilizer",
        "market_cap": 654_000_000_000,
        "change_percent": 0.95,
        "stock_count": 6,
        "avg_pe_ratio": 7.15,
        "top_contributor": "FFC",
    },
    {
        "name": "Power Generation",
        "market_cap": 456_000_000_000,
        "change_percent": -1.25,
        "stock_count": 12,
        "avg_pe_ratio": 3.90,
        "top_contributor": "HUBC",
    },
    {
        "name": "Technology",
        "market_cap": 234_000_000_000,
        "change_percent": 3.45,
        "stock_count": 9,
        "avg_pe_ratio": 12.50,
        "top_contributor": "SYSTEMS",
    },
    {
        "name": "Automobile",
        "market_cap": 187_000_000_000,
        "change_percent": -0.55,
        "stock_count": 5,
        "avg_pe_ratio": 4.25,
        "top_contributor": "INDU",
    },
]

# Mock Top Stocks Data
MOCK_TOP_STOCKS = [
    {
        "symbol": "FCCL",
        "name": "Fauji Cement Company Limited",
        "sector": "Cement",
        "price": 25.50,
        "change": 0.30,
        "change_percent": 1.19,
        "pe_ratio": 4.50,
        "sector_pe_avg": 4.82,
        "dividend_yield": 8.24,
        "eps": 5.67,
        "market_cap": 50_000_000_000,
        "volume": 8_234_500,
    },
    {
        "symbol": "POWER",
        "name": "Power Cement Limited",
        "sector": "Cement",
        "price": 8.75,
        "change": 0.15,
        "change_percent": 1.74,
        "pe_ratio": 5.20,
        "sector_pe_avg": 4.82,
        "dividend_yield": 7.50,
        "eps": 1.68,
        "market_cap": 22_000_000_000,
        "volume": 12_500_000,
    },
    {
        "symbol": "PIOC",
        "name": "Pioneer Cement Limited",
        "sector": "Cement",
        "price": 42.00,
        "change": 0.85,
        "change_percent": 2.07,
        "pe_ratio": 4.85,
        "sector_pe_avg": 4.82,
        "dividend_yield": 6.90,
        "eps": 8.66,
        "market_cap": 19_000_000_000,
        "volume": 3_456_000,
    },
    {
        "symbol": "LUCK",
        "name": "Lucky Cement Limited",
        "sector": "Cement",
        "price": 870.00,
        "change": -5.50,
        "change_percent": -0.63,
        "pe_ratio": 4.20,
        "sector_pe_avg": 4.82,
        "dividend_yield": 9.10,
        "eps": 207.14,
        "market_cap": 125_000_000_000,
        "volume": 456_000,
    },
    {
        "symbol": "HBL",
        "name": "Habib Bank Limited",
        "sector": "Commercial Banks",
        "price": 105.50,
        "change": -0.75,
        "change_percent": -0.71,
        "pe_ratio": 6.25,
        "sector_pe_avg": 6.45,
        "dividend_yield": 8.50,
        "eps": 16.88,
        "market_cap": 145_000_000_000,
        "volume": 2_345_000,
    },
    {
        "symbol": "OGDC",
        "name": "Oil & Gas Development Company Limited",
        "sector": "Oil & Gas Exploration",
        "price": 165.00,
        "change": 2.30,
        "change_percent": 1.41,
        "pe_ratio": 5.50,
        "sector_pe_avg": 5.20,
        "dividend_yield": 12.50,
        "eps": 30.00,
        "market_cap": 708_000_000_000,
        "volume": 5_678_000,
    },
    {
        "symbol": "PPL",
        "name": "Pakistan Petroleum Limited",
        "sector": "Oil & Gas Exploration",
        "price": 92.50,
        "change": 1.15,
        "change_percent": 1.26,
        "pe_ratio": 4.90,
        "sector_pe_avg": 5.20,
        "dividend_yield": 10.80,
        "eps": 18.88,
        "market_cap": 156_000_000_000,
        "volume": 8_900_000,
    },
    {
        "symbol": "FFC",
        "name": "Fauji Fertilizer Company Limited",
        "sector": "Fertilizer",
        "price": 145.00,
        "change": 1.50,
        "change_percent": 1.04,
        "pe_ratio": 7.40,
        "sector_pe_avg": 7.15,
        "dividend_yield": 6.90,
        "eps": 19.59,
        "market_cap": 165_000_000_000,
        "volume": 3_456_000,
    },
    {
        "symbol": "ENGRO",
        "name": "Engro Corporation Limited",
        "sector": "Fertilizer",
        "price": 298.00,
        "change": 0.50,
        "change_percent": 0.17,
        "pe_ratio": 6.85,
        "sector_pe_avg": 7.15,
        "dividend_yield": 5.50,
        "eps": 43.50,
        "market_cap": 87_000_000_000,
        "volume": 1_234_000,
    },
    {
        "symbol": "HUBC",
        "name": "Hub Power Company Limited",
        "sector": "Power Generation",
        "price": 82.50,
        "change": -1.05,
        "change_percent": -1.26,
        "pe_ratio": 3.75,
        "sector_pe_avg": 3.90,
        "dividend_yield": 11.20,
        "eps": 22.00,
        "market_cap": 124_000_000_000,
        "volume": 6_789_000,
    },
]

# Mock Company Details
MOCK_COMPANY_DETAILS = {
    "FCCL": {
        "symbol": "FCCL",
        "name": "Fauji Cement Company Limited",
        "sector": "Cement",
        "description": "Fauji Cement Company Limited (FCCL) is one of Pakistan's leading cement manufacturers. "
                      "The company operates multiple production lines with a combined capacity exceeding 6 million "
                      "tonnes per annum. FCCL is part of the Fauji Foundation Group.",
        "website": "https://www.fccl.com.pk",
        "listing_date": "1992-01-15",
        "current_price": 25.50,
        "market_cap": 50_000_000_000,
        "shares_outstanding": 1_960_784_314,
        "pe_ratio": 4.50,
        "dividend_yield": 8.24,
        "eps": 5.67,
        "book_value": 15.30,
        "52_week_high": 28.50,
        "52_week_low": 18.75,
    },
    "POWER": {
        "symbol": "POWER",
        "name": "Power Cement Limited",
        "sector": "Cement",
        "description": "Power Cement Limited is a cement manufacturing company operating in Pakistan with modern "
                      "production facilities. The company focuses on producing high-quality cement for construction.",
        "website": "https://www.powercement.com",
        "listing_date": "2005-06-20",
        "current_price": 8.75,
        "market_cap": 22_000_000_000,
        "shares_outstanding": 2_514_285_714,
        "pe_ratio": 5.20,
        "dividend_yield": 7.50,
        "eps": 1.68,
        "book_value": 10.50,
        "52_week_high": 10.25,
        "52_week_low": 6.50,
    },
    "PIOC": {
        "symbol": "PIOC",
        "name": "Pioneer Cement Limited",
        "sector": "Cement",
        "description": "Pioneer Cement Limited is engaged in the manufacturing and sale of cement and clinker. "
                      "The company has established a strong presence in the domestic cement market.",
        "website": "https://www.pioneercement.com.pk",
        "listing_date": "2004-12-01",
        "current_price": 42.00,
        "market_cap": 19_000_000_000,
        "shares_outstanding": 452_380_952,
        "pe_ratio": 4.85,
        "dividend_yield": 6.90,
        "eps": 8.66,
        "book_value": 25.80,
        "52_week_high": 48.00,
        "52_week_low": 35.00,
    },
}


def get_mock_index() -> Dict:
    """Get mock KSE100 index data"""
    from datetime import datetime
    
    # Calculate derived values
    previous_close = MOCK_KSE100_INDEX["value"] - MOCK_KSE100_INDEX["change"]
    
    # Enhanced index data with all required fields
    enhanced_data = {
        **MOCK_KSE100_INDEX,
        "name": "Karachi Stock Exchange 100 Index",
        "previous_close": round(previous_close, 2),
        "open": 94950.20,
        "high": 95450.75,
        "low": 94875.30,
        "year_high": 97500.00,
        "year_low": 88250.00,
        "ytd_change_percent": 12.5,
        "constituent_count": 100,
        "trading_status": "closed",  # Market closed at time of data
        "average_volume_30d": 235_000_000,
    }
    
    return enhanced_data


def get_mock_sectors() -> List[Dict]:
    """Get mock sector summary data"""
    return MOCK_SECTORS


def get_mock_top_stocks(limit: int = 10) -> List[Dict]:
    """Get mock top stocks data"""
    return MOCK_TOP_STOCKS[:limit]


def get_mock_company_details(symbol: str) -> Dict:
    """Get mock company details"""
    return MOCK_COMPANY_DETAILS.get(symbol, {})

