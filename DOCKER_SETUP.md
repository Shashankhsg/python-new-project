# 🐳 Docker Setup Guide (Optional)

This guide helps you containerize the application for easy deployment.

## Prerequisites

- Docker installed: https://www.docker.com/products/docker-desktop
- Docker Compose (comes with Docker Desktop)

## Option 1: Quick Docker Compose Setup

Create a `docker-compose.yml` file in the root directory:

```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - SENDER_EMAIL=${SENDER_EMAIL}
      - SENDER_PASSWORD=${SENDER_PASSWORD}
      - RECIPIENT_EMAIL=${RECIPIENT_EMAIL}
    volumes:
      - ./backend:/app
    command: uvicorn main:app --reload --host 0.0.0.0

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - VITE_API_URL=http://backend:8000
    volumes:
      - ./frontend:/app
      - /app/node_modules

volumes:
  backend:
  frontend:
```

### Backend Dockerfile

Create `backend/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Frontend Dockerfile

Create `frontend/Dockerfile`:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
```

### Run with Docker Compose

```bash
# Build images
docker-compose build

# Start services
docker-compose up

# Stop services
docker-compose down
```

---

## Option 2: Individual Docker Setup

### Build Backend Image

```bash
cd backend
docker build -t proposal-backend .
```

### Build Frontend Image

```bash
cd frontend
docker build -t proposal-frontend .
```

### Run Backend Container

```bash
docker run -p 8000:8000 \
  -e SENDER_EMAIL=your-email@gmail.com \
  -e SENDER_PASSWORD=app-password \
  -e RECIPIENT_EMAIL=shashankhsg@gmail.com \
  proposal-backend
```

### Run Frontend Container

```bash
docker run -p 3000:3000 \
  -e VITE_API_URL=http://localhost:8000 \
  proposal-frontend
```

---

## Deployment with Docker

### Push to Docker Hub

```bash
# Login to Docker Hub
docker login

# Tag images
docker tag proposal-backend username/proposal-backend
docker tag proposal-frontend username/proposal-frontend

# Push
docker push username/proposal-backend
docker push username/proposal-frontend
```

### Deploy to Cloud Platforms

**Using Railway:**
```bash
railway login
railway init
railway up
```

**Using Render:**
- Connect GitHub repo
- Select `docker-compose.yml`
- Set environment variables
- Deploy!

---

## Production Deployment

For production, update `docker-compose.yml`:

```yaml
version: '3.8'

services:
  backend:
    image: username/proposal-backend:latest
    restart: always
    environment:
      - SENDER_EMAIL=${SENDER_EMAIL}
      - SENDER_PASSWORD=${SENDER_PASSWORD}
      - RECIPIENT_EMAIL=${RECIPIENT_EMAIL}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    image: username/proposal-frontend:latest
    restart: always
    environment:
      - VITE_API_URL=${BACKEND_URL:-http://backend:8000}
    depends_on:
      backend:
        condition: service_healthy

  nginx:
    image: nginx:alpine
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - frontend
      - backend
```

---

## Troubleshooting Docker

### Container exits immediately

Check logs:
```bash
docker logs container-name
```

### Can't connect between containers

Use service names (from docker-compose.yml):
- Backend: `http://backend:8000`
- Frontend: `http://frontend:3000`

### Permission issues on Linux

```bash
sudo usermod -aG docker $USER
```

---

**Docker makes deployment super easy! 🐳**
