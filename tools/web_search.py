import requests
import os
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()  # Loads values from .env

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

from serpapi import GoogleSearch

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def web_search(query):
    if not SERPAPI_KEY:
        return "Web search API key not found.", None

    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    answer = results.get("answer_box", {}).get("snippet") or "No good answer found."
    source_url = results.get("organic_results", [{}])[0].get("link", "No URL")

    return answer, source_url
