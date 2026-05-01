# Proposal App Backend

A FastAPI backend for handling proposal responses and sending email notifications.

## Features

- Fast and async request handling with FastAPI
- Email notifications via Gmail SMTP
- CORS support for React frontend
- Input validation with Pydantic
- Environment variable configuration

## API Endpoints

### `POST /api/has-boyfriend`

Handle the first question response.

**Request Body:**
```json
{
  "has_boyfriend": true
}
```

**Responses:**
- If `has_boyfriend` = true: Email sent, returns rejection message
- If `has_boyfriend` = false: Returns continue message

### `POST /api/proposal-response`

Handle the final proposal response.

**Request Body:**
```json
{
  "proposal_response": true
}
```

**Responses:**
- If `proposal_response` = true: Email sent, returns acceptance message
- If `proposal_response` = false: Returns rejection message (no email)

## Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
RECIPIENT_EMAIL=shashankhsg@gmail.com
FRONTEND_URL=http://localhost:3000
```

### Gmail App Password Setup

1. Go to https://myaccount.google.com/
2. Click **Security** in left sidebar
3. Enable 2-Step Verification if not already enabled
4. Go to **App passwords** (you may need to scroll down)
5. Select "Mail" and "Windows Computer"
6. Google generates a 16-character password
7. Use this password as `SENDER_PASSWORD`

## Installation

1. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file with your configuration

4. Run server:
   ```bash
   uvicorn main:app --reload
   ```

## Running in Production

```bash
# Without reload flag for production
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Error Handling

- All errors are caught and logged
- Email failures don't crash the server
- Detailed error messages in console logs

## Security Notes

- Never commit `.env` file to version control
- Use environment variables for sensitive data
- Consider rate limiting for production
- Validate CORS origins for production deployment

---

**Built with ❤️ for special moments**
