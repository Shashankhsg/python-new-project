# Proposal App - Features & Customization Guide

## Frontend Features

### 1. First Page: Boyfriend Question
- Beautiful animated hearts floating at the top
- Two buttons: "Yes" and "No"
- Smooth animations and transitions
- Responsive design for mobile and desktop

### 2. Proposal Page
- Romantic proposal message with customizable text
- Heart emojis with floating animation
- Two response buttons:
  - **Yes Button**: Direct path to success
  - **No Button**: Jumps away when hovered/clicked (fun UX!)
- Success page with celebration message

### 3. Styling
- Gradient backgrounds
- Smooth animations and transitions
- Heart emojis throughout
- Mobile-responsive design
- Box shadows and modern UI elements

## Backend Features

### 1. API Endpoints
- `POST /api/has-boyfriend` - Handles boyfriend question
- `POST /api/proposal-response` - Handles proposal response
- `GET /` - Health check

### 2. Email Service
- Sends emails via Gmail SMTP
- Customizable email content
- Error handling and logging
- Support for multiple recipients

### 3. CORS Support
- Allows requests from React frontend
- Configured for localhost development
- Easy to configure for production

## Customization Guide

### Change Proposal Message
File: `frontend/src/components/Proposal.jsx`

```jsx
<p>
  Your custom proposal message here!
  Make it personal and heartfelt.
</p>
```

### Change Color Scheme
Edit CSS files:
- Primary colors in `BirthdayQuestion.css`
- Gradient backgrounds in `Proposal.css`
- Global styles in `index.css`

Example gradient:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Add More Pages/Steps
1. Create new component file
2. Add to `App.jsx`
3. Add routing logic in state management

### Change Email Content
File: `backend/main.py`

```python
send_email(
    subject="Custom Subject",
    body="Custom message content here"
)
```

### Deploy to Production
1. Build frontend: `npm run build`
2. Deploy to Vercel, Netlify, or any hosting
3. Deploy backend to Heroku, Railway, or any cloud platform
4. Update API URLs in frontend environment variables

## Browser Compatibility
- Chrome ✅
- Firefox ✅
- Safari ✅
- Edge ✅
- Mobile browsers ✅

## Performance Tips
1. Optimize images if added
2. Use lazy loading for components
3. Minimize CSS bundle
4. Consider caching API responses

## Security Notes
- Never commit Gmail password to version control
- Use environment variables for sensitive data
- Validate input on both frontend and backend
- Consider rate limiting in production

Enjoy creating the perfect proposal experience! 💕
