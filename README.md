# AI-Driven News Curator Chatbot

## Overview
This project is an AI-driven news curator chatbot that fetches real-time news articles based on user interests and summarizes them using NLP. The backend is powered by FastAPI, and the frontend is built with React.

## Features
- Fetches recent news based on a given topic
- Uses an AI-powered summarization model (`facebook/bart-large-cnn`)
- Supports CORS for frontend-backend communication
- Logs system processes for debugging

## Tech Stack
### Backend:
- FastAPI
- Requests
- Transformers (Hugging Face NLP models)
- Python-dotenv (for environment variables)
- Uvicorn (for ASGI server)

### Frontend:
- React (with functional components and hooks)
- Fetch API for communicating with FastAPI backend

## Installation and Setup
### Prerequisites
- Python 3.8+
- Node.js and npm
- Git

### Backend Setup
1. Navigate to the backend folder:
   ```sh
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the backend directory and add your News API key:
   ```sh
   NEWS_API_KEY=your_news_api_key_here
   ```
5. Run the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
6. The backend should now be running at:
   ```
   http://127.0.0.1:8000
   ```

### Frontend Setup
1. Navigate to the frontend folder:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend development server:
   ```sh
   npm start
   ```
4. The frontend should now be running at:
   ```
   http://localhost:3000
   ```

## API Endpoints
### `GET /news/?topic=<topic>`
Fetches recent news articles related to the provided topic and returns summarized results.

Example request:
```
http://127.0.0.1:8000/news/?topic=technology
```

Response format:
```json
{
  "news": [
    {
      "title": "Tech Advances in AI",
      "summary": "AI is making significant progress...",
      "url": "https://example.com/article1",
      "published_at": "2024-02-14T12:00:00Z"
    }
  ]
}
```

## Deployment
### Deploying Backend
You can deploy the FastAPI backend using **Render, Heroku, or Railway.app**. If using Docker, add a `Dockerfile`.

### Deploying Frontend
You can deploy the React frontend using **Vercel or Netlify**.

## Updating GitHub
To push changes to GitHub:
```sh
git add .
git commit -m "Updated project with improvements"
git push origin main
```

## Contributors
- **Your Name** - Developer

## License
This project is licensed under the MIT License.

