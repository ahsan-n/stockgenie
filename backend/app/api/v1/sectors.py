"""
Sector API Endpoints
Provides KSE100 sector composition and analysis
"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
import logging

# Import mock data
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from mocks.sectors import get_mock_sectors, get_mock_sector_companies

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/sectors", tags=["Sectors"])


class SectorResponse(BaseModel):
    """Sector data model"""
    id: int
    name: str
    market_cap: int = Field(..., description="Market capitalization in PKR")
    weight_percent: float = Field(..., description="Weight in KSE100 index (%)")
    companies_count: int = Field(..., description="Number of companies in sector")
    day_change_percent: float = Field(..., description="Daily change percentage")
    avg_pe_ratio: float = Field(..., description="Average P/E ratio for sector")
    color: str = Field(..., description="Display color for charts")


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


@router.get("/", response_model=List[SectorResponse], summary="Get KSE100 Sector Composition")
async def get_sectors():
    """
    Get KSE100 sector composition and weights.
    
    Returns breakdown of KSE100 by sector including:
    - Market capitalization per sector
    - Weight percentage in index
    - Number of companies
    - Daily performance
    - Average P/E ratio
    
    **Example:**
    ```bash
    curl http://localhost:8000/api/v1/sectors | jq
    ```
    """
    try:
        sectors = get_mock_sectors()
        return [SectorResponse(**s) for s in sectors]
    except Exception as e:
        logger.error(f"Error fetching sectors: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch sector data: {str(e)}"
        )


@router.get("/{sector_name}/companies", response_model=List[CompanyResponse], 
            summary="Get Companies in Sector")
async def get_sector_companies(sector_name: str):
    """
    Get all companies within a specific sector.
    
    **Example:**
    ```bash
    curl http://localhost:8000/api/v1/sectors/Cement/companies | jq
    ```
    """
    try:
        companies = get_mock_sector_companies(sector_name)
        if not companies:
            raise HTTPException(
                status_code=404,
                detail=f"No companies found for sector: {sector_name}"
            )
        return [CompanyResponse(**c) for c in companies]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching sector companies: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch sector companies: {str(e)}"
        )

