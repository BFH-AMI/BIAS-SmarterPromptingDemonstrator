import streamlit as st
import os
import requests
import json
import time

# API Config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_API_KEY = os.path.join(BASE_DIR, "api_key_mistral.txt")


def load_api_key(file_path=FILE_PATH_API_KEY):
    with open(file_path, "r") as file:
        return file.read().strip()


MISTRAL_API_KEY = load_api_key()
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"


# Mistral API Calls
def call_mistral(messages, model="mistral-large-latest"):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


# Streamlit config
st.set_page_config(
    page_title="BIAS Prompt Optimizer",
    page_icon="✨",
    layout="centered"
)


def parse_response(response):
    """Parse prompt and explanation from the structured response"""
    lines = response.strip().split('\n')
    prompt = ""
    explanation = ""
    current_section = None

    for line in lines:
        if line.startswith("prompt:"):
            current_section = "prompt"
            prompt_start = line[7:].strip()
            if prompt_start:
                prompt = prompt_start
        elif line.startswith("explanation:"):
            current_section = "explanation"
            explanation_start = line[12:].strip()
            if explanation_start:
                explanation = explanation_start
        elif current_section == "prompt" and line.strip():
            prompt += "\n" + line if prompt else line
        elif current_section == "explanation" and line.strip():
            explanation += " " + line if explanation else line

    return prompt.strip(), explanation.strip()

# Custom CSS for BIAS colors
st.markdown("""
    <style>
    .stApp {
        background-color: #212222;
    }
    .main-title {
        color: #9076AF;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .intro-text {
        color: #FFFFFF;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        background-color: #FFFFFF;
        color: #212222;
    }
    .stButton > button {
        background-color: #80BC9E;
        color: #212222;
        font-weight: bold;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #9076AF;
        color: #FFFFFF;
    }
    .stButton > button:active {
    background-color: #80BC9E;  
    color: #212222;             
    }
    .status-box {
        background-color: #FCEA91;
        color: #212222;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        font-weight: bold;
    }
    .result-box {
        background-color: #FFFFFF;
        color: #212222;
        padding: 1.5rem;
        border-radius: 5px;
        border-left: 5px solid #9076AF;
        margin: 1rem 0;
    }
    .stSelectbox label {
        color: #FFFFFF !important;
    }
    .stTextArea label {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">✨ BIAS Prompt Optimizer</div>', unsafe_allow_html=True)
st.markdown('''
    <div class="intro-text">
    The BIAS NLP Demonstrator <b>Smarter Prompts for Less Biased Answers from LLMs</b> optimizes user prompts to obtain less biased results when prompting LLMs.
    Drawing on the latest research into how LLMs mirror societal biases such as the contact hypothesis, we showcase with this example how a suite of perspective-taking LLMs can reframe user prompts.    </div>
''', unsafe_allow_html=True)

# Model Selection
model_option = st.selectbox(
    "Choose a model",
    ["Mistral Large", "Mistral Small"],
    index=0
)

# Language Selection
language_option = st.selectbox(
    "Choose a language",
    ["Dutch", "English", "German", "Icelandic", "Italian", "Norwegian", "Turkish"],
    index=0
)

# Map model names
model_mapping = {
    "Mistral Large": "mistral-large-latest",
    "Mistral Small": "mistral-small-latest"
}

# User Input
user_prompt = st.text_area(
    "Your Prompt",
    placeholder="Enter here the prompt that should be optimized...",
    height=150
)

# Optimize Button
if st.button("🚀 Start optimization"):
    if user_prompt.strip():
        try:
            # Agent 1: NLP Research
            st.markdown('<div class="status-box">🔄 I am Agent 1, specialized in Bias in LLMs, and now working on your prompt...</div>',
                        unsafe_allow_html=True)

            agent1_system = """You are an expert on literature on societal stereotypes in LLMs. Your aim is to rephrase the given prompt to avoid that biases or societal stereotypes are reflected. 
            When this prompt is submitted to any LLM, the answer should be as neutral as possible.
            We have the following insights from research:
            - It can help to make a positive example when people or places are mentioned (e.g. positive contact or experience with a given group of people)
            - It can help to explicitely mention more details, less things are implicit, the more potential biases might come up. 

             Return the optimized prompt and a 1 sentence explanation of your changes in the following structure:
             prompt:
             explanation:
            
            Keep the original language of the prompt. Add your explanation in the same language. Do not use any formatting, just text.
             """

            messages1 = [
                {"role": "system", "content": agent1_system},
                {"role": "user", "content": f"Optimize this prompt:\n\n{user_prompt}"}
            ]

            response_1 = call_mistral(messages1, model=model_mapping[model_option])
            improved_prompt_1, explanation_1 = parse_response(response_1)

            # Agent 2: DEI/Legal
            st.markdown('<div class="status-box">🔄 I am Agent 2, specialized in DEI and legal aspects of discrimination, and now also checking the prompt...</div>',
                        unsafe_allow_html=True)

            agent2_system = """
            You are a specialist for Diversity and Inclusion and also the legal situation of discrimination law in Europe. 
            In the following prompt, add a statement of 1-2 sentences to point out legally relevant aspects for a LLM to avoid a biased output if this prompt is put into a LLM.
            Keep the original prompt and just add your statement.
            Return the optimized prompt and a 1 sentence explanation of your changes in the following structure:
             prompt:
             explanation:
            
            Keep the original language of the prompt. Add your explanation in the same language. Do not use any formatting, just text.
            """

            messages2 = [
                {"role": "system", "content": agent2_system},
                {"role": "user", "content": f"Optimize this prompt:\n\n{improved_prompt_1}"}
            ]

            response_2 = call_mistral(messages1, model=model_mapping[model_option])
            improved_prompt_2, explanation_2 = parse_response(response_2)

            # Display Result
            st.success("✅ Optimization done!")
            st.info("### 📋 Your Optimized Prompt")
            st.markdown('''<div class="intro-text"><b>Improved Prompt: </b>'''+improved_prompt_2, unsafe_allow_html=True)
            st.markdown('''<div class="intro-text"><b>Agent 1's Explanation: </b>'''+explanation_1, unsafe_allow_html=True)
            st.markdown('''<div class="intro-text"><b>Agent 2's Explanation: </b>'''+explanation_2, unsafe_allow_html=True)


        except Exception as e:
            st.error(f"❌ An error happened while optimizing: {str(e)}")
    else:
        st.warning("⚠️ Please enter a prompt!")

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #80BC9E;">This work is part of the Europe Horizon project BIAS, grant agreement number 101070468, funded by the European Commission, and has received funding from the Swiss State Secretariat for Education, Research and Innovation (SERI).</div>',
    unsafe_allow_html=True
)