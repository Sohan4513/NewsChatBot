import logging
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
from transformers import pipeline
from dotenv import load_dotenv
import os

# Suppress warnings from the transformers library
logging.getLogger("transformers").setLevel(logging.ERROR)

# Load environment variables (API keys)
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"

# Load NLP summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Use a better model

@app.get("/news/")
def get_news(topic: str = Query(..., title="Topic", description="Enter a topic of interest")):
    """
    Fetch recent news articles based on user interest and summarize them.
    """
    params = {
        "q": topic,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5  # Limit the number of articles
    }
    
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    
    if "articles" not in data:
        return {"error": "No news articles found or API limit reached."}
    
    news_summaries = []
    for article in data["articles"]:
        description = article.get("description", "")
        
        # Skip if description is empty
        if not description:
            news_summaries.append({
                "title": article["title"],
                "summary": "No description available.",
                "url": article["url"],
                "published_at": article["publishedAt"]
            })
            continue
        
        # Summarize the description
        try:
            summary = summarizer(
                description[:512],  # Truncate input to 512 tokens
                max_length=100,     # Increase max_length for longer summaries
                min_length=30,       # Increase min_length to avoid very short summaries
                do_sample=False
            )[0]["summary_text"]
        except Exception as e:
            summary = description  # Fallback to the original description if summarization fails
        
        news_summaries.append({
            "title": article["title"],
            "summary": summary,
            "url": article["url"],
            "published_at": article["publishedAt"]
        })
    
    return {"news": news_summaries}