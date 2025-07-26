# AGENT.md – Learning Ladder AI Blueprint

---

## Agent Name

**Learning Ladder AI**  
Plan. Learn. Achieve. With AI by your side.

---

## Problem

Many learners have the motivation to grow their skills but struggle to convert broad ambitions into structured, achievable learning plans. Without clear goals, milestones, or curated resources, it's easy to lose direction or momentum.

---

## Solution

Learning Ladder AI acts as an intelligent learning assistant that helps users:

- Define their learning goal in natural language
- Break the goal down into a 4-week structured plan
- Recommend resources for each milestone
- Adapt plans over time (future functionality)
- Track progress and build consistent learning habits (future functionality)

The agent is powered by a large language model and built using a no-code platform (Langflow), making it accessible, customizable, and scalable.

---

## Agent Type

**Goal-Based Agent**  
Plans actions to achieve a specific end goal (learning objective), adjusting outputs based on user input and context.

---

## Key Tools & Components

| Tool / Component      | Purpose                                                |
|-----------------------|--------------------------------------------------------|
| OpenAI GPT            | Language understanding, reasoning, and plan generation |
| Prompt Templates      | Structured natural language instructions for planning  |
| Langflow              | No-code agent orchestration and UI                     |
| (Optional) Web Search Tool | Future expansion: pulling up-to-date learning resources |
| Memory Module         | Retain goal context and user preferences over time     |

---

## Responsible AI: Guardrails

**Orchestration Layer Guardrails**

- Validate that generated plans are realistic, safe, and motivational
- Avoid suggesting harmful or inappropriate resources
- Implement prompt constraints to ensure non-prescriptive advice

Additional considerations (future):
- Tool Layer: restrict agent’s access to external APIs or write permissions
- Model Layer: fine-tuned prompts to reinforce ethical and inclusive behavior

---

## Example Prompt Template

```text
You are an intelligent learning assistant. The user will give you three things:
1. Their learning goal
2. The duration they want to achieve it in (e.g., 4 weeks, 6 weeks)
3. Their current experience level (e.g., beginner, intermediate, advanced)

Your task is to:
- Break the goal into a structured weekly plan based on the duration
- Create 2–3 milestones per week
- For each milestone, recommend 2 helpful resources (videos, articles, tutorials, exercises)
- Use a supportive, motivational tone

If the user does not specify an experience level, assume they are a beginner.

Input example:
Goal: Learn Python for data analysis  
Duration: 6 weeks  
Experience Level: Beginner

Make the tone supportive and achievable. Tailor plans to beginners unless otherwise specified.

User goal: {goal_description}  
Duration: {duration}  
Experience level: {experience_level}

