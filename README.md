# Flask DevOps Application

A containerized Python Flask web application demonstrating DevOps best practices including Docker containerization, environment variable management, GitHub Actions CI/CD, and automated dependency management with Dependabot.

## 🚀 Features

- **Flask Web Application** with two routes:
  - `/` - Home page displaying a custom message
  - `/health` - Health check endpoint
- **Docker Containerization** for consistent deployment
- **Environment Variables** for secure configuration management
- **GitHub Actions** for automated testing and deployment
- **Dependabot** for automated dependency updates
- **Beautiful UI** with gradient backgrounds and responsive design

## 📋 Prerequisites

- Docker and Docker Compose installed
- Git installed
- GitHub account (for CI/CD)

## 🛠️ Local Setup

1. **Clone the repository:**
```bash
   git clone <your-repo-url>
   cd <your-repo-name>
```

2. **Create environment file:**
```bash
   cp .env.example .env
```
   
   Edit `.env` if you want to customize the messages.

3. **Build and run with Docker Compose:**
```bash
   docker compose up --build
```

4. **Access the application:**
   - Home page: http://localhost:5000
   - Health check: http://localhost:5000/health

## 🐳 Docker Commands

**Build the image:**
```bash
docker build -t flask-devops-app .
```

**Run the container:**
```bash
docker run -d -p 5000:5000 --env-file .env flask-devops-app
```

**Stop the container:**
```bash
docker compose down
```

## 🔧 GitHub Setup

### Setting up GitHub Secrets

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the following secrets:
   - `APP_MESSAGE` - Your custom message for the home page
   - `APP_HEALTH` - Your custom health status message

### GitHub Actions Workflow

The workflow automatically:
- Triggers on push and pull requests to main/master branch
- Creates `.env` file from GitHub secrets
- Builds the Docker image
- Runs the container
- Tests both endpoints
- Provides debug information

## 📦 Dependencies

- **Python 3.11**
- **Flask 3.0.0**

Dependencies are automatically monitored by Dependabot for weekly updates.

## 🤖 Dependabot

Dependabot is configured to check for updates weekly (every Monday) for:
- Python pip packages
- Docker base images
- GitHub Actions

## 📁 Project Structure
```

|-- .github/
|   |- workflows/
|   |   |- main.yml           # GitHub Actions workflow
|   |-- dependabot.yml        # Dependabot configuration
|-- app.py                    # Flask application
|-- requirements.txt          # Python dependencies
|-- Dockerfile                # Docker configuration
|-- docker-compose.yml        # Docker Compose configuration
|-- .env                      # Environment variables (not in repo)
|-- .env.example              # Example environment variables
|-- .gitignore                # Git ignore rules
|-- README.md                 # This file


```
## Author
Onyeka Uzochukwu
Created as part of DevOps Assignment 4

## License

This project is for educational purposes.
```