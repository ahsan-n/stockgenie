# Validation Rules - MANDATORY

## Lesson Learned: October 16, 2025

**Incident**: Claimed dashboard was working, but it showed 404 errors in browser due to misconfigured API URL in `next.config.js`.

**Cost**: Wasted user time and money through careless validation.

---

## CRITICAL: Before Claiming "It Works"

### 1. End-to-End Browser Testing (MANDATORY)
- ✅ Open actual browser at the URL
- ✅ Verify data displays correctly (not loading spinner, not error)
- ✅ Check browser DevTools Network tab for API calls
- ❌ curl tests alone are NOT sufficient
- ❌ Never claim success without browser verification

### 2. Backend Log Verification
Check logs for:
- ✅ Correct request paths (e.g., `/api/v1/index/`)
- ❌ Doubled paths (e.g., `/api/v1/api/v1/index/`)
- ✅ 200 status codes from frontend requests (not just curl)
- ✅ No 404 errors

### 3. Configuration File Checklist

**Frontend** (`frontend/`):
- [ ] `next.config.js` - NEXT_PUBLIC_API_URL should be `http://localhost:8000` (NO `/api/v1` suffix)
- [ ] `lib/api.ts` - baseURL should NOT duplicate path prefixes
- [ ] `.env.local` - Check for URL overrides
- [ ] Verify: base URL + endpoint path = correct full URL

**Backend** (`backend/`):
- [ ] Router prefixes don't conflict
- [ ] Environment variables are correct

### 4. Systematic Debugging Process (MANDATORY ORDER)

When user reports an error:

1. **Check backend logs** (`tail -f /tmp/backend.log`)
   - What request paths are actually coming in?
   - Are they correct or malformed?

2. **Check frontend configuration**
   - `next.config.js` - API URL
   - `lib/api.ts` - baseURL configuration
   - `.env.local` - environment overrides

3. **Test in browser with DevTools**
   - Open Network tab
   - Refresh page
   - Check actual API calls being made

4. **Make targeted fix**
   - Fix the root cause (usually config)
   - Clear Next.js cache: `rm -rf .next`
   - Restart services

5. **Verify in browser**
   - Open browser
   - Verify data displays
   - Check backend logs show 200 OK

### 5. After Making Changes

Always:
- [ ] Clear Next.js cache if config changed: `rm -rf .next`
- [ ] Restart affected services
- [ ] Wait for rebuild (15+ seconds)
- [ ] Test in actual browser
- [ ] Check backend logs for new requests
- [ ] Verify 200 OK status codes

---

## Common Pitfalls

### ❌ DON'T
- Test only with curl
- Claim "it works" without browser test
- Make assumptions about what's wrong
- Change multiple things at once
- Skip checking configuration files

### ✅ DO
- Test end-to-end in browser
- Check logs before claiming success
- Verify configuration files first
- Make one change at a time
- Document what you tested

---

## Cost Awareness

**Every mistake has a cost:**
- User's time is valuable
- User pays for API usage
- Careless errors waste money
- Systematic approach saves resources

**Therefore:**
- Be methodical, not fast
- Verify thoroughly before claiming success
- Test the user's actual experience
- Don't waste time with trial and error

---

## API Configuration Reference

### Correct Setup

**frontend/next.config.js:**
```javascript
env: {
  NEXT_PUBLIC_API_URL: 'http://localhost:8000',  // ✅ No /api/v1 suffix
}
```

**frontend/lib/api.ts:**
```javascript
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE_URL,  // ✅ No /api/v1 here
});

// Endpoints include full path:
api.get('/api/v1/index/')  // ✅ Results in: http://localhost:8000/api/v1/index/
```

### Incorrect Setup (DON'T DO THIS)

**❌ Wrong:**
```javascript
env: {
  NEXT_PUBLIC_API_URL: 'http://localhost:8000/api/v1',  // ❌ Has suffix
}
```

**Result:** Doubled path: `/api/v1/api/v1/index/` → 404 error

---

## Checklist Before Pushing

- [ ] Tested in actual browser (not just curl)
- [ ] Backend logs show 200 OK from browser requests
- [ ] No 404 errors in backend logs
- [ ] Data displays correctly in browser
- [ ] No loading spinners or error messages
- [ ] Configuration files verified
- [ ] Changes documented in commit message

---

**Remember: User time = User money. Be thorough, not careless.**

