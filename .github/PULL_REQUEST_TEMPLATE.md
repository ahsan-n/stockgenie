# Pull Request

## Issue Reference
Closes #<!-- issue number -->

## Description
<!-- Brief description of what this PR does -->

## Type of Change
- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 Documentation update

## Lean Slice Checklist
- [ ] This is a complete vertical slice (Frontend → API → Database)
- [ ] All acceptance criteria from the issue are met
- [ ] Mock data implemented (if applicable)
- [ ] Real data integration plan documented (if not yet implemented)

## Validation Checklist
### Backend
- [ ] Backend validation passed: `./scripts/validate-backend.sh`
- [ ] All new endpoints tested with `curl` (examples below)
- [ ] Database migrations run successfully
- [ ] No linter errors: `docker-compose exec backend black . && flake8 .`

### Frontend
- [ ] Frontend validation passed: `./scripts/validate-frontend.sh`
- [ ] Page loads without errors
- [ ] Tested in browser (Chrome/Safari)
- [ ] Tested on mobile viewport
- [ ] No ESLint errors: `npm run lint`

### E2E
- [ ] E2E validation passed: `./scripts/validate-e2e.sh`
- [ ] Feature works end-to-end
- [ ] Screenshots attached (for UI changes)

## Security Checklist
- [ ] No secrets committed (API keys, passwords, tokens)
- [ ] Environment variables documented in `.env.example`
- [ ] Input validation implemented (if applicable)
- [ ] SQL injection prevention verified (parameterized queries)
- [ ] No security warnings in logs

## API Testing (if applicable)
```bash
# Paste curl commands and responses here

curl http://localhost:8000/api/v1/... | jq

# Expected response:
{
  ...
}
```

## Screenshots (if applicable)
<!-- Attach screenshots for UI changes -->
<!-- Include browser dev tools showing no console errors -->

## Budget Impact (if applicable)
- [ ] No new API costs
- [ ] New API costs documented (estimated $X/month)
- [ ] Cost optimization implemented (caching, batching)

## Additional Notes
<!-- Any additional information reviewers should know -->

---

## Reviewer Checklist
- [ ] Code follows project structure
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No security issues
- [ ] Ready to merge
