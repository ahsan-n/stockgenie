# 📋 StockGenie Development Rules

## 🎯 Core Principles

### 1. Lean Slice Methodology
Every feature must be delivered as a **complete vertical slice** from frontend to database.

**What is a vertical slice?**
```
✅ Good Slice: "Display top 5 KSE100 stocks table"
   - Frontend: Stock table component
   - Backend: GET /api/v1/stocks/top endpoint
   - Database: stocks table with sample data
   - Validation: curl test + browser screenshot

❌ Bad Slice: "Create all database tables"
   - No user-facing value
   - Cannot be validated E2E
```

### 2. GitHub Issues as Source of Truth
- **All work** must have a corresponding GitHub issue
- No code without an issue number
- Issue must define:
  - **Acceptance criteria** (how to validate)
  - **API contract** (if backend work)
  - **Mock data** (if applicable)
  - **Real data source** (API or scraping target)

### 3. No Push Without Validation
Before pushing any code:
```bash
# Backend validation
./scripts/validate-backend.sh

# Frontend validation
./scripts/validate-frontend.sh

# E2E validation
./scripts/validate-e2e.sh
```

**Validation Checklist**:
- [ ] Backend: All new endpoints tested with `curl`
- [ ] Frontend: Manually tested in browser
- [ ] Database: Migrations applied successfully
- [ ] Docker: All containers start without errors
- [ ] Linting: No ESLint/Pylint errors
- [ ] Security: No secrets committed

### 4. Mock First, Real Data ASAP
**Phase 1: Mock Data** (0-2 hours)
- Hardcode sample data in backend
- Get frontend working end-to-end
- Validate UX and data structure

**Phase 2: Real Data** (within same day)
- Integrate actual API or scraper
- Replace mocks with real data
- Update tests with real scenarios

### 5. One Feature = One Commit
```bash
# Good commit message
git commit -m "feat: add KSE100 top stocks table (closes #12)"

# Include:
# - Type: feat/fix/chore/docs
# - Description: what was built
# - Issue reference: closes #X
```

## 🔀 Git Workflow

### Branch Naming
```
feat/issue-12-kse100-stocks-table
fix/issue-45-price-formatting
chore/issue-78-update-dependencies
docs/issue-90-api-documentation
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `chore`: Maintenance (deps, config)
- `docs`: Documentation
- `refactor`: Code restructuring
- `test`: Adding tests
- `perf`: Performance improvement

### Pull Request Process
1. Create branch from `main`
2. Complete work in small commits
3. Run validation scripts
4. Push and create PR
5. Self-review checklist:
   - [ ] All acceptance criteria met
   - [ ] Screenshots added (for UI changes)
   - [ ] API tested with curl examples
   - [ ] No console errors
   - [ ] No security issues
6. Merge only when validated

## 🧪 Testing Requirements

### Backend Testing
Every endpoint must have:
```bash
# Example curl test
curl -X GET "http://localhost:8000/api/v1/stocks/top?limit=5" \
  -H "Content-Type: application/json" | jq

# Expected output:
{
  "data": [
    {"symbol": "FCCL", "price": 25.50, "change": 1.2},
    ...
  ],
  "count": 5
}
```

**Test Script Template** (`tests/test_stocks.sh`):
```bash
#!/bin/bash
set -e

echo "Testing GET /api/v1/stocks/top"
response=$(curl -s http://localhost:8000/api/v1/stocks/top?limit=5)
count=$(echo $response | jq '.count')

if [ "$count" -eq 5 ]; then
  echo "✅ Test passed"
else
  echo "❌ Test failed: Expected 5 stocks, got $count"
  exit 1
fi
```

### Frontend Testing
Manual checklist per feature:
- [ ] Page loads without errors
- [ ] Data displays correctly
- [ ] Loading states work
- [ ] Error states handled
- [ ] Responsive on mobile
- [ ] No console warnings

**Screenshot Required**:
- Attach to PR showing working feature
- Include browser dev tools open (no errors)

### Integration Testing
For critical paths (e.g., stock detail page):
```bash
# 1. Start services
docker-compose up -d

# 2. Wait for health checks
./scripts/wait-for-services.sh

# 3. Run E2E test
./scripts/test-e2e-stock-detail.sh FCCL

# 4. Verify output
# - API returns 200
# - Frontend renders data
# - Database has stock record
```

## 📊 Data Management

### Mock Data Standards
**Location**: `backend/app/mocks/`

**Example**: `backend/app/mocks/stocks.py`
```python
MOCK_STOCKS = [
    {
        "symbol": "FCCL",
        "name": "Fauji Cement Company Limited",
        "sector": "Cement",
        "price": 25.50,
        "change": 1.2,
        "pe_ratio": 4.5,
        "dividend_yield": 8.2
    },
    # ... more stocks
]
```

**Toggle**: Environment variable
```bash
USE_MOCK_DATA=true  # Development
USE_MOCK_DATA=false # Production
```

### Real Data Integration
**Urgency**: Within same issue/PR if possible

**Process**:
1. Document API endpoint or scraping target in issue
2. Implement mock version first
3. Create service method for real data
4. Add error handling and retries
5. Test with actual API/scraping
6. Update `USE_MOCK_DATA` flag

**Example Service**:
```python
# backend/app/services/stock_service.py
class StockService:
    def get_top_stocks(self, limit: int = 10):
        if settings.USE_MOCK_DATA:
            return MOCK_STOCKS[:limit]
        else:
            # Real API call
            return self._fetch_from_psx_api(limit)
```

## 💰 Budget Management

### API Cost Tracking
**Budget**: $5/month (OpenAI + other APIs)

**Rules**:
- Monitor daily spend: `./scripts/check-api-usage.sh`
- Alert at 80% budget ($4)
- Hard limit at 100% ($5)

**Cost Optimization**:
```python
# ✅ Good: Cache embeddings
@cache(ttl=86400)  # 24 hours
def get_embedding(text: str):
    return openai.embeddings.create(...)

# ✅ Good: Batch processing
documents = [doc1, doc2, doc3, ...]
embeddings = openai.embeddings.create(input=documents)

# ❌ Bad: Per-request embeddings without cache
def chat(query: str):
    embedding = openai.embeddings.create(input=query)  # Costly!
```

**Development Mode**:
- Use smaller models: `gpt-3.5-turbo` instead of `gpt-4`
- Limit RAG context: 3 chunks instead of 5
- Use mock LLM responses for frontend dev

**Production Mode**:
- Aggressive caching (Redis)
- Rate limiting per user
- Semantic cache (similar queries return cached results)

## 🔐 Security Checklist

### Pre-Commit
- [ ] No hardcoded secrets (API keys, passwords)
- [ ] `.env` file not committed
- [ ] All secrets in `.env.example` are placeholders
- [ ] No sensitive data in logs

### Docker Security
- [ ] Non-root user in all Dockerfiles
```dockerfile
# ✅ Good
USER 1000

# ❌ Bad
# (running as root)
```
- [ ] Specific version tags (no `latest`)
```dockerfile
# ✅ Good
FROM python:3.11-slim

# ❌ Bad
FROM python:latest
```
- [ ] Multi-stage builds
```dockerfile
# ✅ Good
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
USER 1000
COPY --from=builder /app/.next ./.next
CMD ["npm", "start"]
```

### API Security
- [ ] Input validation (Pydantic models)
- [ ] Rate limiting (Redis-based)
- [ ] SQL injection prevention (parameterized queries)
- [ ] CORS properly configured
- [ ] Authentication on sensitive endpoints (future)

## 📈 Performance Standards

### Backend API
- **Response Time**: < 200ms (p95) for cached responses
- **Database Queries**: < 100ms for simple queries
- **Max Response Size**: 1MB (paginate larger datasets)

### Frontend
- **First Contentful Paint**: < 2s
- **Time to Interactive**: < 3s
- **Bundle Size**: < 500KB (initial load)

### Optimization Techniques
```typescript
// ✅ Good: Use TanStack Query for caching
const { data } = useQuery({
  queryKey: ['stocks', 'top'],
  queryFn: fetchTopStocks,
  staleTime: 60000, // 1 minute
})

// ✅ Good: Lazy load charts
const StockChart = dynamic(() => import('./StockChart'), {
  ssr: false,
  loading: () => <Spinner />
})

// ❌ Bad: Fetch on every render
useEffect(() => {
  fetch('/api/stocks/top').then(...)
}, []) // Missing dependencies, refetches unnecessarily
```

## 🚀 Deployment Checklist

### Pre-Deployment
- [ ] All tests passing
- [ ] No linter errors
- [ ] Documentation updated
- [ ] Environment variables documented
- [ ] Database migrations tested
- [ ] Docker build successful
- [ ] Security scan passed (Trivy)

### Deployment Steps
```bash
# 1. Pull latest
git pull origin main

# 2. Build images
docker-compose build

# 3. Run migrations
docker-compose run backend alembic upgrade head

# 4. Start services
docker-compose up -d

# 5. Health check
./scripts/health-check.sh

# 6. Smoke tests
./scripts/smoke-tests.sh
```

### Post-Deployment
- [ ] All services running
- [ ] Logs show no errors
- [ ] Key endpoints responding
- [ ] Database connections healthy
- [ ] Frontend accessible

## 📝 Documentation Requirements

### Code Documentation
```python
# ✅ Good: Clear docstrings
def get_financial_ratios(stock_id: int, period_end: date) -> FinancialRatios:
    """
    Retrieve financial ratios for a stock at a specific period.
    
    Args:
        stock_id: Database ID of the stock
        period_end: End date of the financial period
        
    Returns:
        FinancialRatios object with calculated metrics
        
    Raises:
        NotFoundError: If stock doesn't exist
        DataIncompleteError: If financial data is missing
    """
```

### API Documentation
FastAPI auto-generates docs, but add examples:
```python
@router.get("/stocks/top", response_model=StockListResponse)
async def get_top_stocks(
    limit: int = Query(10, ge=1, le=100, description="Number of stocks to return")
):
    """
    Get top performing stocks by market cap.
    
    Example:
        curl "http://localhost:8000/api/v1/stocks/top?limit=5"
    """
```

### Issue Documentation
Every issue must have:
```markdown
## Description
Clear explanation of what needs to be built

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## API Contract (if applicable)
```
GET /api/v1/stocks/top?limit=5
Response: {
  "data": [...],
  "count": 5
}
```

## Mock Data
[Link to mock data or inline JSON]

## Real Data Source
PSX API: https://... OR Scraping target: https://...

## Validation Steps
1. Start services: `docker-compose up`
2. Test endpoint: `curl ...`
3. Open frontend: http://localhost:3000/dashboard
4. Verify: Table shows 5 stocks
```

## 🎯 Definition of Done

A feature is **DONE** when:
- [x] Code written and committed
- [x] All acceptance criteria met
- [x] Backend validated with curl
- [x] Frontend validated in browser
- [x] No linter errors
- [x] No security issues
- [x] Docker containers start successfully
- [x] Documentation updated
- [x] PR reviewed and merged
- [x] Deployed to target environment

## 🚫 Anti-Patterns to Avoid

### ❌ Database-First Development
Don't create all tables before building features. Create tables as needed per slice.

### ❌ API-Without-Consumer
Don't build backend endpoints without a frontend consumer in the same PR.

### ❌ Premature Optimization
Don't optimize before measuring. Build working solution first.

### ❌ Feature Branching for Weeks
Keep branches short-lived (1-2 days max). Merge frequently.

### ❌ Mock Data Forever
Don't let mock data linger. Replace with real data ASAP.

### ❌ Ignoring Budget
Don't make unlimited API calls. Always check costs.

---

**Remember**: Ship small, ship often, validate always. 🚀

