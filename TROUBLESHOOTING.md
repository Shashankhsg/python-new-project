# ❓ FAQ & Troubleshooting Guide

## Common Questions

### Q: How long will setup take?
**A:** About 10-15 minutes for initial setup, then deployment depends on your chosen platform.

### Q: Can I change the proposal message?
**A:** Yes! Edit `frontend/src/components/Proposal.jsx` - the message is in a `<p>` tag.

### Q: Where will the emails go?
**A:** To the address in `RECIPIENT_EMAIL` in `backend/email_service.py` (default: shashankhsg@gmail.com)

### Q: Can I deploy this?
**A:** Yes! Deploy frontend to Vercel/Netlify and backend to Railway/Render/Heroku.

### Q: Is the "No" button really undodgeable?
**A:** Almost! On mobile it might be clickable if the screen is large enough. It's designed to be fun!

### Q: Can I add music/videos?
**A:** Yes! Add `<video>` or `<audio>` tags in the JSX components and style them.

### Q: What if she has JavaScript disabled?
**A:** The app won't work. But who doesn't have JS enabled? 😄

### Q: Can I track if she opened the link?
**A:** Not with this setup, but you could add analytics like Google Analytics.

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'fastapi'"

**Solution:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Why:** Virtual environment not activated or dependencies not installed.

---

### Issue: "Cannot find module 'react'"

**Solution:**
```bash
cd frontend
npm install
```

**Why:** Node modules not installed.

---

### Issue: "Email failed to send"

**Solution:**

1. Check if 2FA is enabled:
   - Go to https://myaccount.google.com/security
   - Verify 2-Step Verification is ON

2. Verify App Password:
   - Go to App passwords
   - Make sure you selected "Mail" and correct device
   - Copy the 16-character password (no spaces)

3. Check `email_service.py`:
   ```python
   SENDER_EMAIL = "your-email@gmail.com"      # Your Gmail
   SENDER_PASSWORD = "xxxx xxxx xxxx xxxx"    # App password (16 chars)
   ```

4. Check backend logs for specific error

---

### Issue: "CORS error - blocked by browser"

**Solution:**

The backend already allows CORS. If you still get errors:

1. Make sure backend is running at http://localhost:8000
2. Check browser console (F12 → Console tab)
3. Verify API URL in frontend matches backend

---

### Issue: "Port 3000 is already in use"

**Solution:**

Vite will automatically use port 5173 instead. Or find what's using port 3000:

```bash
# Windows
netstat -ano | findstr :3000

# Mac/Linux
lsof -i :3000
```

Then either kill that process or use different port:
```bash
npm run dev -- --port 3001
```

---

### Issue: "Port 8000 is already in use"

**Solution:**

```bash
# Use different port
uvicorn main:app --reload --port 8001
```

Then update frontend to use port 8001.

---

### Issue: "Blank page or 404 errors"

**Solution:**

1. Hard refresh: Ctrl+Shift+Delete (clear cache)
2. Check browser console: F12 → Console tab
3. Verify both servers are running:
   - Backend: http://localhost:8000 (should show JSON)
   - Frontend: http://localhost:3000 (should show the app)

---

### Issue: "Button clicks don't work"

**Solution:**

1. Check browser console for JavaScript errors (F12)
2. Make sure backend is running
3. Hard refresh the page (Ctrl+F5)
4. Check network requests in DevTools (F12 → Network tab)

---

### Issue: "Frontend shows 'Cannot GET /api/...'"

**Solution:**

This means the frontend is hitting the wrong URL. Check:

1. Backend is running on http://localhost:8000
2. `vite.config.js` proxy configuration is correct
3. Or update API calls in `App.jsx` to use full URL

---

### Issue: "Email configuration keeps failing"

**Solution:**

Double-check each character in your Gmail credentials:

1. **SENDER_EMAIL**: Must be your Gmail address exactly
2. **SENDER_PASSWORD**: Must be the App Password (not your Gmail password!)
   - Should be 16 characters with spaces
   - Example: `xxxx xxxx xxxx xxxx`
3. Copy-paste directly from Google to avoid typos

---

### Issue: "The No button works on my phone"

**Solution:**

On smaller screens, the button might be easier to click. To make it even harder:

Edit `frontend/src/components/Proposal.jsx`:

```javascript
const handleNoMouseEnter = () => {
  moveNoButton()
  setHoveredNo(true)
}

// Add this for touch devices:
const handleNoTouchStart = () => {
  moveNoButton()
}

// Add to button:
onTouchStart={handleNoTouchStart}
```

---

## 🐛 Debug Mode

### Enable detailed logging

**Backend** - Edit `main.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

**Frontend** - Add to `App.jsx`:
```javascript
useEffect(() => {
  console.log('Response received:', response.data)
}, [])
```

---

## 📊 Test Checklist

Before deploying, test this flow:

- [ ] Start backend - no errors?
- [ ] Start frontend - no errors?
- [ ] Open app in browser
- [ ] Click "No" on page 1 - goes to page 2?
- [ ] "No" button on page 2 moves away?
- [ ] Click "Yes" on page 2 - success page shows?
- [ ] Check email - did you receive "proposal accepted"?
- [ ] Go back, click "Yes" on page 1 - email about boyfriend?
- [ ] All emails went to correct address?

---

## 🌐 Deployment Issues

### Issue: "Emails not sending in production"

**Solution:**

1. Set environment variables on hosting platform:
   - `SENDER_EMAIL`
   - `SENDER_PASSWORD`
   - `RECIPIENT_EMAIL`

2. Don't hardcode values in code

3. Verify backend can access Gmail (some hosting blocks SMTP)

---

### Issue: "Frontend can't reach backend in production"

**Solution:**

1. Update API URL for production:
   ```javascript
   const API_URL = process.env.VITE_API_URL || 'http://localhost:8000'
   ```

2. Set `VITE_API_URL` in frontend environment variables

3. Make sure backend is deployed and accessible

4. Update CORS origins in backend to match frontend domain

---

## 💡 Pro Tips

1. **Test locally first** before deploying
2. **Save your API credentials** securely
3. **Don't commit .env files** to Git
4. **Tell her about the app secretly** (ruins the surprise!)
5. **Have a backup plan** (proposal still works without app!)
6. **Keep error messages secret** (tell her it's "under maintenance")
7. **Check email setup** at least once before the big moment
8. **Test on mobile** if she'll use that device

---

## 🎯 Still Have Issues?

**Check in this order:**

1. Read SETUP_INSTRUCTIONS.md
2. Check error message in browser console (F12)
3. Check error message in backend terminal
4. Read this troubleshooting guide
5. Review code comments for hints
6. Try restarting both servers
7. Clear cache and hard refresh

---

## 🆘 Last Resort

If nothing works:

1. **Restart everything:**
   ```bash
   # Kill backend: Ctrl+C
   # Kill frontend: Ctrl+C
   # Manually delete venv folder
   # Start over from SETUP_INSTRUCTIONS.md
   ```

2. **Fresh install:**
   ```bash
   rm -rf backend/venv
   rm -rf frontend/node_modules
   # Follow SETUP_INSTRUCTIONS.md again
   ```

3. **Check Node/Python versions:**
   ```bash
   python --version  # Should be 3.8+
   node --version    # Should be 14+
   npm --version     # Should be 6+
   ```

---

**Remember:** Most issues are setup-related. Take it slow and follow SETUP_INSTRUCTIONS.md carefully! 💕

Good luck! You've got this! 🚀✨
