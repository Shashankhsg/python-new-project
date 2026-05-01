# Running the Application

## Prerequisites Check
```bash
python --version          # Should be 3.8 or higher
node --version           # Should be 14+ 
npm --version            # Should be 6+
```

## Step-by-Step Instructions

### Step 1: Backend Setup & Configuration

1. Open a terminal/PowerShell and navigate to backend:
   ```bash
   cd backend
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate virtual environment (Windows):
   ```bash
   venv\Scripts\activate
   ```
   
   Or on Mac/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Gmail (CRITICAL STEP)**:
   
   a. Open `email_service.py` in a text editor
   
   b. Replace these two lines:
      ```python
      SENDER_EMAIL = "your-email@gmail.com"
      SENDER_PASSWORD = "your-app-password"
      ```
   
   c. Instructions to get App Password:
      - Go to https://myaccount.google.com/
      - Click "Security" in the left sidebar
      - If 2-Step Verification is not enabled, enable it first
      - Scroll down to "App passwords" section
      - Select "Mail" as the app and "Windows Computer" as device
      - Copy the generated 16-character password
      - Replace `your-app-password` with this password

6. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   
   ✅ You should see: `Uvicorn running on http://127.0.0.1:8000`

### Step 2: Frontend Setup

1. Open a NEW terminal/PowerShell window

2. Navigate to frontend:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```
   
   ✅ You should see: `Local: http://localhost:3000` or similar

### Step 3: Open the Application

1. Open your web browser
2. Go to `http://localhost:3000` (or the URL shown in the terminal)
3. You should see the first page with "Do you have any boyfriend?" question

## Testing the Application

### Test Flow:

1. **Page 1**: Click "No" button
   - Should proceed to proposal page
   - Check backend terminal for logs

2. **Page 2**: 
   - Try clicking "No" - button should move around!
   - Click "Yes" - should show success page
   - Check your emails for the notification

### Check Logs:
- **Backend logs**: Should show API requests in the first terminal
- **Frontend logs**: Open browser DevTools (F12) to see any errors
- **Email logs**: Check `email_service.py` output in backend terminal

## Troubleshooting

### Problem: "Address already in use" on port 8000
**Solution**: Kill the process or use different port:
```bash
uvicorn main:app --reload --port 8001
```

### Problem: "Module not found" error in frontend
**Solution**: 
```bash
cd frontend
npm install
npm run dev
```

### Problem: "Port 3000 is already in use"
**Solution**: Vite will automatically use port 5173
```bash
# Or manually specify:
npm run dev -- --port 3001
```

### Problem: Email not sending
**Solution**:
1. Check Gmail credentials in `email_service.py`
2. Verify 2-Factor Authentication is enabled
3. Check "Less secure apps" setting if using regular password
4. Check backend logs for error messages
5. Test Gmail by trying to login manually

### Problem: CORS Error
**Solution**: Backend is already configured. If you see CORS errors:
- Make sure backend is running
- Check cors are aligned
- Verify API URL matches

### Problem: Frontend shows blank page
**Solution**:
1. Check browser console (F12 → Console tab)
2. Make sure backend is running (http://localhost:8000 should work)
3. Clear browser cache: Ctrl+Shift+Delete
4. Try hard refresh: Ctrl+F5

## Running in Production

1. **Build Frontend**:
   ```bash
   cd frontend
   npm run build
   ```
   Creates `dist` folder ready for deployment

2. **Deploy Frontend**:
   - Vercel/Netlify: Connect GitHub repo or upload `dist` folder
   - Traditional hosting: FTP the `dist` folder

3. **Deploy Backend**:
   - Railway/Render/Heroku: Push to git or Docker
   - Update CORS origins in `main.py` to match production URL

## Keeping it Secret

1. Don't share the GitHub repo link with your crush 😄
2. Deploy to a custom domain if possible
3. Consider password protecting the page
4. Share only the final deployed URL

## Need Help?

1. Check browser console (F12) for errors
2. Check backend terminal for error logs
3. Verify all prerequisites are installed
4. Make sure both backend and frontend are running
5. Clear cache and try again

---

**You're all set! The app is ready to help you propose to your crush! 💕**

Good luck! Remember, the best proposals come from the heart. 🎉✨
