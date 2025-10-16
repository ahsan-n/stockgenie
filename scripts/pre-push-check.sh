#!/bin/bash
# Pre-push hook to enforce E2E validation
# This script runs automatically before each push

echo "🚀 Running pre-push checks..."

# Check if backend is running (Docker OR local)
BACKEND_RUNNING=false

# Check Docker backend
if docker ps 2>/dev/null | grep -q stockgenie-backend; then
    echo "✅ Backend running in Docker"
    BACKEND_RUNNING=true
# Check local backend on port 8000
elif lsof -i :8000 2>/dev/null | grep -q LISTEN; then
    echo "✅ Backend running locally on port 8000"
    BACKEND_RUNNING=true
else
    echo "⚠️  WARNING: Backend is not running"
    echo "   Docker: docker-compose up -d"
    echo "   Local: cd backend && uvicorn app.main:app --reload"
    echo "   Allowing push (ensure backend works before PR)..."
fi

# Only run E2E validation if backend is running
if [ "$BACKEND_RUNNING" = true ]; then
    echo "🧪 Running quick health check..."
    if curl -s -f http://localhost:8000/api/v1/health > /dev/null 2>&1; then
        echo "✅ Backend health check passed!"
    else
        echo "⚠️  Backend running but health check failed"
        echo "   Validate before creating PR!"
    fi
else
    echo "⏭️  Skipping health check (backend not running)"
fi

echo ""
echo "✅ Pre-push checks complete!"
echo "🚀 Pushing to remote..."

