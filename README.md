# 💕 Proposal App

A romantic full-stack web application to propose to your crush! Built with React (Frontend) and FastAPI (Backend).

## Features

- 🎯 Interactive proposal flow
- 💌 Automatic email notifications
- 🎨 Beautiful animated UI with hearts
- 🎭 Dodging "No" button (can't reject this proposal!)
- 📧 Email confirmation to your inbox

## Project Structure

```
python-new-project/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── email_service.py        # Email sending functionality
│   └── requirements.txt        # Python dependencies
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── BirthdayQuestion.jsx    # First page component
    │   │   ├── BirthdayQuestion.css    # Styling
    │   │   ├── Proposal.jsx             # Proposal page component
    │   │   └── Proposal.css             # Styling
    │   ├── App.jsx              # Main app component
    │   ├── index.css            # Global styles
    │   └── main.jsx             # Entry point
    ├── index.html              # HTML template
    ├── vite.config.js          # Vite configuration
    └── package.json            # Node dependencies
```

## Proposal Flow

1. **First Page**: "Do you have any boyfriend?"
   - **YES**: Email sent: "She has already a boyfriend"
   - **NO**: Proceed to proposal page

2. **Proposal Page**: Beautiful proposal message with two buttons
   - **YES Button**: Email sent: "Your proposal has been accepted!" → Success page
   - **NO Button**: Moves away when you try to hover/click (can't escape!)

## Setup Instructions

### Backend Setup (Python)

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Email (IMPORTANT)**:
   - Open `email_service.py`
   - Replace `your-email@gmail.com` with your Gmail address
   - Replace `your-app-password` with your Gmail App Password
   
   **To get Gmail App Password:**
   - Go to https://myaccount.google.com/
   - Click "Security" in the left menu
   - Enable 2-Factor Authentication if not already enabled
   - Scroll to "App passwords" and create one for "Mail" and "Windows Computer"
   - Use this password in the code

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   
   Server will run on `http://localhost:8000`

### Frontend Setup (React/Node.js)

1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   
   Frontend will run on `http://localhost:3000` or `http://localhost:5173`

## How to Use

1. **Start Backend**: Open terminal and run FastAPI server in the backend folder
2. **Start Frontend**: Open another terminal and run React development server in the frontend folder
3. **Open Browser**: Go to `http://localhost:3000` or the URL shown in your terminal
4. **Share the Link**: Send the link to your crush and wait for the magic to happen!

## Technologies Used

### Backend
- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server
- **Python smtplib**: Email sending

### Frontend
- **React 18**: UI library
- **Vite**: Build tool and dev server
- **Axios**: HTTP client
- **CSS3**: Animations and styling

## Email Configuration

Make sure to configure your Gmail credentials in `backend/email_service.py`:

```python
SENDER_EMAIL = "your-email@gmail.com"      # Change this
SENDER_PASSWORD = "your-app-password"      # Change this
RECIPIENT_EMAIL = "shashankhsg@gmail.com"  # Keep or change as needed
```

## Troubleshooting

### Backend Issues
- **Port already in use**: Change port in terminal: `uvicorn main:app --reload --port 8001`
- **Email not sending**: Check Gmail app password and 2FA settings
- **CORS errors**: Backend already configured to accept requests from React

### Frontend Issues
- **Module not found**: Run `npm install` again
- **Port 3000 occupied**: Vite will automatically use port 5173

## Customization

### Change Proposal Message
Edit the message in `frontend/src/components/Proposal.jsx` line ~30

### Change Colors
Edit CSS files:
- `frontend/src/components/BirthdayQuestion.css`
- `frontend/src/components/Proposal.css`
- `frontend/src/index.css`

### Change Email Recipients
Edit `backend/email_service.py` and change `RECIPIENT_EMAIL`

## Notes

- The "No" button is programmed to dodge when hovered/clicked - it will keep moving!
- All responses are logged via email
- The app is designed to be cute and romantic
- Works best on modern browsers (Chrome, Firefox, Safari, Edge)

## Good Luck! 💕

Remember, the best proposals are the ones that come from the heart. Use this app wisely and make it special!

---

**Created with ❤️ for a special someone**
