"""
KSE100 Index API Endpoints
"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import os
import logging

# Import mock data (fallback)
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from mocks.stocks import get_mock_index

# Import real data services
from app.services.psx_scraper import get_psx_scraper
from app.services.cache_service import get_cache_service

logger = logging.getLogger(__name__)
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
    
    **Data Source:** PSX Data Portal (dps.psx.com.pk)  
    **Cache:** 5 minutes  
    **Fallback:** Mock data if PSX unavailable
    
    **Example:**
    ```bash
    curl http://localhost:8000/api/v1/index | jq
    ```
    """
    try:
        cache = get_cache_service()
        scraper = get_psx_scraper()
        
        # Try to get from cache first
        cache_key = "kse100:current"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            logger.info("✅ Returning cached KSE100 data")
            return IndexResponse(**cached_data)
        
        # Fetch from PSX
        logger.info("📊 Fetching fresh KSE100 data from PSX...")
        real_data = scraper.fetch_kse100_data()
        
        if real_data:
            # Ensure all required fields are present
            # Add missing fields with sensible defaults
            if 'open' not in real_data:
                real_data['open'] = real_data.get('previous_close', real_data['value'])
            if 'market_cap' not in real_data:
                real_data['market_cap'] = 8547000000000  # Approximate
            if 'constituent_count' not in real_data:
                real_data['constituent_count'] = 100
            if 'average_volume_30d' not in real_data:
                real_data['average_volume_30d'] = real_data.get('volume')
            
            # Cache for 5 minutes (300 seconds)
            cache.set(cache_key, real_data, ttl_seconds=300)
            logger.info(f"✅ Fetched real KSE100 data: {real_data['value']}")
            return IndexResponse(**real_data)
        
        # Fallback to mock data if PSX fetch fails
        logger.warning("⚠️ PSX data unavailable, using mock data")
        mock_data = get_mock_index()
        return IndexResponse(**mock_data)
        
    except Exception as e:
        logger.error(f"Error in get_index: {e}", exc_info=True)
        # Last resort: return mock data
        try:
            mock_data = get_mock_index()
            return IndexResponse(**mock_data)
        except:
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

