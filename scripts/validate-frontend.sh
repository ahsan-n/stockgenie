#!/bin/bash
# Frontend Validation Script
# Validates that frontend is properly configured and running

set -e

echo "🔍 Validating Frontend..."

# Check if frontend container is running
if ! docker ps | grep -q stockgenie-frontend; then
    echo "❌ Frontend container is not running"
    echo "Run: docker-compose up -d frontend"
    exit 1
fi

# Wait for frontend to be ready
echo "⏳ Waiting for frontend to be ready..."
max_attempts=60  # Frontend takes longer to start
attempt=0

while [ $attempt -lt $max_attempts ]; do
    if curl -s http://localhost:3000 > /dev/null 2>&1; then
        echo "✅ Frontend is responding"
        break
    fi
    attempt=$((attempt + 1))
    sleep 1
done

if [ $attempt -eq $max_attempts ]; then
    echo "❌ Frontend failed to respond after ${max_attempts} seconds"
    echo "Check logs: docker-compose logs frontend"
    exit 1
fi

# Test homepage
echo "🧪 Testing homepage..."
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000)
if [ "$response" = "200" ]; then
    echo "✅ Homepage loads successfully (HTTP $response)"
else
    echo "❌ Homepage failed to load (HTTP $response)"
    exit 1
fi

# Check for common errors in logs
echo "🧪 Checking for errors in logs..."
error_count=$(docker-compose logs frontend --tail=100 | grep -i "error" | grep -v "0 error" | wc -l || true)
if [ "$error_count" -eq 0 ]; then
    echo "✅ No errors in frontend logs"
else
    echo "⚠️  Found $error_count error(s) in frontend logs"
    echo "Review logs: docker-compose logs frontend"
fi

echo ""
echo "✅ All frontend validations passed!"
echo "Frontend URL: http://localhost:3000"
echo ""
echo "📋 Manual Testing Checklist:"
echo "  [ ] Open http://localhost:3000 in browser"
echo "  [ ] Check browser console for errors (F12)"
echo "  [ ] Verify all components render correctly"
echo "  [ ] Test responsive design (mobile view)"

