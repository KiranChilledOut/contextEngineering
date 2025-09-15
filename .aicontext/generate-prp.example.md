# Example: Using generate-prp Workflow

## Context
Suppose you have a Python/Django project with the following in .aicontext/repocontext.json:
```
{
  "repo_path": "C:/Users/ChilledOut/FileCloud/My Files/git/personal_portfolio",
  "shell": "pwsh",
  "languages": ["Python", "Docker", "Powershell"],
  "structure": {
    "main_app": "myportfolio_udemy",
    "blog_app": "blogMarkdown"
  }
}
```
And .aicontext/RULES.md specifies:
- Use PowerShell for all shell commands
- Follow PEP8 and Django conventions
- All tests in /tests, all apps in their own folders

## How the AI Proceeds
1. Reads RULES.md and repocontext.json for context.
2. Scans the repo for code patterns, test structure, and examples.
3. Prompts the user for any missing details (e.g., if INITIAL.md is incomplete).
4. Aggregates context into a block like:

```
# Context for PRP Generation
- Main language: Python
- Shell: pwsh
- Main app: myportfolio_udemy
- Blog app: blogMarkdown
- Style: PEP8, Django conventions
- All tests in /tests
- Example code: see blogMarkdown/models.py, myportfolio_udemy/views.py
```

5. Uses this context to fill out the PRP template, including validation gates like:
```
# Validation Gates
- Run: pytest tests/ -v
- Run: black .
- Run: mypy .
```

6. Saves the PRP as PRPs/feature-name.md and reviews with the user.

## Tips
- Always update repocontext.json if the repo structure or environment changes.
- Add more examples to .aicontext/examples/ to improve PRP quality.
