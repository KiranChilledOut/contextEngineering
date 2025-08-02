import logging
import json
import os
import glob
from datetime import datetime, date
import azure.functions as func
from typing import List, Dict, Optional

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    NewsAPI Function - Provides REST API endpoints for accessing generated news
    
    Endpoints:
    - GET /api/NewsAPI/today - Get all today's news
    - GET /api/NewsAPI/topic/{topic_name} - Get news for specific topic  
    - GET /api/NewsAPI/topics - Get list of available topics
    - GET /api/NewsAPI/latest/{days} - Get news from last N days
    """
    logging.info('NewsAPI function was triggered!')
    
    try:
        # Parse the route to determine which endpoint was called
        route_params = req.route_params
        method = req.method
        
        if method != 'GET':
            return create_error_response("Only GET method is supported", 405)
        
        # Get query parameters
        topic_name = route_params.get('topic_name')
        days = route_params.get('days', '1')
        
        # Route to appropriate handler
        if 'topics' in req.url:
            return handle_topics_list()
        elif topic_name:
            return handle_topic_news(topic_name)
        elif 'latest' in req.url:
            return handle_latest_news(int(days))
        else:  # Default to today's news
            return handle_today_news()
            
    except Exception as e:
        logging.error(f'Error in NewsAPI: {str(e)}')
        return create_error_response(f"Internal error: {str(e)}", 500)


def handle_today_news() -> func.HttpResponse:
    """Get all news for today."""
    try:
        today = date.today().strftime("%Y-%m-%d")
        news_data = get_news_for_date(today)
        
        if not news_data:
            return create_error_response(f"No news found for {today}", 404)
        
        response_data = {
            "status": "success",
            "date": today,
            "articles_count": len(news_data),
            "articles": news_data,
            "generated_at": datetime.now().isoformat()
        }
        
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
        
    except Exception as e:
        logging.error(f'Error getting today news: {str(e)}')
        return create_error_response("Failed to get today's news", 500)


def handle_topic_news(topic_name: str) -> func.HttpResponse:
    """Get news for a specific topic."""
    try:
        # Normalize topic name (handle URL encoding, spaces, etc.)
        topic_name_normalized = topic_name.lower().replace('-', ' ').replace('_', ' ')
        
        today = date.today().strftime("%Y-%m-%d")
        news_file = find_topic_file(topic_name_normalized, today)
        
        if not news_file:
            return create_error_response(f"No news found for topic: {topic_name}", 404)
        
        article_data = parse_news_file(news_file)
        if not article_data:
            return create_error_response("Failed to parse news file", 500)
        
        response_data = {
            "status": "success",
            "topic": topic_name,
            "date": today,
            "article": article_data,
            "generated_at": datetime.now().isoformat()
        }
        
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
        
    except Exception as e:
        logging.error(f'Error getting topic news for {topic_name}: {str(e)}')
        return create_error_response(f"Failed to get news for topic: {topic_name}", 500)


def handle_topics_list() -> func.HttpResponse:
    """Get list of available topics."""
    try:
        # Load topics from configuration
        topics_config = load_topics_config()
        if not topics_config:
            return create_error_response("Failed to load topics configuration", 500)
        
        topics_list = []
        for topic in topics_config["topics"]:
            if topic["enabled"]:
                topics_list.append({
                    "name": topic["name"],
                    "keywords": topic["keywords"],
                    "priority": topic["priority"],
                    "slug": topic["name"].lower().replace(' ', '-')
                })
        
        response_data = {
            "status": "success",
            "topics_count": len(topics_list),
            "topics": topics_list,
            "generated_at": datetime.now().isoformat()
        }
        
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
        
    except Exception as e:
        logging.error(f'Error getting topics list: {str(e)}')
        return create_error_response("Failed to get topics list", 500)


def handle_latest_news(days: int = 1) -> func.HttpResponse:
    """Get latest news from the last N days."""
    try:
        if days < 1 or days > 30:
            return create_error_response("Days parameter must be between 1 and 30", 400)
        
        all_news = []
        for i in range(days):
            target_date = date.today()
            if i > 0:
                from datetime import timedelta
                target_date = target_date - timedelta(days=i)
            
            date_str = target_date.strftime("%Y-%m-%d")
            news_data = get_news_for_date(date_str)
            if news_data:
                all_news.extend(news_data)
        
        # Sort by date descending
        all_news.sort(key=lambda x: x.get('date', ''), reverse=True)
        
        response_data = {
            "status": "success",
            "days_requested": days,
            "articles_count": len(all_news),
            "articles": all_news,
            "generated_at": datetime.now().isoformat()
        }
        
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
        
    except Exception as e:
        logging.error(f'Error getting latest news: {str(e)}')
        return create_error_response("Failed to get latest news", 500)


def get_news_for_date(date_str: str) -> List[Dict]:
    """Get all news articles for a specific date."""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Look in DailyNewsGenerator output directory
        output_dir = os.path.join(os.path.dirname(current_dir), 'DailyNewsGenerator', 'output')
        
        if not os.path.exists(output_dir):
            logging.warning(f'Output directory not found: {output_dir}')
            return []
        
        # Find all markdown files for the given date
        pattern = f"*-{date_str}.md"
        news_files = glob.glob(os.path.join(output_dir, pattern))
        
        news_data = []
        for file_path in news_files:
            article_data = parse_news_file(file_path)
            if article_data:
                news_data.append(article_data)
        
        return news_data
        
    except Exception as e:
        logging.error(f'Error getting news for date {date_str}: {str(e)}')
        return []


def find_topic_file(topic_name: str, date_str: str) -> Optional[str]:
    """Find the news file for a specific topic and date."""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(os.path.dirname(current_dir), 'DailyNewsGenerator', 'output')
        
        if not os.path.exists(output_dir):
            return None
        
        # Try different variations of the topic name
        topic_variations = [
            topic_name.lower().replace(' ', '-'),
            topic_name.lower().replace(' ', '_'),
            topic_name.lower()
        ]
        
        for variation in topic_variations:
            filename = f"{variation}-{date_str}.md"
            file_path = os.path.join(output_dir, filename)
            if os.path.exists(file_path):
                return file_path
        
        return None
        
    except Exception as e:
        logging.error(f'Error finding topic file for {topic_name}: {str(e)}')
        return None


def parse_news_file(file_path: str) -> Optional[Dict]:
    """Parse a markdown news file and extract metadata."""
    try:
        filename = os.path.basename(file_path)
        
        # Extract topic and date from filename
        parts = filename.replace('.md', '').split('-')
        if len(parts) >= 4:  # topic-YYYY-MM-DD format
            topic = '-'.join(parts[:-3]).replace('-', ' ').title()
            date_str = '-'.join(parts[-3:])
        else:
            topic = "Unknown"
            date_str = date.today().strftime("%Y-%m-%d")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic markdown parsing
        lines = content.split('\n')
        title = ""
        body = content
        
        # Extract title (first # heading)
        for line in lines:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                break
        
        # Get file stats
        stat = os.stat(file_path)
        
        return {
            "topic": topic,
            "title": title or f"{topic} - Daily News",
            "content": content,
            "date": date_str,
            "filename": filename,
            "word_count": len(content.split()),
            "file_size": stat.st_size,
            "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
        }
        
    except Exception as e:
        logging.error(f'Error parsing news file {file_path}: {str(e)}')
        return None


def load_topics_config():
    """Load topics configuration from DailyNewsGenerator."""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        topics_file = os.path.join(os.path.dirname(current_dir), 'DailyNewsGenerator', 'topics.json')
        
        with open(topics_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f'Failed to load topics.json: {str(e)}')
        return None


def create_error_response(message: str, status_code: int) -> func.HttpResponse:
    """Create an error HTTP response."""
    response_data = {
        "status": "error",
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    
    return func.HttpResponse(
        json.dumps(response_data, indent=2),
        status_code=status_code,
        mimetype="application/json",
        headers={"Access-Control-Allow-Origin": "*"}
    )