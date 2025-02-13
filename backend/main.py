from fastapi import FastAPI, Query
import requests
from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables (API keys)
load_dotenv()

app = FastAPI()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"

# Load NLP summarization model
summarizer = pipeline("summarization")

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
        summary = summarizer(article["description"][:512], max_length=50, min_length=10, do_sample=False)[0]["summary_text"]
        news_summaries.append({
            "title": article["title"],
            "summary": summary,
            "url": article["url"],
            "published_at": article["publishedAt"]
        })
    
    return {"news": news_summaries}