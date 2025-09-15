# AI Context Engineering Template

A comprehensive template for building context-rich AI coding workflows. This template enables you (and your AI coding assistant) to:

- Understand project rules, languages, and shell environments
- Generate and execute feature blueprints (PRPs) with full context
- Track and validate implementation progress
- Provide examples, documentation, and validation gates for robust, repeatable development

> **Note:**
> - The AI will always create a `checklist.md` for your project automatically when you run any workflow (e.g., onboarding, PRP generation, execution).
> - Users do **not** need to create or manage checklists themselves.
> - All project context and workflow state is persisted in `.md` files (e.g., `.repoContext.md`, `checklist.md`) in your repo, so the AI can always recover context in a new session—even if you close and restart.
> - All required context and files (such as PRPs and repocontext.json) are created dynamically by the AI during the workflow. You do not need to create any special files or folders in advance.

## 🚀 Quick Start

1. **Copy the .aicontext folder into your repo**
   - From this template, copy the entire `.aicontext` folder into your new or existing project directory (e.g., `AIContextEngineering/.aicontext` → `your-repo/.aicontext`).
2. **Explore the .aicontext/ folder**
   - Contains project rules, workflow templates, and step-by-step guides for the AI
3. **Add your own feature requests**
   - Use the provided templates to describe new features
4. **Let your AI coding assistant guide you**
   - Ask the AI to read .aicontext/ and follow the documented workflows

---

## 🧑‍💻 Step-by-Step: How to Use This Template

### Flow 1: For a New Idea
1. **Describe your idea** (e.g., "I want to build a Django app for todos").
2. **Run generate-prp**
   - The AI will prompt for project description, shell, languages, and structure.
   - If you don’t have a structure in mind, the AI will propose a best-practice layout.
   - The AI creates .aicontext/repocontext.json and generates a PRP with validation gates.
3. **Review and confirm the PRP**
   - Check the plan, checklist, and validation steps.
4. **Run execute-prp**
   - The AI breaks down the PRP into actionable checklist items.
   - You confirm each step before the AI proceeds.
   - The AI implements, validates, and documents as it goes.
5. **After execution**
   - The AI updates .repoContext.md with all project knowledge.
   - You’re ready to deploy, test, or iterate further.

### Flow 2: For an Existing Project
1. **Run existingRepo-prp**
   - The AI prompts for repo path, shell, languages, and structure.
   - You describe your project’s layout and details.
   - The AI creates .aicontext/repocontext.json and .repoContext.md.
2. **Run generate-prp**
   - The AI uses all context to generate a PRP for your next feature or refactor.
3. **Review and confirm the PRP**
   - Check the plan, checklist, and validation steps.
4. **Run execute-prp**
   - The AI breaks down the PRP into actionable checklist items.
   - You confirm each step before the AI proceeds.
   - The AI implements, validates, and documents as it goes.
5. **After execution**
   - The AI updates .repoContext.md with all project knowledge.
   - You’re ready to deploy, test, or iterate further.

For detailed examples, see `end-to-end-example.md`.

---

## 📚 Template Structure

```
AIContextEngineering/
├── .aicontext/         # All AI context, rules, and workflow templates
└── README.md           # This file
```

## 🧠 How It Works

- **.aicontext/**: The AI reads this folder to understand your project’s rules, preferred languages, shell environment, and workflow steps. You can add or edit markdown files here to define new workflows or rules.
- **checklist.md**: Created and managed automatically by the AI for each project/workflow. Tracks your progress and ensures you don’t miss any steps.
- All other required files (e.g., PRPs, repocontext.json, .repoContext.md) are created dynamically by the AI as you use the workflows.

## 🛠️ Customization

- Add new workflow templates to .aicontext/ for any process you want the AI to follow (e.g., onboarding, code review, deployment).
- Update RULES.md in .aicontext/ to define project-wide conventions, language preferences, and shell details (e.g., Windows PowerShell, Bash, etc.).

## 🏆 Best Practices

- Be explicit about your shell and main programming language in .aicontext/RULES.md.
- Let the AI create and manage checklists for you.
- Add validation steps and test requirements to your PRPs for robust, production-ready code.
- Encourage your team to add new workflows as your project grows.

## ❤️ Why Use This Template?

- Makes any AI coding assistant as powerful and context-aware as possible
- Enables repeatable, high-quality development workflows
- Easy for anyone to extend and adapt for their own projects
- Designed for teams who want to get the most out of AI coding

---

Ready to build smarter? Start by exploring .aicontext/ and let your AI coding assistant guide you step by step!

