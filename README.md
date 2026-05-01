# Proposal App

A React + Vite app ready for deployment on GitHub Pages.

## Repo Structure

```text
python-new-project/
├── src/
│   ├── components/
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
├── index.html
├── vite.config.js
├── package.json
└── .env.example
```

## Local Setup

1. Install dependencies:
   ```bash
   npm install
   ```
2. Start dev server:
   ```bash
   npm run dev
   ```
3. Build production files:
   ```bash
   npm run build
   ```

## Environment

Create `.env` from `.env.example` and set:

```bash
VITE_API_URL=https://your-backend-url
```

This app calls:
- `POST {VITE_API_URL}/api/has-boyfriend`
- `POST {VITE_API_URL}/api/proposal-response`

## Deploy To GitHub Pages

`package.json` is configured with:
- `homepage`: `https://shashankhsg.github.io/python-new-project`
- `deploy` script using `gh-pages`

Deploy command:

```bash
npm run deploy
```

Then in GitHub repository settings:
1. Open **Settings** -> **Pages**
2. Set source to **Deploy from a branch**
3. Select branch **gh-pages** and folder **/(root)**

## Notes

- GitHub Pages only hosts static frontend files.
- Your backend API must be hosted separately (Render, Railway, Cloud Run, etc.).
