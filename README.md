---
title: Learning Ladder AI
emoji: 📚
sdk: streamlit
sdk_version: 1.36.0
app_file: app.py
pinned: false
---

# learning-ladder-ai 

# Learning Ladder AI  
**Plan. Learn. Achieve. With AI by your side.**

[🚀 Live Demo](https://huggingface.co/spaces/sravanirc/learning-ladder-ai)

---

## Overview

**Learning Ladder AI** is an AI-powered learning goal planner that helps users break down ambitious learning goals into structured, achievable plans. Whether you're starting a new subject or upskilling for your career, Learning Ladder AI acts as your intelligent assistant — organizing your journey step-by-step.

Built using [Langflow](https://docs.langflow.org/) and GroqAI, this no-code MVP demonstrates how dynamic AI agents can support goal-setting, planning, and resource discovery — all through natural language.

---

## What Has Been Done So Far

- Developed a clean, responsive Streamlit UI for users to input:
  - Learning Topic (goal)
  - Preferred Duration
  - Experience Level (Beginner, Intermediate, Advanced)
- Integration with an AI backend via REST API (using environment variables for secure token and endpoint handling)
- Generated learning plans returned and displayed with:
  - An Overview table (desktop only, with scroll on mobile)
  - A weekly plan breakdown, optimized for readability across devices
- Custom styling for buttons and layout to enhance UX without excess complexity
- Error handling for API responses and JSON parsing issues
- Responsive design considerations including:
  - Hiding large tables on small screens with scrollbars to prevent overflow
  - Simplified and minimal CSS to keep the app lightweight and fast

---

## Key Features

- Breaks learning goals into weekly milestones
- Recommends curated learning resources
- (Future) Calendar or reminder integration
- Context-aware, memory-driven conversations
- Built with Responsible AI guardrails

---

## Example Use Case

> **User**: I want to learn Python for data analysis in 4 weeks.  
> **Learning Ladder AI**: Here's your weekly plan with goals and handpicked resources to guide your journey.

---

## Tech Stack

- [Langflow](https://langflow.org/) – No-code agent builder
- [Grok AI] 
- JSON-exported Langflow flows
- [Streamlit](https://streamlit.io/) – Frontend app framework

---

## Screenshots / Demo
[🚀 Live](https://huggingface.co/spaces/sravanirc/learning-ladder-ai)
*Coming soon...*

---

## Contributing

This is an MVP built for the Cajigo Bootcamp — currently under active development. Feedback and collaboration welcome!

---

## How to Run

```bash
# Activate virtual environment
source .venv/Scripts/activate   

# Install dependencies (run once or after deleting .venv)
pip install -r requirements.txt

# Run the app locally
streamlit run app.py
