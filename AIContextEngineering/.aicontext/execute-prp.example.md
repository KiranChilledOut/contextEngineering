# Example: Using execute-prp Workflow

## Context
Suppose you have already run existingRepo-prp and generate-prp, and you have:
- `.aicontext/repocontext.json` with project details (repo path, shell, languages, structure)
- A PRP file (e.g., PRPs/feature-todo-app.md) with a detailed plan, architecture, and validation gates

## How the AI Proceeds
1. Reads `.aicontext/RULES.md`, `.aicontext/repocontext.json`, and `.repoContext.md` (if present) for full context.
2. Loads the PRP file and confirms all context and validation gates are present.
3. Breaks down the PRP into actionable checklist items, e.g.:
   - [ ] Set up project structure
   - [ ] Implement main app module
   - [ ] Add authentication
   - [ ] Write unit tests
   - [ ] Run validation commands (e.g., pytest, linter)
   - [ ] Update documentation
4. Prompts the user before starting each checklist item:
   - "Ready to set up the project structure? (y/n)"
   - Waits for user confirmation before proceeding and checking off the item.
5. After each step, marks the item as complete in the checklist and prompts for the next step.
6. If the AI is unsure about any file or structure, it asks the user clarifying questions and updates `.repoContext.md` with new knowledge.
7. After all steps are complete, runs final validation, updates documentation, and prompts the user for feedback or next steps (e.g., deploy, refactor, start a new PRP).

## Example Checklist (for a Django Todo App)
```
- [ ] Create Django project and app structure
- [ ] Implement models for Todo items
- [ ] Add views and templates for CRUD operations
- [ ] Set up authentication
- [ ] Write unit tests in /tests
- [ ] Run: pytest tests/ -v
- [ ] Run: black .
- [ ] Update README.md with setup and usage instructions
```

## Tips
- Always wait for user confirmation before checking off each checklist item.
- Ask clarifying questions if any step or file is unclear.
- Update `.repoContext.md` with new knowledge after execution for future sessions.
