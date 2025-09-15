# Workflow: PRP for Existing Repository Context Engineering

## Purpose
Guide the AI and user through setting up context engineering for an existing local repository, ensuring all relevant project, environment, and structure details are captured for optimal AI assistance.

---

## Step 1: Prompt for Local Repository Path
- Ask: What is the full path to your local repository?
  - Example: C:\Users\ChilledOut\FileCloud\My Files\git\personal_portfolio
- Wait for user input.

## Step 2: Prompt for Shell Used
- Ask: Which shell do you use for this project?
  - Example: pwsh, bash, cmd, zsh, etc.
- Wait for user input.

## Step 3: Prompt for Repository Languages (in order)
- Ask: What are the main languages used in this repository, in order of importance?
  - Example: Python, Docker, Powershell
- Wait for user input.

## Step 4: Prompt for Project Structure Details
- Ask: Please describe the key structure of your project.
  - What are the main folders or apps?
  - Which folder is the main application, and which are sub-apps or special-purpose directories?
  - Any other important structure details?
  - Example:
    - C:\Users\ChilledOut\FileCloud\My Files\git\personal_portfolio\myportfolio_udemy is the Django project
    - C:\Users\ChilledOut\FileCloud\My Files\git\personal_portfolio\blogMarkdown is the app where I write blogs in markdown
- Wait for user input.

## Step 5: Generate Context Engineering Setup
- Use the above answers to:
  - Create or update .aicontext/RULES.md with shell, languages, and conventions
  - Document the project structure in .aicontext/PROJECT_STRUCTURE.md
  - Suggest or create INITIAL.md and PRP templates tailored to the project
  - Optionally, prompt for any additional project-specific rules or gotchas

## Step 6: Review and Confirm
- Present the generated context engineering setup to the user for review.
- Make any adjustments based on user feedback.

---

## Tips for Best Results
- Be explicit about shell, language, and structure for every project.
- Encourage users to add more details or examples as the project evolves.
- Use this workflow as a repeatable pattern for onboarding new repositories.


