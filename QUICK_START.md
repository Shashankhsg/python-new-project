# Proposal App - Quick Start Guide

## Prerequisites
- Python 3.8+
- Node.js 14+ and npm
- Gmail account for sending emails

## Super Quick Start

### Terminal 1 - Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# ⚠️ IMPORTANT: Edit backend/email_service.py and add your Gmail credentials
# SENDER_EMAIL = "your-email@gmail.com"
# SENDER_PASSWORD = "your-app-password"

uvicorn main:app --reload
```

### Terminal 2 - Frontend
```bash
cd frontend
npm install
npm run dev
```

### Open Browser
Go to `http://localhost:3000` (or the URL shown in Terminal 2)

## Email Setup Help

1. Go to https://myaccount.google.com/
2. Click **Security** in left sidebar
3. if 2FA not enabled, enable it
4. Scroll down to **App passwords**
5. Select "Mail" and "Windows Computer"
6. Google will generate a 16-character password
7. Copy that password to `backend/email_service.py` as `SENDER_PASSWORD`

## Done! 🎉
Share the app link with your crush and let the magic happen! ✨
