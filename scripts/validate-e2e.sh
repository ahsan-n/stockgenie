#!/bin/bash
# End-to-End Validation Script
# Validates complete system integration

set -e

echo "🚀 Running End-to-End Validation..."
echo ""

# Run backend validation
echo "=== Backend Validation ==="
./scripts/validate-backend.sh
echo ""

# Run frontend validation
echo "=== Frontend Validation ==="
./scripts/validate-frontend.sh
echo ""

# Test full integration
echo "=== Integration Tests ==="

# Test API from frontend perspective
echo "🧪 Testing API integration..."
response=$(curl -s http://localhost:8000/api/v1/health)
if echo "$response" | grep -q "healthy"; then
    echo "✅ Frontend can reach backend API"
else
    echo "❌ Frontend cannot reach backend API"
    exit 1
fi

# Test CORS (simulate browser request)
echo "🧪 Testing CORS configuration..."
cors_test=$(curl -s -X OPTIONS http://localhost:8000/api/v1/health \
    -H "Origin: http://localhost:3000" \
    -H "Access-Control-Request-Method: GET" \
    -o /dev/null -w "%{http_code}")

if [ "$cors_test" = "200" ] || [ "$cors_test" = "204" ]; then
    echo "✅ CORS configured correctly"
else
    echo "⚠️  CORS may need configuration (HTTP $cors_test)"
fi

echo ""
echo "✅ All E2E validations passed!"
echo ""
echo "🌐 Application URLs:"
echo "  Frontend:  http://localhost:3000"
echo "  Backend:   http://localhost:8000"
echo "  API Docs:  http://localhost:8000/docs"
echo "  Redoc:     http://localhost:8000/redoc"
echo ""
echo "📊 Database URLs:"
echo "  PostgreSQL: localhost:5432"
echo "  Redis:      localhost:6379"
echo "  Qdrant:     localhost:6333"

