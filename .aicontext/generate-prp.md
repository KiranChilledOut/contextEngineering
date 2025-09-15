# Workflow: Generate PRP (Product Requirements Prompt)

## IMPORTANT: Project Context Check
- If `.aicontext/repocontext.json` does NOT exist, prompt the user for all required project context:
  - **Project description:** Ask the user to describe what they want to build (e.g., 'I want to build a Django app for X', 'I want to build a Terraform project for Azure', etc.).
  - Repository path
  - Shell used
  - Main and secondary languages (in order)
  - Project structure details (main app, subfolders, special directories, etc.)
- Ask the user: "Do you already have a project structure in mind?" If yes, collect details. If not, propose an enterprise-grade structure based on the main language and best practices.
- Once details are collected, create `.aicontext/repocontext.json` before proceeding with PRP generation.

## Purpose
Guide the AI and user through generating a comprehensive PRP for a feature, leveraging all available context from .aicontext/RULES.md and .aicontext/repocontext.json, and following best practices for context engineering.

---

## Step 1: Preparation - Read Context
- Always read .aicontext/RULES.md for project-wide rules and conventions.
- Always read .aicontext/repocontext.json for repo path, shell, languages, and structure.
- Understand the main language, shell, project structure, and any special conventions or gotchas.
- Use the high-level project description to generate a focused and relevant PRP.

## Step 2: Checklist & Context Gathering
- Create or update a checklist for the feature or workflow.
- Scan the repo (using the path and structure from repocontext.json) to:
  - Identify existing patterns, modules, and tests relevant to the feature.
  - Find example files, code styles, and validation/test patterns.
- Prompt the user for any missing context (e.g., if INITIAL.md is incomplete, or if more examples are needed).

## Step 3: Build a Rich Context for PRP Generation
- Aggregate all relevant documentation, code patterns, and examples.
- Document this context in a way that the AI can use for PRP generation (e.g., in a context block at the top of the PRP or in .aicontext/context_snapshot.md).
- Use the project description and structure to tailor the PRP for the next execute step.

## Step 4: Execute the PRP Generation
- Use the context to fill out the PRP template:
  - Goal, Why, What, Success Criteria
  - All needed context (docs, examples, gotchas)
  - Current and desired codebase tree
  - Implementation blueprint (data models, structure, task list)
  - Validation gates (with correct shell commands)
- Confirm with the user before finalizing the PRP.

## Step 5: Output & Next Steps
- Save the generated PRP in the appropriate folder (e.g., PRPs/feature-name.md).
- Review the PRP with the user for completeness and clarity.
- Prompt for next steps (e.g., execute the PRP, revise, or add more context).

---

## Tips for Best Results
- Always leverage all available context before generating a PRP.
- Be explicit about shell, language, and structure in every feature request.
- Reference real code patterns and documentation.
- Ask for clarification if anything is missing or ambiguous.


