---
name: "Multi-Agent Research & Email System PRP"
description: "Comprehensive PRP for building a Pydantic AI multi-agent system with Research Agent and Email Draft Agent, supporting CLI interaction and multiple LLM providers"
---

## Goal

Build a sophisticated multi-agent Pydantic AI system that combines research capabilities with email drafting. The primary agent will be a Research Agent that can search the web using Brave Search API and invoke an Email Draft Agent to create professional email drafts via Gmail API. The system should support multiple LLM providers (OpenAI, Claude, DeepSeek) and provide an interactive CLI interface with real-time streaming and tool call visibility.

## Why

- **Business Value**: Automates research-to-communication workflow, saving time on information gathering and professional correspondence
- **Integration Benefits**: Demonstrates multi-agent architecture with proper dependency injection and tool composition
- **Production Ready**: Includes proper authentication, error handling, testing, and configuration management
- **Developer Experience**: Provides clear patterns for building complex Pydantic AI applications with external API integrations

## What

### User-Visible Behavior
- Interactive CLI that accepts natural language research requests
- Real-time streaming of agent responses with tool execution visibility
- Automatic web search using Brave Search API for current information
- Professional email draft creation through Gmail API integration
- Support for multiple LLM providers with easy switching via environment variables

### Technical Requirements
- Multi-agent architecture with clear separation of concerns
- Type-safe implementation using Pydantic AI patterns
- OAuth2 authentication for Gmail API integration
- API key management for Brave Search and LLM providers
- Comprehensive error handling and retry mechanisms
- Production-ready logging and monitoring capabilities

### Success Criteria
- [ ] Research Agent successfully searches web and synthesizes information
- [ ] Email Draft Agent creates professional emails via Gmail API
- [ ] CLI provides smooth interactive experience with streaming responses
- [ ] Multi-provider LLM support works with proper fallbacks
- [ ] All API integrations handle authentication and rate limiting
- [ ] Comprehensive test coverage with TestModel and FunctionModel
- [ ] Complete setup documentation with .env.example and README

## All Needed Context

### Documentation & References

```yaml
# MUST READ - Pydantic AI Framework Documentation
- url: https://ai.pydantic.dev/
  why: Official PydanticAI documentation with agent creation patterns
  critical: Agent initialization, model providers, dependency injection

- url: https://ai.pydantic.dev/agents/
  why: Comprehensive agent architecture and configuration patterns  
  critical: System prompts, output types, execution methods, multi-agent composition

- url: https://ai.pydantic.dev/tools/
  why: Tool integration patterns and function registration
  critical: @agent.tool decorators, RunContext usage, parameter validation

- url: https://ai.pydantic.dev/testing/
  why: Testing strategies specific to PydanticAI agents
  critical: TestModel, FunctionModel, Agent.override(), pytest patterns

- url: https://ai.pydantic.dev/models/
  why: Model provider configuration and authentication
  critical: OpenAI, Anthropic, custom provider setup, API key management

# MUST READ - Gmail API 2024 Integration
- url: https://developers.google.com/gmail/api/quickstart/python
  why: Official Gmail API Python setup with OAuth2 authentication
  critical: credentials.json setup, token.json management, draft creation

- url: https://developers.google.com/gmail/api/auth/web-server
  why: Server-side OAuth2 implementation patterns
  critical: Scope management, refresh token handling, security best practices

# MUST READ - Brave Search API Integration  
- url: https://brave.com/search/api/
  why: Official Brave Search API documentation and endpoints
  critical: Authentication headers, query parameters, response structure

- url: https://api-dashboard.search.brave.com/app/documentation/summarizer-search/code-samples
  why: Python code examples and implementation patterns
  critical: Request formatting, error handling, rate limiting

# ESSENTIAL CODEBASE PATTERNS - Use as Reference Implementation
- file: /Users/kiran/Desktop/git/personal/contextEngineering/use-cases/pydantic-ai/examples/main_agent_reference/cli.py
  why: Complete CLI implementation with streaming and tool visibility
  critical: Agent interaction patterns, conversation history, error handling

- file: /Users/kiran/Desktop/git/personal/contextEngineering/use-cases/pydantic-ai/examples/main_agent_reference/research_agent.py
  why: Multi-agent composition with tool integration
  critical: Agent dependency injection, tool definitions, sub-agent invocation

- file: /Users/kiran/Desktop/git/personal/contextEngineering/use-cases/pydantic-ai/examples/main_agent_reference/settings.py
  why: Environment-based configuration with pydantic-settings
  critical: API key validation, model configuration, environment variables

- file: /Users/kiran/Desktop/git/personal/contextEngineering/use-cases/pydantic-ai/examples/main_agent_reference/providers.py
  why: Model provider abstraction with get_llm_model()
  critical: Multi-provider support, configuration patterns, fallback strategies

- file: /Users/kiran/Desktop/git/personal/contextEngineering/use-cases/pydantic-ai/examples/main_agent_reference/tools.py
  why: Pure tool function patterns for multi-agent systems
  critical: Tool isolation, error handling, async patterns

# PROJECT RULES AND CONSTRAINTS
- docfile: /Users/kiran/Desktop/git/personal/contextEngineering/CLAUDE.md
  why: Global project rules for code structure, testing, and conventions
  critical: File size limits, testing requirements, documentation standards
```

### Current Codebase Tree
```bash
contextEngineering/
├── .claude/
├── CLAUDE.md                    # Global AI assistant rules
├── PLANNING.md                  # Project architecture
├── INITIAL.md                   # Feature requirements
├── PRPs/
│   └── templates/
│       └── prp_base.md         # PRP template
├── examples/                    # Currently empty 
├── use-cases/
│   └── pydantic-ai/
│       └── examples/
│           └── main_agent_reference/  # Critical reference patterns
│               ├── cli.py
│               ├── research_agent.py
│               ├── settings.py
│               ├── providers.py
│               └── tools.py
└── README.md
```

### Desired Codebase Tree with New Files
```bash
contextEngineering/
├── venv_linux/                  # Virtual environment (to be created)
├── src/
│   ├── __init__.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── research_agent.py    # Primary agent with web search and email invocation
│   │   ├── email_agent.py       # Gmail draft creation agent
│   │   └── dependencies.py     # Dependency injection classes
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── brave_search.py      # Brave Search API integration
│   │   └── gmail_tools.py       # Gmail API integration
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py           # Pydantic models for structured outputs
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py          # Environment-based configuration
│   │   └── providers.py         # LLM provider management
│   └── cli.py                   # Interactive CLI with streaming
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest configuration and fixtures
│   ├── test_agents.py          # Agent testing with TestModel
│   ├── test_tools.py           # Tool testing with mocks
│   └── test_integration.py     # End-to-end integration tests
├── .env.example                # Environment variable template
├── requirements.txt            # Python dependencies
├── pytest.ini                 # Test configuration
└── README.md                   # Complete setup and usage guide
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: Pydantic AI requires specific model string formats
# Use get_llm_model() from providers.py, NEVER hardcode "openai:gpt-4o"
model = get_llm_model()  # Correct
model = "openai:gpt-4o"  # WRONG - breaks provider abstraction

# CRITICAL: Gmail API OAuth2 requires specific scopes in 2024
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']  # Draft creation
# Using broader scopes like 'gmail.readonly' won't allow draft creation

# CRITICAL: Brave Search API rate limiting
# Free tier: 2000 queries/month, paid plans start at $3/1000 queries
# Always implement retry logic with exponential backoff

# CRITICAL: Pydantic AI tool functions must use RunContext for dependency access
@agent.tool
async def search_web(ctx: RunContext[DepsType], query: str):  # Correct
    api_key = ctx.deps.brave_api_key  # Access through context

# CRITICAL: Environment variables must be validated with pydantic-settings
class Settings(BaseSettings):
    brave_api_key: str = Field(...)  # Required field validation
    
    @field_validator("brave_api_key")
    @classmethod
    def validate_api_key(cls, v):
        if not v or v.strip() == "":
            raise ValueError("API key cannot be empty")
        return v

# CRITICAL: Agent-to-agent communication requires proper usage passing
result = await email_agent.run(
    prompt,
    deps=email_deps,
    usage=ctx.usage  # MUST pass usage for token tracking
)

# CRITICAL: Async patterns in CLI - all agent interactions must be awaited
async def main():
    result = await agent.run(prompt, deps=deps)  # Correct
    # result = agent.run_sync(prompt, deps=deps)  # Use sparingly, blocks
```

## Implementation Blueprint

### Data Models and Structure

Create type-safe data models ensuring consistency across agent interactions:

```python
# src/models/schemas.py
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime

class SearchResult(BaseModel):
    """Structured search result from Brave API"""
    title: str
    url: str  
    description: str
    score: float = Field(ge=0.0, le=1.0)

class EmailDraftRequest(BaseModel):
    """Request model for email draft creation"""
    recipient_email: str = Field(..., regex=r'^[^@]+@[^@]+\.[^@]+$')
    subject: str = Field(..., min_length=1, max_length=200)
    context: str = Field(..., min_length=10)
    research_summary: Optional[str] = None

class ResearchSummary(BaseModel):
    """Structured research output"""
    topic: str
    key_findings: List[str]
    sources: List[str]
    confidence_score: float = Field(ge=0.0, le=1.0)
    timestamp: datetime = Field(default_factory=datetime.now)
```

### Task Implementation Order

```yaml
Task 1 - Environment Setup:
  CREATE virtual environment and dependencies:
    - python -m venv venv_linux
    - Install: pydantic-ai, pydantic-settings, google-api-python-client, google-auth, httpx, rich, pytest
    - CREATE requirements.txt with pinned versions
    - CREATE .env.example with all required environment variables

Task 2 - Configuration Layer:
  CREATE src/config/settings.py:
    - MIRROR pattern from: use-cases/pydantic-ai/examples/main_agent_reference/settings.py
    - ADD Gmail-specific configuration (credentials_path, token_path)
    - ADD Brave Search configuration (api_key, base_url)
    - ADD multi-provider LLM configuration (OpenAI, Claude, DeepSeek)
    - IMPLEMENT field validators for all API keys

  CREATE src/config/providers.py:
    - MIRROR pattern from: use-cases/pydantic-ai/examples/main_agent_reference/providers.py
    - EXTEND get_llm_model() to support Claude and DeepSeek providers
    - ADD provider validation and fallback mechanisms
    - IMPLEMENT model information and configuration utilities

Task 3 - Data Models:
  CREATE src/models/schemas.py:
    - IMPLEMENT SearchResult, EmailDraftRequest, ResearchSummary models
    - ADD comprehensive validators for email addresses, URLs, text lengths
    - INCLUDE timestamp and metadata fields for tracking
    - ENSURE type safety for all agent interactions

Task 4 - Tool Layer Implementation:
  CREATE src/tools/brave_search.py:
    - MIRROR pattern from: use-cases/pydantic-ai/examples/main_agent_reference/tools.py
    - IMPLEMENT async search_web_tool() with proper error handling
    - ADD rate limiting and retry logic with exponential backoff
    - INCLUDE response parsing and result scoring

  CREATE src/tools/gmail_tools.py:
    - IMPLEMENT Gmail OAuth2 authentication flow
    - CREATE gmail_authenticate() function with token refresh
    - ADD create_draft_email() function with proper scopes
    - INCLUDE comprehensive error handling for API failures

Task 5 - Agent Implementation:
  CREATE src/agents/dependencies.py:
    - DEFINE ResearchAgentDependencies dataclass
    - DEFINE EmailAgentDependencies dataclass  
    - INCLUDE session management and authentication state

  CREATE src/agents/email_agent.py:
    - IMPLEMENT standalone email draft creation agent
    - USE get_llm_model() for provider configuration
    - ADD @agent.tool for Gmail draft creation
    - INCLUDE professional email formatting and validation

  CREATE src/agents/research_agent.py:
    - MIRROR pattern from: use-cases/pydantic-ai/examples/main_agent_reference/research_agent.py
    - IMPLEMENT web search tool integration
    - ADD email agent invocation capability
    - INCLUDE research summarization and synthesis tools
    - ENSURE proper usage tracking across agent calls

Task 6 - CLI Implementation:
  CREATE src/cli.py:
    - MIRROR pattern from: use-cases/pydantic-ai/examples/main_agent_reference/cli.py
    - IMPLEMENT streaming responses with tool call visibility
    - ADD conversation history management
    - INCLUDE graceful error handling and user feedback
    - ENSURE proper async/await patterns throughout

Task 7 - Testing Infrastructure:
  CREATE tests/conftest.py:
    - SETUP pytest fixtures for agent testing
    - IMPLEMENT mock dependencies for external APIs
    - ADD TestModel and FunctionModel configurations
    - INCLUDE test data factories and utilities

  CREATE tests/test_agents.py:
    - TEST agent instantiation and basic functionality
    - USE TestModel for rapid validation without API costs
    - TEST multi-agent communication and usage tracking
    - INCLUDE edge cases and error scenarios

  CREATE tests/test_tools.py:
    - TEST tool functions with proper mocking
    - VALIDATE API authentication and request formatting
    - TEST error handling and retry mechanisms
    - INCLUDE rate limiting and timeout scenarios

  CREATE tests/test_integration.py:
    - TEST complete workflow from CLI to agent execution
    - INCLUDE end-to-end scenarios with mocked external APIs
    - TEST multi-provider fallback mechanisms
    - VALIDATE configuration and environment variable handling

Task 8 - Documentation and Setup:
  CREATE .env.example:
    - INCLUDE all required environment variables with descriptions
    - ADD setup instructions for Gmail and Brave API credentials
    - PROVIDE example values for development and testing

  UPDATE README.md:
    - INCLUDE comprehensive setup instructions
    - ADD Gmail OAuth2 configuration guide
    - DOCUMENT Brave Search API setup process
    - PROVIDE usage examples and troubleshooting guide
    - INCLUDE project structure and architecture overview
```

### Per Task Pseudocode

```python
# Task 4 - Brave Search Tool Implementation
async def search_web_tool(
    api_key: str,
    query: str,
    count: int = 10
) -> List[Dict[str, Any]]:
    """Pure function for Brave Search API integration"""
    
    # PATTERN: Validate inputs first (see existing tools.py)
    if not api_key or not query.strip():
        raise ValueError("API key and query are required")
    
    # GOTCHA: Brave API requires specific headers
    headers = {
        "X-Subscription-Token": api_key,
        "Accept": "application/json"
    }
    
    # PATTERN: Use httpx for async requests with timeout
    async with httpx.AsyncClient() as client:
        # CRITICAL: Handle rate limiting (429 status)
        @retry(attempts=3, backoff=exponential)
        async def _search():
            response = await client.get(
                "https://api.search.brave.com/res/v1/web/search",
                headers=headers,
                params={"q": query, "count": min(count, 20)},
                timeout=30.0
            )
            
            if response.status_code == 429:
                raise RateLimitError("Rate limit exceeded")
            elif response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            
            response.raise_for_status()
            return response.json()
        
        data = await _search()
    
    # PATTERN: Parse and score results consistently
    results = []
    for idx, result in enumerate(data.get("web", {}).get("results", [])):
        score = 1.0 - (idx * 0.05)  # Position-based scoring
        results.append({
            "title": result.get("title", ""),
            "url": result.get("url", ""),
            "description": result.get("description", ""),
            "score": max(score, 0.1)
        })
    
    return results

# Task 5 - Research Agent with Sub-Agent Invocation
@research_agent.tool
async def create_email_draft(
    ctx: RunContext[ResearchAgentDependencies],
    recipient_email: str,
    subject: str,
    context: str,
    research_summary: Optional[str] = None
) -> Dict[str, Any]:
    """Invoke Email Agent to create Gmail draft"""
    
    # PATTERN: Validate input with Pydantic model
    request = EmailDraftRequest(
        recipient_email=recipient_email,
        subject=subject,
        context=context,
        research_summary=research_summary
    )
    
    # CRITICAL: Create email agent dependencies
    email_deps = EmailAgentDependencies(
        gmail_credentials_path=ctx.deps.gmail_credentials_path,
        gmail_token_path=ctx.deps.gmail_token_path
    )
    
    # CRITICAL: Pass usage for token tracking across agents
    result = await email_agent.run(
        f"Create professional email draft: {request.json()}",
        deps=email_deps,
        usage=ctx.usage  # Essential for multi-agent token tracking
    )
    
    return {
        "success": True,
        "draft_created": True,
        "agent_response": result.data,
        "recipient": recipient_email
    }
```

### Integration Points

```yaml
ENVIRONMENT_VARIABLES:
  - add to: .env.example
  - required: |
    # LLM Provider Configuration
    LLM_PROVIDER=openai
    LLM_API_KEY=your_openai_api_key_here
    LLM_MODEL=gpt-4
    LLM_BASE_URL=https://api.openai.com/v1
    
    # Brave Search Configuration  
    BRAVE_API_KEY=your_brave_api_key_here
    BRAVE_SEARCH_URL=https://api.search.brave.com/res/v1/web/search
    
    # Gmail Configuration
    GMAIL_CREDENTIALS_PATH=credentials.json
    GMAIL_TOKEN_PATH=token.json
    
    # Application Configuration
    APP_ENV=development
    LOG_LEVEL=INFO
    DEBUG=false

DEPENDENCIES:
  - add to: requirements.txt
  - packages: |
    pydantic-ai>=0.0.16
    pydantic>=2.0.0
    pydantic-settings>=2.0.0
    google-api-python-client>=2.0.0
    google-auth-httplib2>=0.2.0
    google-auth-oauthlib>=1.0.0
    httpx>=0.25.0
    rich>=13.0.0
    python-dotenv>=1.0.0
    pytest>=7.0.0
    pytest-asyncio>=0.21.0

CLI_ENTRY_POINT:
  - pattern: "python -m src.cli"
  - alternative: "Add to pyproject.toml as console script"
```

## Validation Loop

### Level 1: Environment & Dependencies
```bash
# Virtual environment setup and activation
python -m venv venv_linux
source venv_linux/bin/activate  # Linux/Mac
# venv_linux\Scripts\activate  # Windows

# Install dependencies and verify
pip install -r requirements.txt
python -c "import pydantic_ai; print('Pydantic AI installed successfully')"
python -c "from google.auth.transport.requests import Request; print('Gmail API libraries installed')"
python -c "import httpx; print('HTTP client installed')"

# Expected: All imports succeed without errors
# If failing: Check Python version compatibility, resolve dependency conflicts
```

### Level 2: Configuration Validation
```bash
# Test configuration loading
python -c "
from src.config.settings import settings
print(f'LLM Provider: {settings.llm_provider}')
print(f'Model: {settings.llm_model}')
print('Configuration loaded successfully')
"

# Test provider configuration
python -c "
from src.config.providers import get_llm_model, validate_llm_configuration
model = get_llm_model()
print(f'Model instance: {model}')
print(f'Config valid: {validate_llm_configuration()}')
"

# Expected: Configuration loads without validation errors
# If failing: Check .env file setup, fix API key validation issues
```

### Level 3: Agent Instantiation & Tool Registration
```bash
# Test agent creation with TestModel
python -c "
from pydantic_ai.models.test import TestModel
from src.agents.research_agent import research_agent
from src.agents.email_agent import email_agent

print(f'Research agent tools: {len(research_agent.tools)}')
print(f'Email agent tools: {len(email_agent.tools)}')

# Test with TestModel to avoid API costs
test_model = TestModel()
with research_agent.override(model=test_model):
    print('Research agent override successful')
    
with email_agent.override(model=test_model):
    print('Email agent override successful')
"

# Expected: Agents instantiate successfully, tools registered, TestModel works
# If failing: Check agent definitions, tool decorators, dependency injection
```

### Level 4: Tool Integration Testing
```bash
# Run tool-specific tests with mocks
python -m pytest tests/test_tools.py -v

# Test specific tool functions
python -c "
import asyncio
from src.tools.brave_search import search_web_tool

async def test_search():
    # This would use mock in real test
    print('Search tool import successful')
    
asyncio.run(test_search())
"

# Test Gmail authentication setup (without actual API calls)
python -c "
from src.tools.gmail_tools import gmail_authenticate
print('Gmail tool import successful')
# Note: Actual auth test requires credentials.json
"

# Expected: All tool imports succeed, mock tests pass
# If failing: Fix import issues, resolve async/sync patterns
```

### Level 5: End-to-End Integration Test
```bash
# Run comprehensive test suite
python -m pytest tests/ -v --tb=short

# Test CLI functionality (with TestModel)
python -c "
import asyncio
from src.cli import stream_agent_interaction

async def test_cli():
    # Mock conversation history
    history = []
    try:
        # This would use TestModel in real test
        print('CLI import and basic structure test passed')
    except Exception as e:
        print(f'CLI test failed: {e}')

asyncio.run(test_cli())
"

# Expected: All tests pass, CLI structure validates
# If failing: Fix integration issues, resolve async patterns, check error handling
```

### Level 6: Manual CLI Testing
```bash
# Start interactive CLI for manual testing
source venv_linux/bin/activate
python -m src.cli

# Test basic interaction:
# User: "Hello, can you help me research Python best practices?"
# Expected: Agent responds, may show tool calls if search triggered

# Test email functionality:
# User: "Create an email draft about Python best practices for john@example.com"
# Expected: Research agent searches, then invokes email agent

# Test error handling:
# User: "Invalid request $$###"
# Expected: Graceful error handling, helpful error messages
```

## Final Validation Checklist

### Core Functionality
- [ ] Multi-agent system works: Research Agent + Email Agent communication
- [ ] Brave Search API integration: Web search with proper authentication
- [ ] Gmail API integration: OAuth2 flow and draft creation
- [ ] Multi-provider LLM support: OpenAI, Claude, DeepSeek with fallbacks
- [ ] CLI interface: Streaming responses with tool call visibility
- [ ] Environment configuration: Secure API key management

### Code Quality & Testing  
- [ ] All tests pass: `python -m pytest tests/ -v`
- [ ] Type checking passes: `mypy src/` (if using mypy)
- [ ] Code follows CLAUDE.md rules: File size limits, modularity, documentation
- [ ] Comprehensive test coverage: Agent, tool, integration tests
- [ ] Error handling robust: API failures, network issues, authentication errors

### Production Readiness
- [ ] Security patterns implemented: No hardcoded credentials, input validation
- [ ] Documentation complete: README with setup guide, .env.example provided
- [ ] Rate limiting handled: Brave API quotas respected, retry logic implemented
- [ ] Logging configured: Informative logs without exposing sensitive data
- [ ] Dependency management: requirements.txt with pinned versions

### User Experience
- [ ] Setup process smooth: Clear instructions for Gmail and Brave API setup
- [ ] CLI intuitive: Natural language interaction, helpful error messages
- [ ] Performance acceptable: Reasonable response times, streaming provides feedback
- [ ] Multi-provider switching: Easy environment variable configuration
- [ ] Error recovery graceful: Network issues don't crash application

---

## Anti-Patterns to Avoid

### Pydantic AI Specific
- ❌ Don't hardcode model strings - always use get_llm_model() from providers.py
- ❌ Don't skip TestModel validation - test agents without API costs during development
- ❌ Don't ignore RunContext - tools must access dependencies through ctx.deps
- ❌ Don't forget usage tracking - pass ctx.usage when invoking sub-agents
- ❌ Don't mix sync/async patterns - be consistent with async agent calls

### API Integration
- ❌ Don't ignore rate limiting - implement proper backoff for Brave Search API
- ❌ Don't hardcode API credentials - use environment variables with validation
- ❌ Don't skip OAuth2 refresh - handle Gmail token expiration gracefully
- ❌ Don't ignore API quotas - monitor usage and provide clear error messages
- ❌ Don't skip error handling - external API failures should not crash agents

### Architecture & Security
- ❌ Don't create monolithic files - follow 500-line limit from CLAUDE.md rules
- ❌ Don't skip input validation - sanitize all user inputs with Pydantic models  
- ❌ Don't expose secrets in logs - implement secure logging practices
- ❌ Don't skip dependency injection - use dataclasses for agent dependencies
- ❌ Don't ignore testing requirements - implement comprehensive test coverage

**CONFIDENCE SCORE: 9/10** - This PRP provides comprehensive context, proven patterns from existing codebase, detailed implementation tasks, and robust validation loops. The AI agent should be able to implement this successfully in one pass with the extensive documentation, reference implementations, and executable validation gates provided.