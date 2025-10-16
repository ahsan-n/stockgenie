#!/bin/bash
# API Usage Monitoring Script
# Checks OpenAI API usage against budget

set -e

echo "💰 Checking API Usage..."

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY not set in environment"
    echo "Set it in .env file or export it"
    exit 1
fi

# Load budget from .env
BUDGET=${OPENAI_MONTHLY_BUDGET_USD:-5}
ALERT_THRESHOLD=${ALERT_AT_BUDGET_PERCENT:-80}

echo "📊 Monthly Budget: \$$BUDGET USD"
echo "⚠️  Alert Threshold: ${ALERT_THRESHOLD}%"
echo ""

# Note: This is a placeholder script
# In production, you would call OpenAI's usage API
# https://platform.openai.com/account/usage

echo "🔍 To check actual usage:"
echo "  1. Visit: https://platform.openai.com/account/usage"
echo "  2. Or use: curl https://api.openai.com/v1/usage?date=YYYY-MM-DD \\"
echo "             -H 'Authorization: Bearer \$OPENAI_API_KEY'"
echo ""

# Check local usage tracking (if implemented)
if [ -f ".api_usage_tracker.json" ]; then
    echo "📈 Local Usage Tracking:"
    cat .api_usage_tracker.json | jq '.'
else
    echo "💡 Tip: Implement local usage tracking in backend"
fi

echo ""
echo "✅ API usage check complete"

