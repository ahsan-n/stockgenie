---
name: Feature Request
about: Propose a new feature (use this for all development work)
title: '[FEATURE] '
labels: 'feature'
assignees: ''
---

## Description
<!-- Clear explanation of what needs to be built -->

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## API Contract (if applicable)
```json
GET /api/v1/endpoint?param=value

Response 200:
{
  "data": [...],
  "count": 0
}
```

## Mock Data (if applicable)
<!-- Link to mock data or inline JSON -->
```json
{
  "example": "data"
}
```

## Real Data Source
<!-- PSX API URL or scraping target -->
<!-- Example: https://dps.psx.com.pk/... -->

## Validation Steps
1. Start services: `docker-compose up`
2. Test endpoint: `curl http://localhost:8000/...`
3. Open frontend: http://localhost:3000/...
4. Verify: [specific behavior]

## Dependencies
<!-- Link to other issues that must be completed first -->
- Depends on #X
- Blocks #Y

## Time Estimate
<!-- Realistic estimate in hours -->
X hours

## Labels
<!-- Add relevant labels: backend, frontend, api, mock, integration, etc. -->

## Priority
<!-- High, Medium, Low -->
