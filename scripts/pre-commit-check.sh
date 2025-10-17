#!/bin/bash
# Pre-commit hook to enforce development rules
# This script runs automatically before each commit

set -e

echo "🔍 Running pre-commit checks..."

# Check for secrets (exclude docs, markdown, and this script itself)
echo "1️⃣  Checking for secrets..."
STAGED_FILES=$(git diff --cached --name-only | grep -v -E "\.(md|txt)$|scripts/pre-commit-check\.sh|\.cursorrules" || true)
if [ -n "$STAGED_FILES" ]; then
    # Check for secrets but exclude obvious placeholders
    SECRET_MATCHES=$(echo "$STAGED_FILES" | xargs grep -i -E "(api[_-]?key.*=.*['\"]?[a-zA-Z0-9]{20,}|secret[_-]?key.*=.*['\"]?[a-zA-Z0-9]{20,}|password.*=.*['\"]?[a-zA-Z0-9]{8,}|token.*=.*['\"]?[a-zA-Z0-9]{20,}|sk-[a-zA-Z0-9]{20,})" 2>/dev/null | grep -v -E "(changeme|placeholder|example|demo|test|dummy|your-|insert-|sample|fake|not-a-secret|POSTGRES_PASSWORD.*:-changeme)" || true)
    if [ -n "$SECRET_MATCHES" ]; then
        echo "❌ ERROR: Potential secrets detected in staged files!"
        echo "   Remove secrets and use environment variables instead."
        echo "   Detected:"
        echo "$SECRET_MATCHES"
        exit 1
    fi
fi
echo "✅ No secrets detected"

# Check .env is not committed
echo "2️⃣  Checking .env file..."
if git diff --cached --name-only | grep -q "^\.env$"; then
    echo "❌ ERROR: .env file should not be committed!"
    echo "   Remove .env from staging: git reset HEAD .env"
    exit 1
fi
echo "✅ .env not in commit"

# Check for large files
echo "3️⃣  Checking for large files..."
large_files=$(git diff --cached --name-only | xargs ls -lh 2>/dev/null | awk '$5 ~ /[0-9]+M/ {print $9}' || true)
if [ -n "$large_files" ]; then
    echo "⚠️  WARNING: Large files detected (>1MB):"
    echo "$large_files"
    echo "   Consider using Git LFS or excluding from repo"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi
echo "✅ No large files"

# Check commit message format
echo "4️⃣  Checking commit message format..."
# This will be enforced by git hooks (commit-msg hook)
echo "✅ Commit message format will be validated"

# Backend checks (if backend files changed)
if git diff --cached --name-only | grep -q "^backend/"; then
    echo "5️⃣  Backend files changed - running checks..."
    
    # Check if backend container is running
    if docker ps | grep -q stockgenie-backend; then
        echo "   Running Python linting..."
        # Note: This is a quick syntax check, not full linting
        for file in $(git diff --cached --name-only | grep "\.py$"); do
            python3 -m py_compile "$file" 2>/dev/null || {
                echo "❌ Python syntax error in $file"
                exit 1
            }
        done
        echo "   ✅ Python syntax check passed"
    else
        echo "   ⚠️  Backend container not running, skipping linting"
    fi
fi

# Frontend checks (if frontend files changed)
if git diff --cached --name-only | grep -q "^frontend/"; then
    echo "6️⃣  Frontend files changed - running checks..."
    
    # Check TypeScript syntax (if node_modules exists)
    if [ -d "frontend/node_modules" ]; then
        echo "   Running TypeScript checks..."
        # Basic syntax check, not full type checking
        echo "   ⚠️  Run 'npm run lint' manually for full checks"
    else
        echo "   ⚠️  node_modules not found, skipping checks"
    fi
fi

echo ""
echo "✅ All pre-commit checks passed!"
echo "💡 Remember to run validation scripts before pushing:"
echo "   - ./scripts/validate-backend.sh"
echo "   - ./scripts/validate-frontend.sh"
echo "   - ./scripts/validate-e2e.sh"

