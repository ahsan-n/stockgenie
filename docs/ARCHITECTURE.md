# 🏗️ StockGenie Architecture

## System Overview

StockGenie follows a modern, microservices-inspired architecture optimized for lean development and future scalability to EKS.

```
┌─────────────────────────────────────────────────────────────────────┐
│                          USERS / BROWSERS                            │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
┌─────────────────────────────────────────────────────────────────────┐
│                     NGINX (Reverse Proxy)                            │
│  • SSL/TLS Termination                                               │
│  • Rate Limiting                                                     │
│  • Static Asset Serving                                              │
└─────────────────────────────────────────────────────────────────────┘
                                  ↓
                    ┌─────────────┴─────────────┐
                    ↓                           ↓
┌──────────────────────────────┐  ┌──────────────────────────────┐
│     FRONTEND (Next.js)       │  │    BACKEND (FastAPI)         │
│  • Server-side rendering     │  │  • REST API endpoints        │
│  • Client-side routing       │  │  • Business logic            │
│  • Component library         │  │  • Data validation           │
│  • State management          │  │  • Authentication            │
│  Port: 3000                  │  │  Port: 8000                  │
└──────────────────────────────┘  └──────────────────────────────┘
                                            ↓
                    ┌───────────────────────┼───────────────────────┐
                    ↓                       ↓                       ↓
┌────────────────────────┐  ┌────────────────────────┐  ┌────────────────────┐
│  PostgreSQL + TimescaleDB│  │    Redis Cache         │  │  Qdrant Vector DB  │
│  • Stock prices          │  │  • API responses       │  │  • Embeddings      │
│  • Financial statements  │  │  • Session data        │  │  • RAG documents   │
│  • Company metadata      │  │  • Rate limit counters │  │  Port: 6333        │
│  Port: 5432              │  │  Port: 6379            │  └────────────────────┘
└────────────────────────┘  └────────────────────────┘
                                            ↓
                              ┌─────────────────────────┐
                              │   LangChain RAG System  │
                              │  • Document loaders     │
                              │  • Text splitters       │
                              │  • Retrieval chains     │
                              │  • LLM integration      │
                              └─────────────────────────┘
                                            ↓
                              ┌─────────────────────────┐
                              │   External Services     │
                              │  • OpenAI API           │
                              │  • PSX Data APIs        │
                              │  • Web Scraping targets │
                              └─────────────────────────┘
```

## Component Details

### Frontend Layer

**Technology**: Next.js 14 with App Router

**Responsibilities**:
- Server-side rendering for SEO and performance
- Client-side interactivity for charts and dashboards
- Responsive design for mobile and desktop
- Real-time data updates (polling/WebSocket)

**Key Libraries**:
- `shadcn/ui`: Accessible, customizable components
- `Recharts`: Financial charts and visualizations
- `TanStack Query`: Server state management and caching
- `Zod`: Runtime type validation

**Routes**:
```
/                          → Landing page
/dashboard                 → KSE100 Index Dashboard
/dashboard/sectors         → Sector Summary Dashboard
/company/[symbol]          → Company detail page (e.g., /company/FCCL)
/company/[symbol]/income   → Income statement
/company/[symbol]/cashflow → Cash flow statement
/company/[symbol]/balance  → Balance sheet
/company/[symbol]/ratios   → Financial ratios
/chat                      → AI Chatbot interface
/compare                   → Multi-company comparison
```

### Backend Layer

**Technology**: FastAPI (Python 3.11+)

**API Structure**:
```
/api/v1/
  ├── /health              → Health check
  ├── /index               → KSE100 index data
  ├── /sectors             → Sector summary
  ├── /stocks              → Stock list and search
  ├── /stocks/{symbol}     → Single stock details
  ├── /stocks/{symbol}/financials
  │     ├── /income        → Income statement
  │     ├── /cashflow      → Cash flow statement
  │     ├── /balance       → Balance sheet
  │     └── /ratios        → Financial ratios
  ├── /chat                → AI chatbot endpoint
  └── /compare             → Comparative analysis
```

**Services**:
- `StockService`: Market data operations
- `FinancialService`: Financial statement CRUD
- `RAGService`: AI/RAG operations
- `ScraperService`: Data collection
- `CacheService`: Redis operations

### Database Layer

#### PostgreSQL Schema

**Tables**:

```sql
-- Core entities
stocks (
  id SERIAL PRIMARY KEY,
  symbol VARCHAR(10) UNIQUE NOT NULL,
  name VARCHAR(200) NOT NULL,
  sector VARCHAR(100),
  listing_date DATE,
  created_at TIMESTAMP DEFAULT NOW()
)

-- Time-series price data (TimescaleDB hypertable)
stock_prices (
  stock_id INT REFERENCES stocks(id),
  timestamp TIMESTAMP NOT NULL,
  open DECIMAL(10,2),
  high DECIMAL(10,2),
  low DECIMAL(10,2),
  close DECIMAL(10,2),
  volume BIGINT,
  PRIMARY KEY (stock_id, timestamp)
)

-- Financial statements
income_statements (
  id SERIAL PRIMARY KEY,
  stock_id INT REFERENCES stocks(id),
  period_end DATE NOT NULL,
  period_type VARCHAR(10) CHECK (period_type IN ('annual', 'quarterly')),
  revenue DECIMAL(15,2),
  cost_of_revenue DECIMAL(15,2),
  gross_profit DECIMAL(15,2),
  operating_expenses DECIMAL(15,2),
  operating_income DECIMAL(15,2),
  net_income DECIMAL(15,2),
  eps DECIMAL(10,4),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(stock_id, period_end, period_type)
)

balance_sheets (
  id SERIAL PRIMARY KEY,
  stock_id INT REFERENCES stocks(id),
  period_end DATE NOT NULL,
  period_type VARCHAR(10) CHECK (period_type IN ('annual', 'quarterly')),
  total_assets DECIMAL(15,2),
  current_assets DECIMAL(15,2),
  total_liabilities DECIMAL(15,2),
  current_liabilities DECIMAL(15,2),
  shareholders_equity DECIMAL(15,2),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(stock_id, period_end, period_type)
)

cashflow_statements (
  id SERIAL PRIMARY KEY,
  stock_id INT REFERENCES stocks(id),
  period_end DATE NOT NULL,
  period_type VARCHAR(10) CHECK (period_type IN ('annual', 'quarterly')),
  operating_cashflow DECIMAL(15,2),
  investing_cashflow DECIMAL(15,2),
  financing_cashflow DECIMAL(15,2),
  free_cashflow DECIMAL(15,2),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(stock_id, period_end, period_type)
)

-- Financial ratios (calculated or stored)
financial_ratios (
  id SERIAL PRIMARY KEY,
  stock_id INT REFERENCES stocks(id),
  period_end DATE NOT NULL,
  pe_ratio DECIMAL(10,4),
  pb_ratio DECIMAL(10,4),
  roe DECIMAL(10,4),
  roa DECIMAL(10,4),
  debt_to_equity DECIMAL(10,4),
  current_ratio DECIMAL(10,4),
  dividend_yield DECIMAL(10,4),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(stock_id, period_end)
)

-- Sector aggregates
sector_summary (
  id SERIAL PRIMARY KEY,
  sector VARCHAR(100) NOT NULL,
  date DATE NOT NULL,
  avg_pe_ratio DECIMAL(10,4),
  total_market_cap DECIMAL(20,2),
  day_change_percent DECIMAL(10,4),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(sector, date)
)

-- Document storage for RAG
documents (
  id SERIAL PRIMARY KEY,
  stock_id INT REFERENCES stocks(id),
  document_type VARCHAR(50), -- 'annual_report', 'quarterly_report'
  period_end DATE,
  file_path TEXT,
  processed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
)
```

#### Redis Cache Strategy

**Key Patterns**:
```
stock:price:{symbol}:latest      → TTL: 60s (real-time price)
stock:details:{symbol}           → TTL: 5min (stock metadata)
sector:summary:{sector}          → TTL: 5min
index:kse100:latest              → TTL: 60s
api:ratelimit:{ip}:{endpoint}    → TTL: 60s (rate limiting)
chat:context:{session_id}        → TTL: 30min (chat history)
```

### RAG System Architecture

**Document Processing Pipeline**:
```
PDF Reports → PyMuPDF → Text Chunks → OpenAI Embeddings → Qdrant
                              ↓
                    Metadata Extraction
                  (Date, Company, Type)
```

**Retrieval Chain**:
```
User Query → Query Embedding → Qdrant Search → Top-K Documents → 
LLM Context → GPT-4 Response → Formatted Answer
```

**LangChain Components**:
- `Document Loaders`: PDF loaders with custom parsers
- `Text Splitters`: Recursive splitter (chunk_size=1000, overlap=200)
- `Embeddings`: OpenAI `text-embedding-3-small` (cost-optimized)
- `Vector Store`: Qdrant with HNSW indexing
- `Retrieval QA Chain`: Conversational retrieval with memory

**Cost Optimization**:
- Cache embeddings (don't regenerate for same text)
- Batch embed documents during off-peak hours
- Use smaller embedding model for initial tests
- Implement semantic caching for similar queries

## Data Flow Examples

### Example 1: Dashboard Load
```
User → /dashboard → Next.js SSR → API: GET /api/v1/index
                                → Check Redis cache
                                → If miss: Query PostgreSQL
                                → Cache result → Return JSON
                  ← Render dashboard with data
```

### Example 2: AI Chat Query
```
User → "What was FCCL's revenue in 2023?" 
     → POST /api/v1/chat
     → Embed query (OpenAI)
     → Search Qdrant (top 5 chunks)
     → Build context + retrieved docs
     → GPT-4 completion
     → Parse response
     ← "FCCL reported revenue of PKR X billion in 2023..."
```

### Example 3: Stock Price Update (Background Job)
```
Cron (every 5 min) → Scraper Service → Fetch PSX data
                                     → Transform/Validate
                                     → Bulk insert PostgreSQL
                                     → Invalidate Redis cache
```

## Deployment Architecture

### Local Development (Docker Compose)
```yaml
services:
  frontend, backend, postgres, redis, qdrant, nginx
```

### Future EKS Architecture
```
Route53 → ALB → EKS Cluster
                  ├── frontend-deployment (3 replicas)
                  ├── backend-deployment (3 replicas)
                  ├── worker-deployment (cron jobs)
                  └── External Services:
                       ├── RDS PostgreSQL
                       ├── ElastiCache Redis
                       └── Qdrant Cloud
```

## Security Considerations

1. **API Authentication**: JWT tokens for protected endpoints
2. **Rate Limiting**: Redis-based, per-IP and per-user
3. **Input Validation**: Pydantic models on all inputs
4. **SQL Injection**: Parameterized queries via SQLAlchemy
5. **Secrets Management**: Environment variables, AWS Secrets Manager (production)
6. **Container Security**: Non-root users, minimal base images
7. **CORS**: Strict origin allowlist

## Performance Targets

- **Dashboard Load**: < 2s (first load), < 500ms (cached)
- **API Response**: p95 < 200ms for cached, < 1s for DB queries
- **AI Chat Response**: < 5s for simple queries, < 10s for complex
- **Stock Price Update**: Real-time or 5-min delay acceptable

## Monitoring & Observability

- **Logging**: Structured JSON logs (ELK stack ready)
- **Metrics**: Prometheus-compatible metrics endpoint
- **Tracing**: OpenTelemetry (future)
- **Alerting**: Error rate, API latency, budget overruns

## Scalability Considerations

- **Horizontal Scaling**: Stateless backend, load-balanced
- **Database**: Read replicas for reporting queries
- **Caching**: Multi-tier (browser → Redis → DB)
- **CDN**: CloudFront for static assets (production)

