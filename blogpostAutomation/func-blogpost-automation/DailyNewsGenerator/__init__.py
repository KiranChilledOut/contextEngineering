import logging
import json
import os
import requests
from datetime import datetime, date
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    DailyNewsGenerator Function - Generates daily news for all configured topics
    
    This function:
    1. Reads topics from topics.json
    2. Generates news for each enabled topic
    3. Creates individual .md files for each topic
    4. Creates a main.md summary file
    """
    logging.info('DailyNewsGenerator function was triggered!')
    
    try:
        # Step 1: Load topics configuration
        topics = load_topics_config()
        if not topics:
            return create_error_response("Failed to load topics configuration", 500)
        
        # Step 2: Get API key
        api_key = os.getenv('PERPLEXITY_API_KEY')
        if not api_key:
            return create_error_response("PERPLEXITY_API_KEY not found", 400)
        
        # Step 3: Generate news for all enabled topics
        today = date.today().strftime("%Y-%m-%d")
        news_results = []
        
        for topic in topics["topics"]:
            if topic["enabled"]:
                logging.info(f'Generating news for: {topic["name"]}')
                news_content = generate_topic_news(api_key, topic, today)
                if news_content:
                    news_results.append(news_content)
        
        # Step 4: Save individual topic files
        saved_files = save_topic_files(news_results)
        
        # Step 5: Create and save main summary
        main_summary = create_main_summary(news_results, today)
        main_file = save_main_summary(main_summary, today)
        
        # Step 6: Return results
        response_data = {
            "status": "success",
            "message": f"Generated daily news for {len(news_results)} topics",
            "date": today,
            "topics_processed": [result["topic"] for result in news_results],
            "main_summary_file": main_file,
            "individual_files": saved_files,
            "output_directory": "DailyNewsGenerator/output"
        }
        
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            mimetype="application/json"
        )
        
    except Exception as e:
        logging.error(f'Error in DailyNewsGenerator: {str(e)}')
        return create_error_response(f"Internal error: {str(e)}", 500)


def load_topics_config():
    """Load topics configuration from topics.json file."""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        topics_file = os.path.join(current_dir, 'topics.json')
        
        with open(topics_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f'Failed to load topics.json: {str(e)}')
        return None


def generate_topic_news(api_key: str, topic: dict, today: str) -> dict:
    """Generate news content for a specific topic."""
    try:
        keywords = ", ".join(topic["keywords"])
        prompt = f"""Find and summarize the most important news from the last 24 hours about: {topic['name']}

Focus on these keywords: {keywords}

Requirements:
- Only include news from the last 24 hours
- Provide 3-5 most significant stories
- Include brief summary for each story
- Mention sources when possible
- Use clear, engaging headlines
- Format as a news digest

Structure:
# {topic['name']} - Daily News Digest
## {today}

[News content here]
"""
        
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a news aggregator that finds and summarizes the latest news from the past 24 hours. Always include recent, factual information with sources when available."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 1000,
            "temperature": 0.3
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            
            return {
                "topic": topic["name"],
                "date": today,
                "content": content,
                "filename": f"{topic['name'].lower().replace(' ', '-')}-{today}.md",
                "word_count": len(content.split()),
                "generated_at": datetime.now().isoformat()
            }
        else:
            logging.error(f'API error for {topic["name"]}: {response.status_code}')
            return None
            
    except Exception as e:
        logging.error(f'Error generating news for {topic["name"]}: {str(e)}')
        return None


def create_main_summary(news_results: list, today: str) -> str:
    """Create a main summary file combining all topics."""
    try:
        summary = f"""# Daily News Digest
## {today}

*Your personalized news summary for today*

---

"""
        
        for news in news_results:
            summary += f"""## {news['topic']}

{news['content'][:300]}...

**[Read full {news['topic']} news]({news['filename']})**

---

"""
        
        summary += f"""
*Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Topics covered: {len(news_results)}*
"""
        
        return summary
        
    except Exception as e:
        logging.error(f'Error creating main summary: {str(e)}')
        return "Error creating summary"


def save_topic_files(news_results: list) -> list:
    """Save individual topic files to output directory."""
    saved_files = []
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_dir, 'output')
        
        for news in news_results:
            file_path = os.path.join(output_dir, news['filename'])
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(news['content'])
            
            saved_files.append({
                "topic": news['topic'],
                "filename": news['filename'],
                "file_path": file_path,
                "word_count": news['word_count']
            })
            logging.info(f'Saved: {news["filename"]}')
        
        return saved_files
        
    except Exception as e:
        logging.error(f'Error saving topic files: {str(e)}')
        return []


def save_main_summary(summary_content: str, today: str) -> str:
    """Save main summary file."""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_dir, 'output')
        main_file = f"main-{today}.md"
        file_path = os.path.join(output_dir, main_file)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        logging.info(f'Saved main summary: {main_file}')
        return main_file
        
    except Exception as e:
        logging.error(f'Error saving main summary: {str(e)}')
        return "Error saving main summary"


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
        mimetype="application/json"
    )