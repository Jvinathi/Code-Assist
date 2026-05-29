# 🤖 Multi-Agent AI Coding Assistant

An autonomous AI-powered coding assistant that converts natural language software requirements into complete working projects using a multi-agent architecture.

---

# 🚀 Live Demo

https://code-assist-yfmscgttctxrm7nt2xuwmy.streamlit.app/

---

# 📌 Project Overview

This project simulates a real-world AI software engineering team using multiple specialized AI agents.

The system accepts a natural language software request such as:

```bash
Build a calculator web app
```

and automatically:

* Plans the project
* Designs the architecture
* Generates files
* Writes code
* Reviews generated code
* Validates JavaScript
* Creates downloadable projects

The application is built using LangGraph, Groq-hosted LLMs, Streamlit, and Playwright.

---

# ✨ Features

## 🧠 Multi-Agent Workflow

### Planner Agent

Analyzes the user request and creates the project plan.

### Architect Agent

Generates project architecture and file structure.

### Coder Agent

Writes complete working code for every file.

### Reviewer Agent

Reviews and improves generated code.

### JavaScript Validator

Validates generated JS syntax before saving files.

### Browser Execution Validator

Uses Playwright to verify generated applications.

### ZIP Export

Allows users to download generated projects instantly.

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## AI Framework

* LangGraph

## LLM Provider

* Groq Cloud

## Models

* Qwen
* Kimi K2

## Validation

* Esprima
* Playwright

## Version Control

* Git & GitHub

---

# 🧠 System Architecture

The project follows a multi-agent architecture where multiple AI agents collaborate together.

## Workflow

1. User enters software request
2. Planner Agent analyzes requirements
3. Architect Agent creates file structure
4. Coder Agent generates code
5. Reviewer Agent improves generated code
6. JavaScript Validator checks syntax
7. Playwright tests generated application
8. ZIP package is generated for download

---

# 📂 Project Structure

```bash
Code-Assist/
│
├── app/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── architect.py
│   │   ├── coder.py
│   │   └── reviewer.py
│   │
│   ├── core/
│   │   ├── graph_builder.py
│   │   ├── prompts.py
│   │   └── llm.py
│   │
│   ├── services/
│   │   ├── file_writer.py
│   │   ├── js_validator.py
│   │   ├── execution_validator.py
│   │   ├── zip_service.py
│   │   └── project_namer.py
│   │
│   ├── generated_projects/
│   │
│   └── main.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Jvinathi/Code-Assist.git
```

---

## 2. Move Into Project

```bash
cd Code-Assist
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

Get API key from:

https://console.groq.com

---

# ▶️ Running the Application

Run the Streamlit app:

```bash
streamlit run app/main.py
```

Application will start at:

```bash
http://localhost:8501
```

# Example Prompts

```bash
Build a calculator web app
```

```bash
Build a todo app using HTML CSS and JavaScript
```

```bash
Build a responsive portfolio website
```

---

# 🔥 Future Improvements

* React project generation
* FastAPI backend generation
* Self-healing AI loops
* Docker support
* Memory-enabled AI agents
* Full-stack project generation
* Deployment automation
* Multi-model orchestration

---

# 🚀 Deployment

The application is deployed using Streamlit Cloud.

---

# 📚 Key Learnings

This project helped in understanding:

* Multi-Agent Systems
* LangGraph Workflows
* AI Code Generation
* Browser Automation
* Runtime Validation
* AI System Design
* LLM Orchestration
* Autonomous Engineering Systems

---

# 👨‍💻 Author

Jonnala Vinathi Reddy

GitHub:
https://github.com/Jvinathi

---

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
