import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    HelloWorld Function - Our learning example
    
    This function demonstrates:
    1. How to receive HTTP requests
    2. How to read query parameters 
    3. How to read request body
    4. How to return responses
    5. How to log information
    
    Args:
        req (func.HttpRequest): The incoming HTTP request
        
    Returns:
        func.HttpResponse: The response sent back to the user
    """
    logging.info('🎉 HelloWorld function was triggered\!')
    
    # Method 1: Get data from URL query string (?name=John)
    name = req.params.get('name')
    
    # Method 2: Get data from request body (for POST requests)
    try:
        req_body = req.get_json()
        if req_body and not name:
            name = req_body.get('name')
    except ValueError:
        # No JSON body, that's fine
        pass
    
    # Create our response message
    if name:
        message = f"Hello {name}\! 👋 This is your Azure Function working\!"
        status = "success"
    else:
        message = "Hello World\! 🌍 Try adding ?name=YourName or send JSON with 'name' field"
        status = "info"
    
    # Log some information (you'll see this in the console)
    logging.info(f'Request method: {req.method}')
    logging.info(f'Request URL: {req.url}')
    logging.info(f'Name parameter: {name}')
    
    # Return a JSON response
    response_data = {
        "status": status,
        "message": message,
        "request_info": {
            "method": req.method,
            "url": str(req.url),
            "headers_count": len(req.headers),
            "has_body": len(req.get_body()) > 0
        }
    }
    
    return func.HttpResponse(
        json.dumps(response_data, indent=2),
        status_code=200,
        mimetype="application/json"
    )