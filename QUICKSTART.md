# 🚀 StockGenie - Quick Start Guide

> Get up and running in 5 minutes!

## Prerequisites

- Docker & Docker Compose installed
- Git installed
- Terminal/Command Line access

## 📦 Installation

### Step 1: Clone & Setup
```bash
cd stockgenie  # Already in this directory

# Copy environment file
cp .env.example .env

# Edit .env (optional for now, mock data works out of the box)
# nano .env
```

### Step 2: Start Services
```bash
# Start all Docker containers
docker-compose up -d

# This will start:
# - PostgreSQL (port 5432)
# - Redis (port 6379)
# - Qdrant (port 6333)
# - Backend API (port 8000)
# - Frontend (port 3000)

# Wait ~30 seconds for all services to be healthy
```

### Step 3: Verify Installation
```bash
# Run validation script
./scripts/validate-e2e.sh

# Expected output:
# ✅ Backend is responding
# ✅ Frontend is responding
# ✅ All E2E validations passed!
```

### Step 4: Access Applications
Open your browser:
- **Frontend**: http://localhost:3000
- **Backend API Docs**: http://localhost:8000/docs
- **Backend Health Check**: http://localhost:8000/api/v1/health

## 🧪 Test the API

```bash
# Test health endpoint
curl http://localhost:8000/api/v1/health | jq

# Expected output:
# {
#   "status": "healthy",
#   "timestamp": "2024-01-15T...",
#   "service": "stockgenie-backend"
# }
```

## 📊 What's Available Now?

### Backend (FastAPI)
- ✅ Health check endpoint: `GET /api/v1/health`
- ✅ Ping endpoint: `GET /api/v1/ping`
- ✅ API documentation: http://localhost:8000/docs
- ✅ Mock data structures ready

### Frontend (Next.js)
- ✅ Landing page: http://localhost:3000
- ✅ Basic layout with feature cards
- ✅ Ready for dashboard implementation

### Databases
- ✅ PostgreSQL + TimescaleDB running
- ✅ Redis caching layer running
- ✅ Qdrant vector database running

## 🛠️ Development Workflow

### Starting Development
```bash
# Check GitHub issues
# https://github.com/ahsan-n/stockgenie/issues

# Pick an issue (start with #2: Database Schema)
git checkout -b feat/issue-2-database-schema

# Make changes...
# Test changes...

# Validate before commit
./scripts/validate-backend.sh
./scripts/validate-frontend.sh

# Commit and push
git add .
git commit -m "feat: add core database tables (closes #2)"
git push origin feat/issue-2-database-schema

# Create Pull Request on GitHub
```

## 📋 Next Steps

### Immediate (Issue #2)
1. Install PostgreSQL client (psql)
2. Create Alembic migrations for core tables
3. Seed sample data
4. Validate database schema

### Short Term (Issues #3-8)
1. Implement KSE100 index API with mock data
2. Build dashboard frontend
3. Create sector summary API
4. Build sector dashboard
5. Implement top contributors API
6. Build top contributors table

### Medium Term (Issues #9-18)
1. Integrate real PSX data
2. Build FCCL company page
3. Add financial statements
4. Create charts and visualizations

### Long Term (Issues #19-30)
1. PDF ingestion pipeline
2. RAG system with LangChain
3. AI chatbot interface
4. Multi-company comparison
5. Production deployment

## 🐛 Troubleshooting

### Containers won't start
```bash
# Check Docker is running
docker --version

# Check logs
docker-compose logs

# Restart services
docker-compose down
docker-compose up -d
```

### Port conflicts
```bash
# Check what's using ports
lsof -i :3000
lsof -i :8000
lsof -i :5432

# Change ports in docker-compose.yml if needed
```

### Frontend not loading
```bash
# Check frontend container
docker-compose logs frontend

# Restart frontend
docker-compose restart frontend
```

### Backend API not responding
```bash
# Check backend container
docker-compose logs backend

# Check database connection
docker-compose exec postgres psql -U stockgenie -c "SELECT version();"

# Restart backend
docker-compose restart backend
```

## 🔧 Useful Commands

```bash
# Stop all services
docker-compose down

# Stop and remove volumes (CAUTION: deletes data)
docker-compose down -v

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Access database
docker-compose exec postgres psql -U stockgenie -d stockgenie_db

# Access Redis
docker-compose exec redis redis-cli

# Rebuild containers
docker-compose build --no-cache
docker-compose up -d

# Check API usage budget
./scripts/check-api-usage.sh
```

## 📚 Documentation

- **Full README**: [README.md](README.md)
- **Architecture**: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- **Development Rules**: [docs/DEVELOPMENT_RULES.md](docs/DEVELOPMENT_RULES.md)
- **GitHub Issues**: [docs/GITHUB_ISSUES.md](docs/GITHUB_ISSUES.md)
- **Project Summary**: [docs/PROJECT_SUMMARY.md](docs/PROJECT_SUMMARY.md)

## 🆘 Getting Help

- **GitHub Issues**: https://github.com/ahsan-n/stockgenie/issues
- **Documentation**: Check `docs/` directory
- **API Docs**: http://localhost:8000/docs (when running)

## ✅ Verification Checklist

Before starting development, ensure:
- [ ] Docker containers are running (`docker-compose ps`)
- [ ] Backend health check passes (http://localhost:8000/api/v1/health)
- [ ] Frontend loads (http://localhost:3000)
- [ ] PostgreSQL is accessible
- [ ] Redis is accessible
- [ ] Validation scripts pass (`./scripts/validate-e2e.sh`)

## 🎯 Your First Contribution

**Issue #2: Database Schema - Core Tables**

1. Create feature branch: `git checkout -b feat/issue-2-database-schema`
2. Read issue: https://github.com/ahsan-n/stockgenie/issues/2
3. Follow acceptance criteria
4. Run validations
5. Create PR

---

**Happy Coding! 🚀**

*Need help? Check the docs or create a GitHub issue.*

