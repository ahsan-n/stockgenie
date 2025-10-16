# Data Sources & APIs Needed for StockGenie

## Current Status
✅ **Mock Data**: Dashboard works with hardcoded data
🔴 **Real Data**: Not yet integrated

---

## 1. KSE100 Index Data (PRIORITY 1 - Issue #3)

### What We Need:
- **Current index value** (e.g., 95,234.50)
- **Daily change** (absolute and percentage)
- **Open, High, Low, Close** (OHLC)
- **Trading volume**
- **Market capitalization** (total)
- **52-week high/low**
- **YTD performance**
- **Last updated timestamp**
- **Trading status** (open/closed)

### Possible Data Sources:

#### Option A: Pakistan Stock Exchange (PSX) Official
- **Website**: https://www.psx.com.pk
- **Method**: Web scraping or official API (if available)
- **Frequency**: Real-time or 15-min delayed
- **Cost**: Need to verify
- **Status**: ❓ Need to check if PSX provides API access

#### Option B: Financial Data Providers
1. **Alpha Vantage** (https://www.alphavantage.co)
   - ❓ Need to check if they support KSE100
   - Free tier: 5 API calls/minute, 500 calls/day
   - Cost: Free tier available

2. **Financial Modeling Prep** (https://financialmodelingprep.com)
   - ❓ Need to verify KSE100 coverage
   - Free tier: 250 calls/day
   - Cost: $14.99/month for more

3. **Yahoo Finance** (via yfinance library)
   - Symbol: Might be available as `^KSE100` or similar
   - Free, no API key needed
   - Python library: `pip install yfinance`

4. **Investing.com**
   - Web scraping required
   - Real-time data
   - Cost: Free (but requires scraping)

#### Option C: Pakistani Financial APIs
- **Business Recorder** (https://www.brecorder.com)
- **Dawn News Business** (https://www.dawn.com/business)
- **Dunya News Business**
- **Status**: Need to check API availability

### Recommended Approach:
1. **Start with**: PSX official website scraping (most reliable)
2. **Backup**: Yahoo Finance if KSE100 is listed
3. **Future**: Subscribe to professional API if budget allows

---

## 2. Individual Stock Data (PRIORITY 2 - Issues #6-#12)

### What We Need:
For each stock (FCCL, POWER, PIOC, HBL, OGDC, etc.):
- **Current price**
- **Daily change** (% and absolute)
- **Volume**
- **Market cap**
- **P/E ratio**
- **Dividend yield**
- **EPS** (Earnings Per Share)
- **Sector classification**
- **52-week range**

### Data Sources:

#### Option A: PSX Stock Quotes API
- Official source for all KSE100 stocks
- Need to check: https://www.psx.com.pk/market-data
- **Status**: ❓ Requires investigation

#### Option B: Scraping PSX Website
- URL pattern: `https://www.psx.com.pk/psx/resources-and-tools/listed-companies/`
- Parse HTML for stock data
- Libraries: BeautifulSoup, Selenium (if JavaScript rendered)

#### Option C: Yahoo Finance (yfinance)
```python
import yfinance as yf
# Try symbols like: FCCL.KA, POWER.KA (KA = Karachi?)
ticker = yf.Ticker("FCCL.KA")
```
**Status**: Need to verify correct ticker symbols

---

## 3. Sector Data (PRIORITY 2 - Issue #5)

### What We Need:
- **Sector names** (Cement, Banking, Oil & Gas, etc.)
- **Sector performance** (daily change %)
- **Sector P/E ratio** (average)
- **Number of companies** per sector
- **Market cap** per sector

### Data Sources:
- **PSX Sector Indices**: https://www.psx.com.pk/market-data
- Need aggregate data for each sector
- **Status**: Likely requires web scraping or manual compilation

---

## 4. Historical Stock Prices (PRIORITY 3 - Issue #13)

### What We Need:
- **Daily OHLC** (Open, High, Low, Close) for past 10 years
- **Volume** data
- For all KSE100 constituent stocks

### Data Sources:

#### Option A: PSX Historical Data
- Check if PSX provides historical data download
- CSV/Excel format preferred

#### Option B: Yahoo Finance Historical
```python
import yfinance as yf
ticker = yf.Ticker("FCCL.KA")
hist = ticker.history(period="10y")  # 10 years
```

#### Option C: Quandl (Now part of Nasdaq Data Link)
- Might have emerging market data
- **Cost**: Paid subscription likely needed

---

## 5. Financial Statements (PRIORITY 4 - Issues #14-#17)

### What We Need (per company):
- **Income Statement**: Revenue, expenses, net income (10 years)
- **Balance Sheet**: Assets, liabilities, equity (10 years)
- **Cash Flow Statement**: Operating, investing, financing cash flows (10 years)
- **Financial Ratios**: P/E, P/B, ROE, ROA, debt-to-equity, etc.

### Data Sources:

#### Option A: Company Annual Reports (PDF)
- Download from PSX or company websites
- Extract data using:
  - Manual entry (time-consuming)
  - PDF parsing (PyPDF2, pdfplumber)
  - OCR if needed (Tesseract)

#### Option B: SECP (Securities & Exchange Commission of Pakistan)
- Website: https://www.secp.gov.pk
- Check for financial statement repositories

#### Option C: Business Recorder / Financial Websites
- Some websites aggregate financial data
- May require web scraping

#### Option D: Financial Data APIs
- **Financial Modeling Prep**: Has some emerging markets
- **Alpha Vantage**: Limited international coverage
- **Status**: ❓ Need to verify KSE coverage

---

## 6. News & Sentiment Data (PRIORITY 5 - Future)

### What We Need:
- Company-related news articles
- Market news
- Regulatory announcements

### Data Sources:
- **Dawn News API** (if available)
- **Business Recorder** web scraping
- **PSX Announcements**: https://www.psx.com.pk/psx/exchange/listed-companies/announcements
- **RSS Feeds** from Pakistani business news sites

---

## Implementation Plan

### Phase 1: KSE100 Index (Issue #3 - Real Data)
**Timeline**: 1-2 days

**Tasks**:
1. ✅ Research PSX website structure
2. ✅ Try Yahoo Finance for KSE100 (symbol verification)
3. ✅ Implement web scraper for PSX if needed
4. ✅ Create data fetching service
5. ✅ Replace mock data with real data
6. ✅ Add caching (Redis) to respect rate limits

**Deliverable**: Dashboard shows real KSE100 index value

### Phase 2: Top Stocks Data (Issue #6)
**Timeline**: 2-3 days

**Tasks**:
1. Get list of top 10-20 KSE100 stocks
2. Fetch current prices for these stocks
3. Build stock table with real data
4. Implement auto-refresh

**Deliverable**: Top contributors table shows real stock prices

### Phase 3: Sector Summary (Issue #5)
**Timeline**: 2 days

**Tasks**:
1. Compile sector classification for all stocks
2. Aggregate data by sector
3. Calculate sector metrics
4. Build sector summary API

**Deliverable**: Sector summary with real performance data

### Phase 4: Financial Statements (Issues #14-17)
**Timeline**: 1-2 weeks

**Tasks**:
1. Collect annual reports for key companies (FCCL, POWER, PIOC)
2. Extract financial data (automated or manual)
3. Store in database
4. Build financial analysis APIs

**Deliverable**: Company detail pages with 10-year financials

---

## Budget Considerations

### Free Options:
- ✅ Web scraping PSX website
- ✅ Yahoo Finance (if KSE100 data available)
- ✅ Manual data collection from annual reports
- **Cost**: $0, but time-intensive

### Paid Options (If Needed):
- **Financial Modeling Prep**: $14.99/month (250 API calls/day → 7,500/month)
- **Alpha Vantage Premium**: $49.99/month (more calls)
- **Professional Data Provider**: $100-500/month (comprehensive)

### Recommended: Start Free
1. Begin with web scraping (free)
2. Monitor API usage
3. Upgrade only if scraping becomes unreliable or blocked

---

## Data Update Frequency

### Real-time (Every 30 seconds):
- ❌ Not feasible with free APIs
- ❌ Requires WebSocket or professional data feed

### Frequent (Every 5 minutes):
- ✅ Feasible with web scraping
- ✅ Within free API limits
- ✅ Good for day trading dashboard

### Moderate (Every 15-30 minutes):
- ✅ Recommended for MVP
- ✅ Low API usage
- ✅ Still useful for investors

### Daily (End of day):
- ✅ Easiest to implement
- ✅ Sufficient for long-term investors
- ✅ Can cache all day

**Recommendation**: Start with **15-minute intervals** for index, **daily** for financial statements

---

## Technical Implementation

### Backend Architecture:
```
Data Sources → Scrapers/APIs → Redis Cache → FastAPI → Frontend
                     ↓
              PostgreSQL (historical)
```

### Files to Create:
1. `backend/app/services/psx_scraper.py` - PSX website scraper
2. `backend/app/services/yahoo_finance.py` - Yahoo Finance integration
3. `backend/app/services/data_fetcher.py` - Unified data fetching
4. `backend/app/tasks/scheduler.py` - Celery/APScheduler for periodic updates
5. `backend/app/cache/redis_client.py` - Caching layer

---

## Action Items for User

### Immediate (Next 48 hours):
1. **Verify PSX API**: Check https://www.psx.com.pk for official API documentation
2. **Test Yahoo Finance**: Try symbol `^KSE100` or variations in yfinance
3. **Check Data Access**: Confirm no login/subscription needed for PSX website data
4. **Budget Approval**: Confirm $0 budget (scraping) or approve $15/month for API

### Short-term (Next week):
1. **Provide company list**: Top 20-30 KSE100 stocks you want to track
2. **Sector classification**: List of sectors and which stocks belong to each
3. **Priority companies**: Which 3-5 companies for detailed analysis first (you said FCCL, POWER, PIOC)

### Medium-term (Next month):
1. **Annual reports**: Links to PDF annual reports for priority companies
2. **Data validation**: Review scraped data for accuracy

---

## Questions for You

1. **Do you have access to any paid financial data APIs?**
2. **Is web scraping PSX website acceptable to you?** (legal/ethical considerations)
3. **What update frequency do you need?** (Real-time, 15-min, daily?)
4. **Which stocks are most important?** (Beyond FCCL, POWER, PIOC)
5. **Do you have existing data sources** you're currently using?

---

## Next Steps

Once you provide:
- ✅ Data source preferences (scraping OK? API access?)
- ✅ Update frequency requirements
- ✅ Priority stocks list

I will:
1. Implement data fetching service
2. Replace mock data with real data
3. Add caching and error handling
4. Test with actual KSE100 data
5. Deploy to your dashboard

**Estimated time to real data: 2-5 days** (depending on data source complexity)

