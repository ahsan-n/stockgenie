# GitHub Issues Template for StockGenie

This document contains all issues to be created on GitHub for project tracking.

## Phase 1: Foundation & Core Dashboards

### Issue #1: Project Setup & Docker Configuration
**Label**: `setup`, `infrastructure`
**Priority**: High
**Assignee**: @ahsan-n

**Description**:
Set up complete Docker development environment with all services.

**Acceptance Criteria**:
- [ ] All containers start successfully (`docker-compose up`)
- [ ] PostgreSQL + TimescaleDB accessible
- [ ] Redis accessible
- [ ] Qdrant accessible
- [ ] Backend health check passes
- [ ] Frontend loads on localhost:3000

**Validation**:
```bash
docker-compose up -d
./scripts/validate-e2e.sh
```

**Time Estimate**: 2 hours

---

### Issue #2: Database Schema - Core Tables
**Label**: `backend`, `database`
**Priority**: High
**Dependencies**: #1

**Description**:
Create core database tables for stocks, sectors, and market data.

**Acceptance Criteria**:
- [ ] `stocks` table created
- [ ] `sectors` table created
- [ ] `stock_prices` hypertable created (TimescaleDB)
- [ ] Alembic migration scripts created
- [ ] Sample data seeded (3-5 stocks)

**API Contract**:
N/A (database only)

**Validation**:
```bash
docker-compose exec postgres psql -U stockgenie -d stockgenie_db -c "\dt"
# Should show: stocks, sectors, stock_prices
```

**Time Estimate**: 3 hours

---

### Issue #3: KSE100 Index API - Mock Data
**Label**: `backend`, `api`, `mock`
**Priority**: High
**Dependencies**: #2

**Description**:
Create API endpoint for KSE100 index data with mock data.

**Acceptance Criteria**:
- [ ] GET `/api/v1/index` endpoint created
- [ ] Returns current index value, change %, market cap
- [ ] Mock data in `backend/app/mocks/index.py`
- [ ] API documentation in Swagger

**API Contract**:
```json
GET /api/v1/index

Response 200:
{
  "symbol": "KSE100",
  "value": 95000.50,
  "change": 250.30,
  "change_percent": 0.26,
  "market_cap": 8500000000000,
  "timestamp": "2024-01-15T14:30:00Z"
}
```

**Validation**:
```bash
curl http://localhost:8000/api/v1/index | jq
```

**Time Estimate**: 2 hours

---

### Issue #4: KSE100 Index Dashboard - Frontend
**Label**: `frontend`, `dashboard`
**Priority**: High
**Dependencies**: #3

**Description**:
Create KSE100 index dashboard page with real-time index display.

**Acceptance Criteria**:
- [ ] `/dashboard` route created
- [ ] Index value displayed prominently
- [ ] Change % with color coding (green/red)
- [ ] Loading and error states
- [ ] Responsive design

**Validation**:
- Open http://localhost:3000/dashboard
- Verify data from API displays correctly
- Test on mobile viewport

**Screenshot Required**: Yes

**Time Estimate**: 4 hours

---

### Issue #5: Sector Summary API - Mock Data
**Label**: `backend`, `api`, `mock`
**Priority**: High
**Dependencies**: #2

**Description**:
Create API endpoint for sector summary data.

**Acceptance Criteria**:
- [ ] GET `/api/v1/sectors` endpoint created
- [ ] Returns list of sectors with performance metrics
- [ ] Mock data for 5-7 sectors (Cement, Banking, Oil & Gas, etc.)
- [ ] Sortable by various metrics

**API Contract**:
```json
GET /api/v1/sectors?sort_by=change_percent&order=desc

Response 200:
{
  "data": [
    {
      "name": "Cement",
      "market_cap": 500000000000,
      "change_percent": 2.5,
      "stock_count": 15,
      "avg_pe_ratio": 4.8
    },
    ...
  ],
  "count": 7
}
```

**Validation**:
```bash
curl "http://localhost:8000/api/v1/sectors?sort_by=change_percent" | jq
```

**Time Estimate**: 3 hours

---

### Issue #6: Sector Summary Dashboard - Frontend
**Label**: `frontend`, `dashboard`
**Priority**: High
**Dependencies**: #5

**Description**:
Create sector summary dashboard with sortable table and charts.

**Acceptance Criteria**:
- [ ] `/dashboard/sectors` route created
- [ ] Sortable table of sectors
- [ ] Pie chart showing sector distribution
- [ ] Click sector → filter/navigate to details
- [ ] Responsive design

**Validation**:
- Open http://localhost:3000/dashboard/sectors
- Test sorting functionality
- Test chart rendering

**Screenshot Required**: Yes

**Time Estimate**: 5 hours

---

### Issue #7: Top Contributors Table API - Mock Data
**Label**: `backend`, `api`, `mock`
**Priority**: High
**Dependencies**: #2

**Description**:
Create API endpoint for KSE100 top contributors with key metrics.

**Acceptance Criteria**:
- [ ] GET `/api/v1/stocks/top` endpoint created
- [ ] Returns top N stocks by contribution/market cap
- [ ] Includes: price, P/E, sector P/E, dividend yield, EPS
- [ ] Mock data for 10-20 stocks
- [ ] Pagination support

**API Contract**:
```json
GET /api/v1/stocks/top?limit=10&offset=0

Response 200:
{
  "data": [
    {
      "symbol": "FCCL",
      "name": "Fauji Cement Company Limited",
      "sector": "Cement",
      "price": 25.50,
      "change_percent": 1.2,
      "pe_ratio": 4.5,
      "sector_pe_avg": 4.8,
      "dividend_yield": 8.2,
      "eps": 5.67,
      "market_cap": 50000000000
    },
    ...
  ],
  "total": 100,
  "page": 1,
  "per_page": 10
}
```

**Validation**:
```bash
curl "http://localhost:8000/api/v1/stocks/top?limit=5" | jq
```

**Time Estimate**: 4 hours

---

### Issue #8: Top Contributors Table - Frontend
**Label**: `frontend`, `component`
**Priority**: High
**Dependencies**: #7

**Description**:
Create top contributors table component with sorting and pagination.

**Acceptance Criteria**:
- [ ] Reusable table component created
- [ ] Sortable columns
- [ ] Pagination controls
- [ ] Row click → navigate to company page
- [ ] Export to CSV functionality (bonus)
- [ ] Responsive (horizontal scroll on mobile)

**Validation**:
- Display table on `/dashboard` page
- Test sorting on each column
- Test pagination
- Test navigation

**Screenshot Required**: Yes

**Time Estimate**: 6 hours

---

## Phase 2: Financial Deep-Dive (FCCL Company Page)

### Issue #9: Real Data Integration - PSX API/Scraping
**Label**: `backend`, `integration`, `scraping`
**Priority**: High
**Dependencies**: #3, #5, #7

**Description**:
Replace mock data with real PSX data (API or scraping).

**Acceptance Criteria**:
- [ ] Data source documented
- [ ] Scraper/API client implemented
- [ ] Data transformation pipeline
- [ ] Error handling and retries
- [ ] `USE_MOCK_DATA=false` works correctly
- [ ] Caching strategy implemented

**Validation**:
```bash
# Set USE_MOCK_DATA=false in .env
docker-compose restart backend
curl http://localhost:8000/api/v1/index | jq
# Verify real data returns
```

**Time Estimate**: 8 hours

---

### Issue #10: Company Detail API - FCCL
**Label**: `backend`, `api`
**Priority**: High
**Dependencies**: #2

**Description**:
Create API endpoint for individual company details.

**Acceptance Criteria**:
- [ ] GET `/api/v1/stocks/{symbol}` endpoint
- [ ] Returns comprehensive company info
- [ ] Includes latest financial metrics
- [ ] Mock data for FCCL initially

**API Contract**:
```json
GET /api/v1/stocks/FCCL

Response 200:
{
  "symbol": "FCCL",
  "name": "Fauji Cement Company Limited",
  "sector": "Cement",
  "description": "Brief company description...",
  "website": "https://fccl.com.pk",
  "listing_date": "1992-01-15",
  "current_price": 25.50,
  "market_cap": 50000000000,
  "shares_outstanding": 1960784314,
  "pe_ratio": 4.5,
  "dividend_yield": 8.2,
  "eps": 5.67,
  "book_value": 15.30
}
```

**Validation**:
```bash
curl http://localhost:8000/api/v1/stocks/FCCL | jq
```

**Time Estimate**: 3 hours

---

### Issue #11: Company Page - Frontend Layout
**Label**: `frontend`, `page`
**Priority**: High
**Dependencies**: #10

**Description**:
Create company detail page layout for FCCL.

**Acceptance Criteria**:
- [ ] `/company/[symbol]` dynamic route created
- [ ] Header with company name and key metrics
- [ ] Tab navigation (Overview, Financials, Analysis)
- [ ] Stock price chart (placeholder initially)
- [ ] Responsive design

**Validation**:
- Open http://localhost:3000/company/FCCL
- Verify all company data displays
- Test tab navigation

**Screenshot Required**: Yes

**Time Estimate**: 5 hours

---

### Issue #12: Financial Statements Schema
**Label**: `backend`, `database`
**Priority**: High
**Dependencies**: #2

**Description**:
Create database tables for financial statements.

**Acceptance Criteria**:
- [ ] `income_statements` table created
- [ ] `balance_sheets` table created
- [ ] `cashflow_statements` table created
- [ ] `financial_ratios` table created
- [ ] Alembic migrations
- [ ] Sample data for FCCL (3 years)

**Validation**:
```sql
SELECT * FROM income_statements WHERE stock_id = (SELECT id FROM stocks WHERE symbol = 'FCCL');
```

**Time Estimate**: 4 hours

---

### Issue #13: Income Statement API - FCCL
**Label**: `backend`, `api`
**Priority**: High
**Dependencies**: #12

**Description**:
Create API endpoint for income statements.

**Acceptance Criteria**:
- [ ] GET `/api/v1/stocks/{symbol}/financials/income` endpoint
- [ ] Returns annual and quarterly data
- [ ] Filter by period (annual/quarterly)
- [ ] Filter by date range
- [ ] Mock data for FCCL (10 years annual)

**API Contract**:
```json
GET /api/v1/stocks/FCCL/financials/income?period=annual&years=5

Response 200:
{
  "symbol": "FCCL",
  "period_type": "annual",
  "data": [
    {
      "period_end": "2023-12-31",
      "revenue": 45000000000,
      "cost_of_revenue": 30000000000,
      "gross_profit": 15000000000,
      "operating_expenses": 3000000000,
      "operating_income": 12000000000,
      "net_income": 10000000000,
      "eps": 5.10
    },
    ...
  ]
}
```

**Validation**:
```bash
curl "http://localhost:8000/api/v1/stocks/FCCL/financials/income?period=annual" | jq
```

**Time Estimate**: 4 hours

---

### Issue #14: Income Statement Page - Tabular View
**Label**: `frontend`, `financial`
**Priority**: High
**Dependencies**: #13

**Description**:
Create income statement page with tabular display.

**Acceptance Criteria**:
- [ ] `/company/[symbol]/income` route
- [ ] Table showing multi-year data
- [ ] Toggle annual/quarterly view
- [ ] Sortable columns
- [ ] Export to CSV
- [ ] Number formatting (thousands separators)

**Validation**:
- Open http://localhost:3000/company/FCCL/income
- Toggle annual/quarterly
- Test export

**Screenshot Required**: Yes

**Time Estimate**: 5 hours

---

### Issue #15: Income Statement Page - Graphical View
**Label**: `frontend`, `charts`
**Priority**: Medium
**Dependencies**: #14

**Description**:
Add graphical charts to income statement page.

**Acceptance Criteria**:
- [ ] Tab toggle: Table/Chart view
- [ ] Line chart for revenue/profit trends
- [ ] Bar chart for expense breakdown
- [ ] Interactive tooltips
- [ ] Recharts library integrated

**Validation**:
- Switch to chart view
- Hover over data points
- Verify data accuracy

**Screenshot Required**: Yes

**Time Estimate**: 4 hours

---

### Issue #16: Balance Sheet & Cash Flow APIs
**Label**: `backend`, `api`
**Priority**: High
**Dependencies**: #12

**Description**:
Create API endpoints for balance sheet and cash flow statements.

**Acceptance Criteria**:
- [ ] GET `/api/v1/stocks/{symbol}/financials/balance` endpoint
- [ ] GET `/api/v1/stocks/{symbol}/financials/cashflow` endpoint
- [ ] Same structure as income statement API
- [ ] Mock data for FCCL (10 years)

**Validation**:
```bash
curl "http://localhost:8000/api/v1/stocks/FCCL/financials/balance" | jq
curl "http://localhost:8000/api/v1/stocks/FCCL/financials/cashflow" | jq
```

**Time Estimate**: 5 hours

---

### Issue #17: Balance Sheet & Cash Flow Pages - Frontend
**Label**: `frontend`, `financial`
**Priority**: High
**Dependencies**: #16

**Description**:
Create balance sheet and cash flow pages (reuse income statement components).

**Acceptance Criteria**:
- [ ] `/company/[symbol]/balance` route
- [ ] `/company/[symbol]/cashflow` route
- [ ] Reuse table/chart components from income statement
- [ ] Custom metrics for each statement type

**Validation**:
- Test both pages
- Verify data displays correctly
- Test table/chart views

**Screenshot Required**: Yes

**Time Estimate**: 4 hours

---

### Issue #18: Financial Ratios API & Page
**Label**: `backend`, `frontend`, `api`
**Priority**: Medium
**Dependencies**: #12

**Description**:
Create financial ratios API endpoint and frontend page.

**Acceptance Criteria**:
- [ ] GET `/api/v1/stocks/{symbol}/financials/ratios` endpoint
- [ ] `/company/[symbol]/ratios` route
- [ ] Display ratios: P/E, P/B, ROE, ROA, Debt/Equity, Current Ratio
- [ ] Trend charts for key ratios
- [ ] Comparison with sector averages

**Validation**:
```bash
curl http://localhost:8000/api/v1/stocks/FCCL/financials/ratios | jq
```
Open http://localhost:3000/company/FCCL/ratios

**Screenshot Required**: Yes

**Time Estimate**: 6 hours

---

## Phase 3: RAG System & AI Chatbot

### Issue #19: PDF Ingestion Pipeline
**Label**: `backend`, `rag`, `ml`
**Priority**: High
**Dependencies**: None

**Description**:
Create pipeline to extract text from financial report PDFs.

**Acceptance Criteria**:
- [ ] PyMuPDF integration
- [ ] Extract text from PDFs (sample FCCL reports)
- [ ] Metadata extraction (company, date, report type)
- [ ] Store in `documents` table
- [ ] CLI script: `python scripts/ingest_reports.py`

**Validation**:
```bash
python scripts/ingest_reports.py data/raw/FCCL_Annual_2023.pdf
# Check documents table
```

**Time Estimate**: 6 hours

---

### Issue #20: Qdrant Vector Database Setup
**Label**: `backend`, `rag`, `infrastructure`
**Priority**: High
**Dependencies**: #19

**Description**:
Set up Qdrant for vector storage and create embeddings.

**Acceptance Criteria**:
- [ ] Qdrant collection created (`financial_documents`)
- [ ] OpenAI embeddings integration
- [ ] Batch embedding generation
- [ ] Text chunking strategy (1000 chars, 200 overlap)
- [ ] Metadata stored with vectors

**Validation**:
```bash
curl http://localhost:6333/collections/financial_documents
# Should return collection info
```

**Time Estimate**: 5 hours

---

### Issue #21: LangChain RAG Implementation
**Label**: `backend`, `rag`, `ml`
**Priority**: High
**Dependencies**: #20

**Description**:
Implement LangChain retrieval chain for Q&A.

**Acceptance Criteria**:
- [ ] LangChain document loader
- [ ] Retrieval QA chain configured
- [ ] GPT-4 or GPT-3.5 integration
- [ ] Conversational memory
- [ ] Cost tracking (token usage)

**Validation**:
```python
from app.rag import rag_service
response = rag_service.ask("What was FCCL's revenue in 2023?")
print(response)
```

**Time Estimate**: 8 hours

---

### Issue #22: Chat API Endpoint
**Label**: `backend`, `api`, `rag`
**Priority**: High
**Dependencies**: #21

**Description**:
Create API endpoint for AI chatbot.

**Acceptance Criteria**:
- [ ] POST `/api/v1/chat` endpoint
- [ ] Accepts: query, session_id, company_symbol (optional)
- [ ] Returns: answer, sources, confidence
- [ ] Rate limiting (prevent abuse)
- [ ] Session management (Redis)

**API Contract**:
```json
POST /api/v1/chat

Request:
{
  "query": "What was FCCL's net profit margin in 2023?",
  "session_id": "user-session-123",
  "company_symbol": "FCCL"
}

Response 200:
{
  "answer": "FCCL's net profit margin in 2023 was 22.2%...",
  "sources": [
    {
      "document": "FCCL Annual Report 2023",
      "page": 15
    }
  ],
  "confidence": 0.92,
  "tokens_used": 450
}
```

**Validation**:
```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"query":"What was FCCL revenue in 2023?","session_id":"test"}' | jq
```

**Time Estimate**: 5 hours

---

### Issue #23: Chat Interface - Frontend
**Label**: `frontend`, `chat`, `ai`
**Priority**: High
**Dependencies**: #22

**Description**:
Create AI chatbot interface page.

**Acceptance Criteria**:
- [ ] `/chat` route created
- [ ] Chat UI (messages, input box)
- [ ] Company context selector
- [ ] Loading indicator while waiting for AI
- [ ] Display sources in expandable section
- [ ] Session persistence
- [ ] Mobile-friendly

**Validation**:
- Open http://localhost:3000/chat
- Send test query
- Verify response renders correctly
- Test sources display

**Screenshot Required**: Yes

**Time Estimate**: 8 hours

---

## Phase 4: Multi-Company & Comparative Analysis

### Issue #24: Add Power Cement & Pioneer Cement Data
**Label**: `backend`, `data`
**Priority**: Medium
**Dependencies**: #12, #19

**Description**:
Add financial data and reports for Power Cement and Pioneer Cement.

**Acceptance Criteria**:
- [ ] Stocks added to `stocks` table
- [ ] Financial statements (10 years)
- [ ] PDF reports ingested
- [ ] Embeddings generated

**Validation**:
```bash
curl http://localhost:8000/api/v1/stocks/POWER | jq
curl http://localhost:8000/api/v1/stocks/PIOC | jq
```

**Time Estimate**: 6 hours (data collection + processing)

---

### Issue #25: Company Comparison API
**Label**: `backend`, `api`
**Priority**: Medium
**Dependencies**: #24

**Description**:
Create API endpoint for multi-company comparison.

**Acceptance Criteria**:
- [ ] GET `/api/v1/compare?symbols=FCCL,POWER,PIOC` endpoint
- [ ] Returns side-by-side metrics
- [ ] Financial ratios comparison
- [ ] Historical performance
- [ ] Sector benchmarking

**API Contract**:
```json
GET /api/v1/compare?symbols=FCCL,POWER,PIOC&metrics=revenue,net_income,pe_ratio

Response 200:
{
  "companies": ["FCCL", "POWER", "PIOC"],
  "comparison": {
    "revenue": {
      "2023": [45000000000, 38000000000, 42000000000],
      "2022": [42000000000, 35000000000, 39000000000]
    },
    "pe_ratio": {
      "current": [4.5, 5.2, 4.8]
    }
  }
}
```

**Validation**:
```bash
curl "http://localhost:8000/api/v1/compare?symbols=FCCL,POWER,PIOC" | jq
```

**Time Estimate**: 6 hours

---

### Issue #26: Comparison Dashboard - Frontend
**Label**: `frontend`, `dashboard`, `comparison`
**Priority**: Medium
**Dependencies**: #25

**Description**:
Create comparative analysis dashboard.

**Acceptance Criteria**:
- [ ] `/compare` route created
- [ ] Multi-select company picker
- [ ] Side-by-side table comparison
- [ ] Comparative charts (bar charts)
- [ ] Highlight best/worst performers
- [ ] Export comparison report

**Validation**:
- Open http://localhost:3000/compare
- Select 2-3 companies
- Verify comparison displays
- Test chart rendering

**Screenshot Required**: Yes

**Time Estimate**: 8 hours

---

### Issue #27: AI-Driven Comparative Insights
**Label**: `backend`, `frontend`, `ai`
**Priority**: Medium
**Dependencies**: #21, #26

**Description**:
Add AI-generated insights to comparison dashboard.

**Acceptance Criteria**:
- [ ] "Generate Insights" button on comparison page
- [ ] LLM analyzes selected companies
- [ ] Returns: strengths, weaknesses, recommendations
- [ ] Natural language summary
- [ ] Citations from reports

**Validation**:
- On comparison page, click "Generate Insights"
- Verify AI generates meaningful analysis

**Screenshot Required**: Yes

**Time Estimate**: 6 hours

---

## Infrastructure & DevOps

### Issue #28: CI/CD Pipeline - GitHub Actions
**Label**: `devops`, `ci-cd`
**Priority**: Medium

**Description**:
Set up GitHub Actions for automated testing and deployment.

**Acceptance Criteria**:
- [ ] `.github/workflows/ci.yml` created
- [ ] On PR: Run linters, tests
- [ ] On merge to main: Build Docker images
- [ ] Docker image security scanning (Trivy)
- [ ] Badge in README

**Time Estimate**: 4 hours

---

### Issue #29: Production Deployment Documentation
**Label**: `docs`, `devops`
**Priority**: Low

**Description**:
Document production deployment to EKS.

**Acceptance Criteria**:
- [ ] `docs/DEPLOYMENT.md` created
- [ ] EKS setup guide
- [ ] RDS/ElastiCache migration guide
- [ ] Environment variables for production
- [ ] SSL/TLS setup
- [ ] Monitoring setup (CloudWatch)

**Time Estimate**: 3 hours

---

### Issue #30: API Documentation & Postman Collection
**Label**: `docs`, `api`
**Priority**: Low

**Description**:
Create comprehensive API documentation and Postman collection.

**Acceptance Criteria**:
- [ ] Postman collection exported
- [ ] Example requests/responses
- [ ] Authentication guide
- [ ] Rate limiting documentation
- [ ] Error codes reference

**Time Estimate**: 3 hours

---

**Total Issues**: 30
**Total Estimated Time**: ~180 hours (4-5 months part-time)

