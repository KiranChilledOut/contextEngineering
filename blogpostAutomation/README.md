# Blog Post Automation System

Automated blog post generation system using Azure Functions, Perplexity AI, and Telegram approval workflow.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Azure CLI
- Terraform
- Git
- Azure Subscription

### 1. Environment Setup

```bash
# Clone and setup
git clone <repository-url>
cd blogpostAutomation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Copy environment template:
```bash
cp .env.example .env
```

Configure your `.env` file:
```bash
# Perplexity AI
PERPLEXITY_API_KEY=your_perplexity_api_key

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id

# Git Repository
GIT_REPO_URL=https://github.com/yourusername/blog-content.git
GIT_ACCESS_TOKEN=your_github_token
GIT_BRANCH=main

# Azure (set after infrastructure deployment)
AZURE_KEYVAULT_URL=https://your-keyvault.vault.azure.net/
```

### 3. Infrastructure Deployment

```bash
# Initialize Terraform
cd terraform
terraform init

# Plan deployment
terraform plan

# Deploy infrastructure
terraform apply
```

### 4. Deploy Function App

```bash
# Login to Azure
az login

# Deploy function
func azure functionapp publish <your-function-app-name>
```

## 📁 Project Structure

```
blogpostAutomation/
├── .azure/                      # Azure Pipelines
│   └── azure-pipelines.yml
├── .claude/                     # Claude AI instructions
│   └── claude_docs.md
├── .vscode/                     # VS Code settings
│   └── settings.json
├── src/                         # Source code
│   ├── agents/                  # AI agents
│   │   ├── content_agent.py     # Perplexity integration
│   │   ├── approval_agent.py    # Telegram workflow
│   │   └── git_agent.py         # Git operations
│   ├── tools/                   # Utility modules
│   │   ├── perplexity_client.py # Perplexity API wrapper
│   │   ├── telegram_client.py   # Telegram bot client
│   │   └── git_operations.py    # Git command utilities
│   ├── models/                  # Data models
│   │   ├── blog_post.py         # Blog post schema
│   │   └── approval_state.py    # Workflow state
│   └── main.py                  # Azure Function entry point
├── terraform/                   # Infrastructure as Code
│   ├── main.tf                  # Main configuration
│   ├── functions.tf             # Function App setup
│   ├── keyvault.tf             # Key Vault configuration
│   └── variables.tf             # Terraform variables
├── tests/                       # Test files
│   ├── test_agents.py
│   ├── test_tools.py
│   └── test_models.py
├── scripts/                     # Utility scripts
│   ├── setup.py                # Setup automation
│   └── deploy.py               # Deployment helper
├── requirements.txt             # Python dependencies
├── host.json                   # Azure Functions config
├── local.settings.json.example # Local development config
├── .env.example                # Environment template
├── .gitignore
├── INITIAL.md                  # Feature specification
├── PLANNING.md                 # Architecture documentation
└── README.md                   # This file
```

## 🔧 Setup Instructions

### Perplexity AI Setup

1. Visit [Perplexity AI](https://docs.perplexity.ai/)
2. Create an account and get API key
3. Add key to `.env` as `PERPLEXITY_API_KEY`

### Telegram Bot Setup

1. Create bot via [@BotFather](https://t.me/botfather)
2. Get bot token and add to `.env` as `TELEGRAM_BOT_TOKEN`
3. Get your chat ID:
   ```bash
   # Send message to your bot, then:
   curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
4. Add chat ID to `.env` as `TELEGRAM_CHAT_ID`

### Git Repository Setup

1. Create repository for blog content
2. Generate Personal Access Token (GitHub/Azure DevOps)
3. Add repository URL and token to `.env`

### Azure Setup

1. Install Azure CLI
2. Login: `az login`
3. Create resource group (or use Terraform)
4. Deploy infrastructure using Terraform
5. Configure Function App settings

## 🚀 Development

### Local Development

```bash
# Activate virtual environment
source venv/bin/activate

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run function locally
func start
```

### Testing

```bash
# Unit tests
pytest tests/

# Integration tests
pytest tests/integration/

# Coverage report
pytest --cov=src tests/
```

### Code Quality

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/
```

## 📊 Monitoring

### Application Insights

Monitor your function app through Azure Portal:
- Function execution metrics
- Error rates and logs
- Performance metrics
- Custom telemetry

### Alerts

Set up alerts for:
- Function failures
- High response times
- API quota limits
- Git operation failures

## 🔐 Security

### Secrets Management

- All API keys stored in Azure Key Vault
- Function App uses Managed Identity
- No secrets in code or configuration files

### Access Control

- Function App restricted to specific IP ranges
- Telegram bot token with minimal permissions
- Git repository access via read/write tokens only

## 🐛 Troubleshooting

### Common Issues

**Function App won't start:**
- Check Application Insights logs
- Verify environment variables
- Ensure all dependencies installed

**Perplexity API errors:**
- Verify API key validity
- Check quota limits
- Review request format

**Telegram bot not responding:**
- Verify bot token
- Check chat ID
- Ensure bot has message permissions

**Git operations failing:**
- Verify repository URL
- Check access token permissions
- Ensure branch exists

### Debug Mode

Enable debug logging:
```bash
export AZURE_FUNCTIONS_ENVIRONMENT=Development
export LOGGING_LEVEL=DEBUG
```

## 🚢 Deployment

### Manual Deployment

```bash
# Deploy infrastructure
cd terraform && terraform apply

# Deploy function code
func azure functionapp publish <app-name>
```

### CI/CD Pipeline

The project includes Azure Pipelines configuration:
- Automated testing
- Infrastructure deployment
- Function app deployment
- Integration tests

## 📝 Usage

### Daily Operation

1. Function triggers daily at configured time
2. Generates content using Perplexity AI
3. Sends to Telegram for approval
4. User can approve or request edits
5. Approved content committed to Git repository
6. Django app renders new blog post

### Manual Triggers

```bash
# Trigger function manually
curl -X POST https://<function-app>.azurewebsites.net/api/generate-post
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Follow code style guidelines
4. Add tests for new features
5. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- Create issue for bugs/features
- Check troubleshooting section
- Review Azure Functions documentation
- Monitor Application Insights for errors