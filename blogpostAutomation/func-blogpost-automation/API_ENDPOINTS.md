# News API Endpoints Documentation

## Overview
The NewsAPI Azure Function provides REST API endpoints to access generated news data from the DailyNewsGenerator. This API is designed to be consumed by external applications like Django web apps.

## Base URL
```
https://your-function-app.azurewebsites.net/api/NewsAPI
```

## Available Endpoints

### 1. Get Today's News
**GET** `/api/NewsAPI/today`

Returns all news articles generated for today.

**Response:**
```json
{
  "status": "success",
  "date": "2025-08-01",
  "articles_count": 7,
  "articles": [
    {
      "topic": "AI Tools",
      "title": "AI Tools - Daily News Digest",
      "content": "# AI Tools - Daily News Digest\n## 2025-08-01\n\n...",
      "date": "2025-08-01",
      "filename": "ai-tools-2025-08-01.md",
      "word_count": 245,
      "file_size": 1234,
      "last_modified": "2025-08-01T10:30:00"
    }
  ],
  "generated_at": "2025-08-01T15:45:30"
}
```

### 2. Get News by Topic
**GET** `/api/NewsAPI/topic/{topic_name}`

Returns news for a specific topic. Topic names should be URL-encoded (spaces as %20 or hyphens).

**Examples:**
- `/api/NewsAPI/topic/ai-tools`
- `/api/NewsAPI/topic/AI%20Tools`
- `/api/NewsAPI/topic/economics`

**Response:**
```json
{
  "status": "success",
  "topic": "ai-tools",
  "date": "2025-08-01",
  "article": {
    "topic": "AI Tools",
    "title": "AI Tools - Daily News Digest",
    "content": "# AI Tools - Daily News Digest\n...",
    "date": "2025-08-01",
    "filename": "ai-tools-2025-08-01.md",
    "word_count": 245,
    "file_size": 1234,
    "last_modified": "2025-08-01T10:30:00"
  },
  "generated_at": "2025-08-01T15:45:30"
}
```

### 3. Get Available Topics
**GET** `/api/NewsAPI/topics`

Returns list of all available topics with their configuration.

**Response:**
```json
{
  "status": "success",
  "topics_count": 7,
  "topics": [
    {
      "name": "AI Tools",
      "keywords": ["AI tools", "ChatGPT", "Claude", "Copilot"],
      "priority": 1,
      "slug": "ai-tools"
    },
    {
      "name": "AI Innovations",
      "keywords": ["AI breakthrough", "artificial intelligence"],
      "priority": 2,
      "slug": "ai-innovations"
    }
  ],
  "generated_at": "2025-08-01T15:45:30"
}
```

### 4. Get Latest News (Multiple Days)
**GET** `/api/NewsAPI/latest/{days}`

Returns news from the last N days (1-30 days).

**Examples:**
- `/api/NewsAPI/latest/1` - Today only
- `/api/NewsAPI/latest/7` - Last 7 days
- `/api/NewsAPI/latest/30` - Last 30 days

**Response:**
```json
{
  "status": "success",
  "days_requested": 7,
  "articles_count": 49,
  "articles": [
    {
      "topic": "AI Tools",
      "title": "AI Tools - Daily News Digest",
      "content": "...",
      "date": "2025-08-01",
      "filename": "ai-tools-2025-08-01.md",
      "word_count": 245,
      "file_size": 1234,
      "last_modified": "2025-08-01T10:30:00"
    }
  ],
  "generated_at": "2025-08-01T15:45:30"
}
```

## Error Responses

All endpoints return standardized error responses:

```json
{
  "status": "error",
  "message": "Error description",
  "timestamp": "2025-08-01T15:45:30"
}
```

**Common HTTP Status Codes:**
- `200` - Success
- `400` - Bad Request (invalid parameters)
- `404` - Not Found (no news for specified date/topic)
- `405` - Method Not Allowed (only GET supported)
- `500` - Internal Server Error

## CORS Support
All endpoints include CORS headers to allow cross-origin requests from web applications.

## Django Integration Example

```python
import requests
from django.conf import settings

class NewsAPIClient:
    def __init__(self):
        self.base_url = settings.NEWS_API_BASE_URL
    
    def get_today_news(self):
        response = requests.get(f"{self.base_url}/today")
        return response.json() if response.status_code == 200 else None
    
    def get_topic_news(self, topic):
        response = requests.get(f"{self.base_url}/topic/{topic}")
        return response.json() if response.status_code == 200 else None
    
    def get_topics(self):
        response = requests.get(f"{self.base_url}/topics")
        return response.json() if response.status_code == 200 else None
```

## Rate Limiting
Azure Functions have built-in rate limiting. For high-traffic applications, consider implementing caching in your Django app.

## Authentication
Currently set to `anonymous` for easy integration. In production, consider adding API key authentication.