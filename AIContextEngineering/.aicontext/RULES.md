### 🔄 Project Awareness & Context
- **Main language:** (fill in for your project, e.g. Python, TypeScript)
- **Secondary language(s):** (e.g. Bash, PowerShell, etc.)
- **Shell/OS:** 
- **Always use the mentioned Shell syntax and escaping for all shell commands.**
- **Always confirm file paths and module names exist before referencing them.**

### 🧱 Code Structure & Modularity
- Never create a file longer than 500 lines of code. Refactor if needed.
- Organize code into clearly separated modules, grouped by feature or responsibility.
- Use clear, consistent imports (prefer relative imports within packages).

### 🧪 Testing & Reliability
- Always create unit tests for new features (functions, classes, routes, etc).
- After updating any logic, check whether existing unit tests need to be updated.
- Tests should live in a /tests folder mirroring the main app structure.
- Include at least:
  - 1 test for expected use
  - 1 edge case
  - 1 failure case

### ✅ Task Completion
- Track progress in checklist.md and mark completed steps immediately.

### 📎 Style & Conventions
- Use your main language’s style guide (e.g., PEP8 for Python, Prettier for JS/TS, powershell ).
- Use type hints and formatters .
- Write docstrings for every function using a consistent style.

### 📚 Documentation & Explainability
- Update README.md when new features are added, dependencies change, or setup steps are modified.
- Comment non-obvious code and ensure everything is understandable to a mid-level developer.
- When writing complex logic, add an inline # Reason: comment explaining the why, not just the what.

### 🧠 AI Behavior Rules
- Never assume missing context. Ask questions if uncertain.
- Never hallucinate libraries or functions – only use known, verified packages.
- Always confirm file paths and module names exist before referencing them in code or tests.
- Never delete or overwrite existing code unless explicitly instructed to or if part of a checklist task.

---

## 🚨 CORE AI CONTEXT ENGINEERING RULES (CRITICAL) 🚨

### 📝 PRP File Convention
- Every PRP workflow (such as onboarding, feature generation, etc.) must have its own markdown file in .aicontext/ (e.g., prp_existingRepo.md).
- Each PRP file should have a corresponding examples file (e.g., prp_existingRepo.examples.md) that demonstrates how to answer the prompts.
- The AI must always read the PRP file for workflow logic and the examples file for how to prompt and interpret user responses.
- This ensures the AI reacts contextually and interactively for each workflow, using real examples as guidance.

### 🤖 AI Behavior for .aicontext Workflows
- When a user asks the AI to "read the .aicontext" folder, the AI must:
  1. List all files in .aicontext/ that follow the prp_*.md naming pattern (these are PRP workflows/actions).
  2. Output a list of available PRP workflows (with file names and short descriptions if present).
  3. Prompt the user to choose which PRP workflow to run.
  4. Once selected, read the PRP file for workflow logic and prompts, and reference the corresponding examples file for guidance.
  5. Guide the user step-by-step through the workflow, collecting required information and generating outputs as needed.
- This ensures the system is interactive, discoverable, and user-friendly—like a menu of available actions.

### 📄 Repository Context and Rules
- When a user completes the prp_existingRepo.md workflow, the AI must create a repocontext.json file in the .aicontext folder containing all collected details (repo path, shell, languages, structure, etc.).
- Before running any workflow, the AI must always read both .aicontext/RULES.md and .aicontext/repocontext.json (if present) to understand the repository context, shell, languages, and conventions.
- This ensures the AI always operates with full awareness of the project environment and user preferences.

