#!/bin/bash
# Backend Validation Script
# Validates that backend is properly configured and running

set -e

echo "🔍 Validating Backend..."

# Check if backend container is running
if ! docker ps | grep -q stockgenie-backend; then
    echo "❌ Backend container is not running"
    echo "Run: docker-compose up -d backend"
    exit 1
fi

# Wait for backend to be ready
echo "⏳ Waiting for backend to be ready..."
max_attempts=30
attempt=0

while [ $attempt -lt $max_attempts ]; do
    if curl -s http://localhost:8000/api/v1/health > /dev/null 2>&1; then
        echo "✅ Backend is responding"
        break
    fi
    attempt=$((attempt + 1))
    sleep 1
done

if [ $attempt -eq $max_attempts ]; then
    echo "❌ Backend failed to respond after ${max_attempts} seconds"
    echo "Check logs: docker-compose logs backend"
    exit 1
fi

# Test health endpoint
echo "🧪 Testing health endpoint..."
response=$(curl -s http://localhost:8000/api/v1/health)
if echo "$response" | grep -q "healthy"; then
    echo "✅ Health check passed"
else
    echo "❌ Health check failed"
    echo "Response: $response"
    exit 1
fi

# Check database connection
echo "🧪 Testing database connection..."
db_check=$(docker-compose exec -T postgres pg_isready -U stockgenie 2>&1)
if echo "$db_check" | grep -q "accepting connections"; then
    echo "✅ Database connection OK"
else
    echo "❌ Database connection failed"
    exit 1
fi

# Check Redis connection
echo "🧪 Testing Redis connection..."
redis_check=$(docker-compose exec -T redis redis-cli ping 2>&1)
if echo "$redis_check" | grep -q "PONG"; then
    echo "✅ Redis connection OK"
else
    echo "❌ Redis connection failed"
    exit 1
fi

echo ""
echo "✅ All backend validations passed!"
echo "Backend API: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"

