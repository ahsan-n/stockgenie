#!/bin/bash
# Setup Git Hooks for Development Rules Enforcement

echo "🔧 Setting up Git hooks..."

# Create hooks directory if it doesn't exist
mkdir -p .git/hooks

# Install pre-commit hook
echo "Installing pre-commit hook..."
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Pre-commit hook - runs before each commit

# Run pre-commit checks
./scripts/pre-commit-check.sh
EOF

chmod +x .git/hooks/pre-commit
echo "✅ Pre-commit hook installed"

# Install commit-msg hook
echo "Installing commit-msg hook..."
cat > .git/hooks/commit-msg << 'EOF'
#!/bin/bash
# Commit message hook - validates commit message format

commit_msg_file=$1
commit_msg=$(cat "$commit_msg_file")

# Check commit message format: type: description (closes #issue)
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|chore|refactor|test|perf|style)(\(.+\))?: .{10,}"; then
    echo "❌ Invalid commit message format!"
    echo ""
    echo "Format: <type>: <description> (closes #issue)"
    echo ""
    echo "Types:"
    echo "  - feat:     New feature"
    echo "  - fix:      Bug fix"
    echo "  - docs:     Documentation"
    echo "  - chore:    Maintenance"
    echo "  - refactor: Code restructuring"
    echo "  - test:     Adding tests"
    echo "  - perf:     Performance improvement"
    echo ""
    echo "Examples:"
    echo "  feat: add KSE100 index API (closes #3)"
    echo "  fix: resolve database connection issue (closes #15)"
    echo "  docs: update architecture documentation"
    echo ""
    exit 1
fi

# Check for issue reference (unless it's a docs/chore commit)
if echo "$commit_msg" | grep -qE "^(feat|fix|refactor|test|perf):"; then
    if ! echo "$commit_msg" | grep -qE "\(closes #[0-9]+\)"; then
        echo "⚠️  WARNING: Commit message should reference an issue"
        echo "   Format: feat: description (closes #X)"
        echo ""
        read -p "Continue without issue reference? (y/N) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
fi

echo "✅ Commit message format OK"
EOF

chmod +x .git/hooks/commit-msg
echo "✅ Commit-msg hook installed"

# Install pre-push hook
echo "Installing pre-push hook..."
cat > .git/hooks/pre-push << 'EOF'
#!/bin/bash
# Pre-push hook - runs before each push

# Run pre-push checks
./scripts/pre-push-check.sh
EOF

chmod +x .git/hooks/pre-push
echo "✅ Pre-push hook installed"

echo ""
echo "✅ All Git hooks installed successfully!"
echo ""
echo "These hooks will enforce:"
echo "  1. No secrets in commits (pre-commit)"
echo "  2. No .env file commits (pre-commit)"
echo "  3. Proper commit message format (commit-msg)"
echo "  4. E2E validation before push (pre-push)"
echo ""
echo "To bypass hooks (NOT RECOMMENDED):"
echo "  git commit --no-verify"
echo "  git push --no-verify"

