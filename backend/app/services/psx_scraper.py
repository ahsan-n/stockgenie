"""
PSX (Pakistan Stock Exchange) Data Scraper
Fetches real-time KSE100 index data from dps.psx.com.pk
"""
import requests
from bs4 import BeautifulSoup
from typing import Optional, Dict
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class PSXScraper:
    """Scraper for Pakistan Stock Exchange data portal"""
    
    BASE_URL = "https://dps.psx.com.pk"
    MARKET_WATCH_URL = f"{BASE_URL}/?page_id=30"  # Market Watch page
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        })
    
    def fetch_kse100_data(self) -> Optional[Dict]:
        """
        Fetch current KSE100 index data from PSX portal
        
        Returns:
            Dict with index data or None if fetch fails
        """
        try:
            logger.info("Fetching KSE100 data from PSX portal...")
            
            # Try to fetch the page
            response = self.session.get(self.MARKET_WATCH_URL, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Try to find KSE100 data
            # Note: This is a template - actual selectors need to be determined
            # by inspecting the actual page structure
            index_data = self._parse_kse100_from_html(soup)
            
            if index_data:
                logger.info(f"Successfully fetched KSE100: {index_data.get('value')}")
                return index_data
            else:
                logger.warning("Could not parse KSE100 data from page")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error fetching PSX data: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error fetching PSX data: {e}")
            return None
    
    def _parse_kse100_from_html(self, soup: BeautifulSoup) -> Optional[Dict]:
        """
        Parse KSE100 data from HTML soup
        
        Structure in dps.psx.com.pk:
        - Index name: class="topIndices__item__name"
        - Index value: class="topIndices__item__val"
        - Change: class="topIndices__item__change"
        - Change %: class="topIndices__item__changep"
        """
        try:
            # Find the KSE100 section in the top indices slider
            all_indices = soup.find_all('div', class_='topIndices__item')
            
            kse100_data = None
            for index_item in all_indices:
                name_elem = index_item.find('div', class_='topIndices__item__name')
                if name_elem and 'KSE100' in name_elem.text and name_elem.text.strip() == 'KSE100':
                    kse100_data = index_item
                    break
            
            if not kse100_data:
                logger.warning("Could not find KSE100 data in HTML")
                return None
            
            # Extract value
            value_elem = kse100_data.find('div', class_='topIndices__item__val')
            if not value_elem:
                logger.warning("Could not find KSE100 value element")
                return None
            
            value = self._parse_number(value_elem.text)
            
            # Extract change and change percent
            change_elem = kse100_data.find('div', class_='topIndices__item__change')
            change_pct_elem = kse100_data.find('div', class_='topIndices__item__changep')
            
            change = 0
            change_percent = 0
            if change_elem:
                change = self._parse_number(change_elem.text)
            if change_pct_elem:
                # Extract percentage (remove parentheses and % sign)
                pct_text = change_pct_elem.text.replace('(', '').replace(')', '').replace('%', '').strip()
                change_percent = self._parse_number(pct_text)
            
            # Calculate previous close
            previous_close = value - change
            
            # Try to get detailed data from the indices section
            detailed_data = self._parse_detailed_kse100(soup)
            
            base_data = {
                "symbol": "KSE100",
                "name": "Karachi Stock Exchange 100 Index",
                "value": value,
                "change": change,
                "change_percent": change_percent,
                "previous_close": round(previous_close, 2),
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "source": "PSX Data Portal",
                "trading_status": self._determine_trading_status(),
            }
            
            # Merge with detailed data if available
            if detailed_data:
                base_data.update(detailed_data)
            
            return base_data
            
        except Exception as e:
            logger.error(f"Error parsing HTML: {e}", exc_info=True)
            return None
    
    def _parse_detailed_kse100(self, soup: BeautifulSoup) -> Optional[Dict]:
        """Parse detailed KSE100 data from the indices section"""
        try:
            # Find the detailed panel for KSE100
            kse100_panel = soup.find('div', {'class': 'tabs__panel', 'data-name': 'KSE100'})
            if not kse100_panel:
                return None
            
            detailed = {}
            
            # Extract stats
            stats_items = kse100_panel.find_all('div', class_='stats_item')
            for item in stats_items:
                label_elem = item.find('div', class_='stats_label')
                value_elem = item.find('div', class_='stats_value')
                
                if label_elem and value_elem:
                    label = label_elem.text.strip().lower()
                    value_text = value_elem.text.strip()
                    
                    # Parse specific fields
                    if label == 'high':
                        detailed['high'] = self._parse_number(value_text)
                    elif label == 'low':
                        detailed['low'] = self._parse_number(value_text)
                    elif label == 'volume':
                        detailed['volume'] = int(self._parse_number(value_text))
                    elif label == 'previous close':
                        detailed['previous_close'] = self._parse_number(value_text)
                    elif label == '1-year change':
                        # Extract percentage
                        pct_text = value_text.replace('%', '').strip()
                        detailed['year_change_percent'] = self._parse_number(pct_text)
                    elif label == 'ytd change':
                        pct_text = value_text.replace('%', '').strip()
                        detailed['ytd_change_percent'] = self._parse_number(pct_text)
                    elif label == '52-week range':
                        # Parse range like "85,120.90 — 169,988.62"
                        parts = value_text.split('—')
                        if len(parts) == 2:
                            detailed['year_low'] = self._parse_number(parts[0])
                            detailed['year_high'] = self._parse_number(parts[1])
            
            return detailed if detailed else None
            
        except Exception as e:
            logger.debug(f"Could not parse detailed data: {e}")
            return None
    
    def _parse_number(self, text: str) -> float:
        """Parse number from text, removing commas and other characters"""
        try:
            # Remove commas, spaces, and other non-numeric characters
            clean_text = text.replace(',', '').replace(' ', '').strip()
            # Handle negative numbers
            clean_text = clean_text.replace('−', '-')  # Replace minus sign
            return float(clean_text)
        except (ValueError, AttributeError) as e:
            logger.error(f"Error parsing number from '{text}': {e}")
            return 0.0
    
    def _determine_trading_status(self) -> str:
        """Determine if market is open or closed based on current time"""
        now = datetime.utcnow()
        # PSX trading hours: 9:30 AM - 3:30 PM PKT (UTC+5)
        # Convert to UTC: 4:30 AM - 10:30 AM UTC
        hour_utc = now.hour
        
        # Simple check (can be improved with actual holiday calendar)
        is_weekday = now.weekday() < 5  # Monday=0, Friday=4
        is_trading_hours = 4 <= hour_utc < 11
        
        if is_weekday and is_trading_hours:
            return "open"
        else:
            return "closed"
    
    def test_connection(self) -> bool:
        """Test if PSX portal is accessible"""
        try:
            response = self.session.get(self.BASE_URL, timeout=5)
            return response.status_code == 200
        except:
            return False


# Singleton instance
_scraper_instance = None

def get_psx_scraper() -> PSXScraper:
    """Get singleton PSX scraper instance"""
    global _scraper_instance
    if _scraper_instance is None:
        _scraper_instance = PSXScraper()
    return _scraper_instance

