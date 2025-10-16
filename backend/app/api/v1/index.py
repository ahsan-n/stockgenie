"""
KSE100 Index API Endpoints
"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import os

# Import mock data
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from mocks.stocks import get_mock_index

router = APIRouter(prefix="/index", tags=["Index"])


class IndexResponse(BaseModel):
    """KSE100 Index Response Model"""
    symbol: str = Field(..., description="Index symbol (KSE100)")
    name: str = Field(..., description="Index full name")
    value: float = Field(..., description="Current index value in points")
    change: float = Field(..., description="Absolute change from previous close")
    change_percent: float = Field(..., description="Percentage change from previous close")
    previous_close: float = Field(..., description="Previous trading day close")
    open: float = Field(..., description="Today's opening value")
    high: float = Field(..., description="Today's highest value")
    low: float = Field(..., description="Today's lowest value")
    volume: int = Field(..., description="Total trading volume")
    market_cap: int = Field(..., description="Total market capitalization in PKR")
    year_high: float = Field(..., description="52-week high")
    year_low: float = Field(..., description="52-week low")
    ytd_change_percent: float = Field(..., description="Year-to-date change percentage")
    constituent_count: int = Field(..., description="Number of stocks in the index")
    trading_status: str = Field(..., description="Current trading status (open/closed)")
    timestamp: str = Field(..., description="Last updated timestamp (ISO 8601)")
    average_volume_30d: Optional[int] = Field(None, description="30-day average volume")


@router.get("/", response_model=IndexResponse, summary="Get KSE100 Index Data")
async def get_index():
    """
    Get current KSE100 index data including:
    - Current value and daily change
    - Open, High, Low values
    - Trading volume and market cap
    - 52-week range and YTD performance
    - Trading status and constituent count
    
    **Example:**
    ```bash
    curl http://localhost:8000/api/v1/index | jq
    ```
    """
    try:
        # Get mock data (will be replaced with real data later)
        index_data = get_mock_index()
        return IndexResponse(**index_data)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch index data: {str(e)}"
        )


@router.get("/historical", summary="Get Historical Index Data")
async def get_historical_index(
    days: int = Query(30, ge=1, le=365, description="Number of days of historical data")
):
    """
    Get historical KSE100 index data
    
    **Note:** This endpoint will be implemented in a future update
    """
    raise HTTPException(
        status_code=501,
        detail="Historical data endpoint not yet implemented. Coming in Phase 2."
    )

