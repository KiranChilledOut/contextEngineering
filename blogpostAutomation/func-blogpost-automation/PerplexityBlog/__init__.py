import logging
import json
import os
import requests
from datetime import datetime
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    PerplexityBlog Function - Step 2: Reading user input
    
    Now we'll learn how to get data FROM the user request.
    """
    logging.info('🤖 PerplexityBlog function was triggered!')
    print("DEBUG: PerplexityBlog function started")  # This will show in console
    
    # Step 1: Try to get topic from URL query parameter (?topic=AI)
    topic = req.params.get('topic')
    logging.info(f'Topic from query params: {topic}')
    
    # Step 2: If no query param, try to get from JSON body
    if not topic:
        try:
            req_body = req.get_json()
            if req_body:
                topic = req_body.get('topic')
                logging.info(f'Topic from JSON body: {topic}')
        except ValueError:
            logging.info('No JSON body found or invalid JSON')
    
    # Step 3: Use default if still no topic
    if not topic:
        topic = "software development trends"
        logging.info(f'Using default topic: {topic}')
    
    # Step 4: Check for API key in environment variables
    api_key = os.getenv('PERPLEXITY_API_KEY')
    if not api_key:
        # No API key found - return error
        response_data = {
            "status": "error",
            "message": "PERPLEXITY_API_KEY not found in environment variables",
            "hint": "Add your API key to Azure Function App settings"
        }
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=400,
            mimetype="application/json"
        )
    
    # Step 5: Make actual Perplexity API call
    logging.info(f'🌐 Calling Perplexity API for topic: {topic}')
    blog_content = call_perplexity_api(api_key, topic)
    
    if blog_content:
        # Success - return the generated content
        response_data = {
            "status": "success",
            "message": "Blog content generated successfully!",
            "data": blog_content
        }
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            mimetype="application/json"
        )
    else:
        # API call failed
        response_data = {
            "status": "error",
            "message": "Failed to generate blog content",
            "topic": topic
        }
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=500,
            mimetype="application/json"
        )
    

def call_perplexity_api(api_key: str, topic: str) -> dict:
    """
    Call Perplexity AI API to generate blog content.
    
    This function demonstrates:
    1. HTTP POST requests with authentication
    2. JSON payload construction  
    3. Error handling for network issues
    4. Response processing
    
    Args:
        api_key (str): Perplexity API key
        topic (str): Blog topic to write about
        
    Returns:
        dict: Generated blog content or None if failed
    """
    try:
        # Perplexity API endpoint
        url = "https://api.perplexity.ai/chat/completions"
        
        # Create the prompt
        prompt = f"""Write a professional blog post about: {topic}

Requirements:
- 400-600 words
- Include practical examples
- Add actionable insights  
- Use engaging tone for developers
- Include a compelling title
- Structure with clear sections

Format the response as a blog post with title and content."""
        
        # API request headers (authentication)
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # API request payload (what we send to Perplexity)
        payload = {
            "model": "sonar",
            "messages": [
                {
                    "role": "system", 
                    "content": "You are a technical blogger who writes engaging, informative content for software developers."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            "max_tokens": 800,
            "temperature": 0.7
        }
        
        logging.info('📡 Making HTTP request to Perplexity API...')
        
        # Make the API call with 30-second timeout
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        
        # Check if request was successful (HTTP 200)
        if response.status_code == 200:
            logging.info('Response received with code 200')
            result = response.json()
            content = result['choices'][0]['message']['content']
            
            # Extract title from content (first line usually)
            lines = content.split('\n')
            title = lines[0].replace('#', '').strip() if lines else f"Insights on {topic}"
            
            # Return structured blog content
            blog_data = {
                'title': title,
                'content': content,
                'topic': topic,
                'generated_at': datetime.now().isoformat(),
                'word_count': len(content.split()),
                'model_used': 'llama-3.1-sonar-small-128k-online'
            }
            
            logging.info(f'✅ Blog generated! Word count: {blog_data["word_count"]}')
            return blog_data
            
        else:
            logging.error(f'❌ Perplexity API error: {response.status_code} - {response.text}')
            return None
            
    except requests.exceptions.Timeout:
        logging.error('❌ Perplexity API request timed out (30 seconds)')
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f'❌ Network error: {str(e)}')
        return None
    except Exception as e:
        logging.error(f'❌ Unexpected error: {str(e)}')
        return None