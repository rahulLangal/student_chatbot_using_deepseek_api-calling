# Student Chatbot

A lightweight Streamlit chatbot that interfaces with OpenRouter-compatible APIs. Created by Rahul .

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Features
- Clean Streamlit chat interface with persistent history
- OpenRouter API integration (via `openai` Python client)
- Minimalist implementation (single `app.py` file)
- Customizable system prompts and model selection
- Secure API key management through Streamlit secrets

## Requirements
- Python 3.8+
- Required packages:
  ```bash
  pip install streamlit openai
