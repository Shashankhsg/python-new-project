# Frontend - React Proposal App

A beautiful, interactive React frontend for proposing to your crush!

## Features

- 🎨 Beautiful animated UI with hearts
- 📱 Responsive design for all devices
- ✨ Smooth transitions and animations
- 🎭 Dodging "No" button (can't reject!)
- ⚡ Fast with Vite dev server

## Project Structure

```
src/
├── components/
│   ├── BirthdayQuestion.jsx       # First page - boyfriend question
│   ├── BirthdayQuestion.css       # Styling for first page
│   ├── Proposal.jsx               # Second page - proposal message
│   └── Proposal.css               # Styling for proposal
├── App.jsx                        # Main component with routing
├── App.css                        # Global styles
├── index.css                      # Base styles
└── main.jsx                       # Entry point
```

## Components

### BirthdayQuestion
Shows the first question with two buttons (Yes/No).
- Makes API call to backend
- Progresses to proposal page on "No"
- Shows message on "Yes"

### Proposal
Shows romantic proposal with animated hearts.
- "Yes" button accepts proposal
- "No" button moves away when hovered
- Shows success page on acceptance

### App
Main component that manages page routing and API communication.

## Installation

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start development server:
   ```bash
   npm run dev
   ```

3. Open browser to `http://localhost:3000`

## Available Scripts

```bash
npm run dev      # Start dev server on port 3000 or 5173
npm run build    # Build for production (creates dist folder)
npm run preview  # Preview production build locally
```

## Customization

### Change Proposal Message

Edit `src/components/Proposal.jsx`:

```jsx
<p>
  Your custom message here! Make it personal and heartfelt.
</p>
```

### Change Colors

Edit CSS gradient colors in:
- `src/components/BirthdayQuestion.css`
- `src/components/Proposal.css`

Example:
```css
background: linear-gradient(135deg, #color1 0%, #color2 100%);
```

### Add More Animations

Modify keyframes in CSS files:
```css
@keyframes customAnimation {
  0% { /* start */ }
  50% { /* middle */ }
  100% { /* end */ }
}
```

## Browser Support

- Chrome ✅
- Firefox ✅
- Safari ✅
- Edge ✅
- Mobile browsers ✅

## Performance

- Fast reload with Vite HMR
- Optimized production build
- Minimal dependencies
- No unnecessary re-renders

## Deployment

1. Build for production:
   ```bash
   npm run build
   ```

2. Deploy `dist` folder to:
   - Vercel
   - Netlify
   - Any static hosting

3. Update API URL in environment variables

## Environment Variables

Create `.env` file:
```
VITE_API_URL=http://localhost:8000
```

## API Communication

Uses Axios to communicate with FastAPI backend:
- `POST /api/has-boyfriend` - Send first question response
- `POST /api/proposal-response` - Send proposal response

## State Management

Uses React hooks:
- `useState` for page navigation and loading state
- Props passing between components

## Styling

- Pure CSS3 (no CSS-in-JS)
- Animations and transitions
- Responsive flexbox layout
- Mobile-first approach

---

**Made with 💕 for special moments**
