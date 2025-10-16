#!/usr/bin/env python3
"""
Test script for PSX scraper
Run this to test fetching real data from dps.psx.com.pk
"""
import sys
import logging
from app.services.psx_scraper import get_psx_scraper

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    print("=" * 60)
    print("PSX Scraper Test")
    print("=" * 60)
    
    scraper = get_psx_scraper()
    
    # Test connection
    print("\n1. Testing connection to PSX portal...")
    if scraper.test_connection():
        print("✅ Connection successful!")
    else:
        print("❌ Connection failed!")
        print("   The PSX portal might be down or blocking requests")
        return
    
    # Test fetching data
    print("\n2. Fetching KSE100 index data...")
    data = scraper.fetch_kse100_data()
    
    if data:
        print("✅ Data fetched successfully!")
        print("\n" + "=" * 60)
        print("KSE100 Index Data:")
        print("=" * 60)
        for key, value in data.items():
            print(f"  {key:20s}: {value}")
        print("=" * 60)
    else:
        print("❌ Failed to fetch data!")
        print("\n" + "=" * 60)
        print("Debugging Information:")
        print("=" * 60)
        print("This likely means:")
        print("1. The page structure has changed")
        print("2. The CSS selectors need to be updated")
        print("3. JavaScript rendering is required (need Selenium)")
        print("\nNext steps:")
        print("- Manually visit: https://dps.psx.com.pk/?page_id=30")
        print("- Inspect the page to find correct CSS selectors")
        print("- Update psx_scraper.py with correct selectors")

if __name__ == "__main__":
    main()

