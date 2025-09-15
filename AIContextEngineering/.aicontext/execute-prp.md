# Workflow: Execute PRP (Product Requirements Prompt)

## 🚩 Checklist-Driven Execution (Critical)
- For every PRP execution or major task, the AI must create or update a checklist (e.g., checklist.md or a TODO list) and check off items as they are completed. This ensures progress is tracked, nothing is missed, and the user can review the workflow at any time.

## Context Awareness (Critical First Step)
- Always read `.aicontext/RULES.md` and `.aicontext/repocontext.json` before starting execution.
- Use this context to ensure all commands, code, and validation steps match the project’s shell, language, and conventions.

## Step 1: Load the PRP
- Read the specified PRP file in PRPs/ (e.g., PRPs/feature-name.md).
- Confirm all context, requirements, and validation gates are present.
- If anything is missing (e.g., shell, language, structure), prompt the user and update the PRP before proceeding.
- If the project is new and no structure exists, propose a best-practice structure based on the main language and PRP goals, and confirm with the user.

## Step 2: Plan the Implementation
- Break down the PRP into actionable tasks (use checklist.md or a TODO list).
- Identify code patterns, modules, and tests to follow.
- Confirm the plan with the user before starting execution.

## Step 3: Execute Each Task
- Implement code, tests, and documentation as described in the PRP.
- After each major step, validate with the user and run any specified validation commands (PowerShell, tests, etc.).
- If errors or failures occur, debug and iterate until all validation gates pass.

## Step 4: Final Validation
- Run all validation commands and tests listed in the PRP.
- Ensure all success criteria are met and documented.
- Review the implementation with the user for completeness and clarity.

## Step 5: Completion, Documentation, and Project Knowledge
- Mark tasks as complete in checklist.md.
- Update README.md and any relevant documentation.
- After executing the checklist for an existing project, if the AI is unsure about any file or structure, it must:
  - Ask the user clarifying questions.
  - Go through all files in the project.
  - Create or update a `.repoContext.md` file summarizing all accumulated knowledge about the project structure, conventions, and important files.
- In future sessions, always read `.repoContext.md` to quickly understand the project structure and details before starting any new task.
- Prompt the user for feedback or next steps (e.g., deploy, refactor, further testing, or start a new PRP).

---

## Tips for Best Results
- Always follow the PRP’s validation gates and test requirements.
- Use PowerShell syntax for all commands and scripts (or the shell specified in repocontext.json).
- Ask for clarification if any step is unclear or context is missing.
- Encourage the user to review and iterate for the best outcome.


