import logging
import json
import os
import requests
from datetime import datetime
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Simple test function to debug the Perplexity API call with one topic
    """
    logging.info('TestNews function started')
    
    try:
        # Step 1: Check API key
        api_key = os.getenv('PERPLEXITY_API_KEY')
        if not api_key:
            return func.HttpResponse(
                json.dumps({"error": "No API key found"}),
                status_code=400,
                mimetype="application/json"
            )
        
        logging.info(f'API key found, length: {len(api_key)}')
        
        # Step 2: Simple test with one topic
        topic = "AI Tools"
        logging.info(f'Testing with topic: {topic}')
        
        # Step 3: Make API call
        result = test_single_topic(api_key, topic)
        
        return func.HttpResponse(
            json.dumps(result, indent=2),
            status_code=200,
            mimetype="application/json"
        )
        
    except Exception as e:
        logging.error(f'Error in TestNews: {str(e)}')
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )


def test_single_topic(api_key: str, topic: str) -> dict:
    """Test Perplexity API call with a single topic"""
    try:
        logging.info('Starting API call to Perplexity')
        
        prompt = f"Find the latest news about {topic} from the last 24 hours. Keep it brief (200 words max)."
        
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 300,
            "temperature": 0.3
        }
        
        logging.info('Making request to Perplexity API...')
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        logging.info(f'Response status: {response.status_code}')
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            
            # Try to save to file
            filename = f"test-{topic.lower().replace(' ', '-')}.md"
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_dir, filename)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                file_saved = True
                logging.info(f'File saved: {file_path}')
            except Exception as save_error:
                file_saved = False
                logging.error(f'File save error: {str(save_error)}')
            
            return {
                "status": "success",
                "topic": topic,
                "content": content[:200] + "..." if len(content) > 200 else content,
                "full_content_length": len(content),
                "file_saved": file_saved,
                "filename": filename,
                "api_response_time": "success"
            }
        else:
            logging.error(f'API error: {response.status_code} - {response.text}')
            return {
                "status": "error",
                "api_status_code": response.status_code,
                "api_error": response.text
            }
            
    except requests.exceptions.Timeout:
        logging.error('API request timed out')
        return {"status": "error", "message": "API timeout"}
    except Exception as e:
        logging.error(f'API call error: {str(e)}')
        return {"status": "error", "message": str(e)}