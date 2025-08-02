# Context Engineering Template - Project Architecture

## 🎯 Project Goals
This template provides a comprehensive framework for Context Engineering - the discipline of engineering context for AI coding assistants. The goal is to enable AI assistants to implement complex features end-to-end with proper context.

## 🏗️ Architecture Overview
```
context-engineering-intro/
├── .claude/                    # Claude Code configuration
│   ├── commands/              # Custom slash commands
│   │   ├── generate-prp.md   # Generates comprehensive PRPs
│   │   └── execute-prp.md    # Executes PRPs to implement features
│   └── settings.local.json   # Claude Code permissions
├── PRPs/                      # Product Requirements Prompts
│   ├── templates/            # PRP templates
│   └── *.md                  # Generated PRPs
├── examples/                  # Code examples (critical for patterns)
├── use-cases/                # Real-world implementation examples
│   ├── mcp-server/          # MCP server implementation
│   ├── pydantic-ai/         # Pydantic AI examples
│   └── template-generator/   # Template generation utilities
├── CLAUDE.md                 # Global AI assistant rules
├── PLANNING.md              # This file - project architecture
├── TASK.md                  # Task tracking
├── INITIAL.md               # Template for feature requests
└── README.md                # Documentation
```

## 🔧 Core Components

### Context Engineering System
- **CLAUDE.md**: Global rules for AI behavior, coding standards, testing requirements
- **INITIAL.md**: Template for describing feature requests with proper context
- **PRPs/**: Generated comprehensive implementation blueprints
- **examples/**: Critical code patterns and examples for AI to follow

### Slash Commands
- `/generate-prp`: Analyzes feature request and creates comprehensive PRP
- `/execute-prp`: Implements features from PRP with validation loops

### Use Cases
- **mcp-server/**: TypeScript MCP server with authentication and database tools
- **pydantic-ai/**: Python AI agent examples with structured outputs
- **template-generator/**: Tools for generating new project templates

## 🎨 Style & Conventions

### File Organization
- Keep files under 500 lines (enforced in CLAUDE.md)
- Organize by feature/responsibility
- Use clear module separation

### Language Standards
- **Python**: PEP8, type hints, Black formatting, Google-style docstrings
- **TypeScript**: Modern ES6+, proper typing, consistent imports
- **Documentation**: Markdown with clear structure

### Testing Requirements
- Pytest for Python projects
- Vitest for TypeScript projects
- Minimum: 1 success case, 1 edge case, 1 failure case per function

## 🔄 Workflow Patterns

### Feature Implementation Flow
1. Create feature request in INITIAL.md format
2. Run `/generate-prp INITIAL.md` to create comprehensive PRP
3. Run `/execute-prp PRPs/feature-name.md` to implement
4. AI follows validation loops to ensure working code

### Context Engineering Principles
1. **Comprehensive Context**: Include all necessary documentation, examples, patterns
2. **Validation Gates**: Multiple checkpoints to ensure quality
3. **Self-Correction**: AI can fix its own mistakes with proper feedback loops
4. **Pattern Following**: Examples directory provides implementation patterns

## 🚀 Upgrade Path
- Template is designed to be extensible
- New use-cases can be added to demonstrate patterns
- Slash commands can be enhanced for specific workflows
- CLAUDE.md can be customized per project needs

## 📋 Success Criteria
A successful Context Engineering implementation should:
- Enable AI to implement complex features end-to-end
- Follow consistent patterns and conventions
- Include comprehensive tests and validation
- Require minimal human intervention after initial setup
- Be self-documenting and maintainable