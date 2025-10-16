"""
Company API Endpoints  
Provides top companies and detailed company data
"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import logging

# Import mock data
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from mocks.sectors import get_mock_top_companies

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/companies", tags=["Companies"])


class SortField(str, Enum):
    """Sortable fields for companies"""
    rank = "rank"
    symbol = "symbol"
    market_cap = "market_cap"
    price = "price"
    change_percent = "change_percent"
    pe_ratio = "pe_ratio"
    dividend_yield = "dividend_yield"
    volume = "volume"


class SortOrder(str, Enum):
    """Sort order"""
    asc = "asc"
    desc = "desc"


class CompanyResponse(BaseModel):
    """Company data model"""
    rank: int
    symbol: str
    name: str
    sector: str
    price: float
    change: float
    change_percent: float
    market_cap: int
    pe_ratio: float
    dividend_yield: float
    eps: float
    volume: int
    year_high: float
    year_low: float


@router.get("/top", response_model=List[CompanyResponse], summary="Get Top Companies")
async def get_top_companies(
    limit: int = Query(30, ge=1, le=100, description="Number of companies to return"),
    sort_by: SortField = Query(SortField.rank, description="Field to sort by"),
    sort_order: SortOrder = Query(SortOrder.asc, description="Sort order (asc/desc)"),
    sector: Optional[str] = Query(None, description="Filter by sector")
):
    """
    Get top KSE100 companies by market capitalization.
    
    **Features:**
    - Sort by any field (market cap, price, P/E, dividend yield)
    - Filter by sector
    - Configurable limit
    
    **Example:**
    ```bash
    # Top 30 companies
    curl http://localhost:8000/api/v1/companies/top | jq
    
    # Top 10 by market cap (descending)
    curl "http://localhost:8000/api/v1/companies/top?limit=10&sort_by=market_cap&sort_order=desc" | jq
    
    # Banks only
    curl "http://localhost:8000/api/v1/companies/top?sector=Commercial%20Banks" | jq
    ```
    """
    try:
        companies = get_mock_top_companies(limit=limit)
        
        # Filter by sector if provided
        if sector:
            companies = [c for c in companies if c["sector"] == sector]
        
        # Sort
        reverse = (sort_order == SortOrder.desc)
        companies = sorted(companies, key=lambda x: x[sort_by.value], reverse=reverse)
        
        return [CompanyResponse(**c) for c in companies]
        
    except Exception as e:
        logger.error(f"Error fetching top companies: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch companies: {str(e)}"
        )

