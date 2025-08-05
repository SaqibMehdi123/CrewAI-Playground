import os
import requests
from crewai.tools import BaseTool
from typing import Type, Optional, List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

class NewsAPIInput(BaseModel):
    query: str = Field(..., description="Search term for breaking news")

class NewsSearchTool(BaseTool):
    name: str = "search_news"
    description: str = "Searches news articles using NewsAPI for specific topics"
    args_schema: Type[BaseModel] = NewsAPIInput

    def _run(self, query: str) -> str:
        """Execute the news search for a specific topic"""
        try:
            if not query.strip():
                return "No search query provided."
            
            # Search for the specific query
            url = f"https://newsapi.org/v2/everything?q={query}&pageSize=10&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
            response = requests.get(url)
            data = response.json()
            articles = data.get("articles", [])
            
            if not articles:
                return f"No articles found for query: '{query}'"
            
            results = [f"🔍 NEWS SEARCH RESULTS FOR: '{query}'\n{'='*50}"]
            
            for i, article in enumerate(articles[:5], 1):  # Limit to top 5 articles
                title = article.get('title', 'No title')
                description = article.get('description', 'No description')
                source = article.get('source', {}).get('name', 'Unknown source')
                url_link = article.get('url', '')
                published = article.get('publishedAt', '')
                
                results.append(f"""
� Article {i}: {title}
📝 Description: {description}
📍 Source: {source}
🕒 Published: {published}
🔗 URL: {url_link}
""")
            
            return "\n".join(results)
            
        except Exception as e:
            return f"News API Error: {str(e)}"
