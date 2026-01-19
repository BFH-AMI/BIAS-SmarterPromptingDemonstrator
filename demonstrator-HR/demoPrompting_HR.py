import streamlit as st
import os
import requests
import json
import time
import pandas as pd
from datetime import datetime
import os

# API Config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_API_KEY = os.path.join(BASE_DIR, "api_key_mistral.txt")


def load_api_key(file_path=FILE_PATH_API_KEY):
    with open(file_path, "r") as file:
        return file.read().strip()


MISTRAL_API_KEY = load_api_key()
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"


# Mistral API access
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


# Streamlit Config
st.set_page_config(
    page_title="BIAS Prompt Optimizer for HR Experts",
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
st.markdown('<div class="main-title">✨ BIAS Prompt Optimizer for HR Experts</div>', unsafe_allow_html=True)
st.markdown('''
    <div class="intro-text">
    This BIAS NLP Demonstrator is part of the <b>Smarter Prompts for Less Biased Answers from LLMs</b> demonstrators, and optimizes user prompts to obtain less biased results when prompting LLMs.
    Drawing on the latest research from the ethnographic field studies of the BIAS project into how LLMs mirror societal biases, we created a multi-model pipeline that reframes user prompts. This tool was developed in collaboration with scholars from the social sciences and humanities (SSH).    </div>
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

# Prepare data structure to store
columns = ["record_id", "language", "model", "prompt", "adapted_prompt", "explanation"]
df = pd.DataFrame(columns=columns)

def sanitize(text):
    if text is None:
        return ""
    return text.replace("\n", " ").replace("\r", " ").strip()

def add_record(df, language, model, prompt, extracted_info, answer, explanation):
    new_id = 1 if df.empty else df["record_id"].max() + 1

    new_row = pd.DataFrame([{
        "record_id": new_id,
        "language": language,
        "model": model,
        "prompt": sanitize(prompt),
        "extracted_info": sanitize(extracted_info),
        "adapted_prompt": sanitize(answer),
        "explanation:": sanitize(explanation)
    }])

    # concat is the new replacement for append
    df = pd.concat([df, new_row], ignore_index=True)
    return df

# Optimize Button
if st.button("🚀 Start optimization"):
    if user_prompt.strip():
        try:

            # Agent 1: Retrieve suitable knowledge from SSH research knowledge base
            st.markdown(
                '<div class="status-box">🔄 I am Agent 1, and analyzing what know-how needs to be retrieved...</div>',
                unsafe_allow_html=True)

            st.markdown(
                '<div class="status-box">🔄 Seems you are working with '+language_option+'...let me get the relevant data...</div>',
                unsafe_allow_html=True)

            FILE_PATH_ITA = os.path.join(BASE_DIR, "italian.txt")
            if language_option =="Italian":
                with open(FILE_PATH_ITA, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                langspec = "".join(line for line in lines if not line.lstrip().startswith("#"))

            FILE_PATH_NO = os.path.join(BASE_DIR, "norwegian.txt")
            if language_option =="Norwegian":
                with open(FILE_PATH_NO, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                langspec = "".join(line for line in lines if not line.lstrip().startswith("#"))

            agent1_system = """You are a social science and humanities expert on AI bias in recruitment.
            You are preparing data for another agent that rephrases the following prompt to avoid biases in LLM answers.
            You receive a large file with information from research, and you need to summarize the most relevant aspects for the given prompt, that the other agent needs to take into consideration.
            Language specific content: """ + langspec + """
            Do not use ANY formatting AT ALL, just text.
            """

            messages1 = [
                {"role": "system", "content": agent1_system},
                {"role": "user", "content": f"Optimize this prompt:\n\n{user_prompt}"}
            ]

            selected_data = call_mistral(messages1, model=model_mapping[model_option])

            # Agent 2: SSH Research, rephrasing
            st.markdown(
                '<div class="status-box">🔄 I am Agent 2, SSH expert for AI biases in recruitment, and now working on your prompt...</div>',
                unsafe_allow_html=True)

            agent2_system = """You are a social science and humanities expert on AI bias in recruitment. Your aim is to rephrase the given prompt to avoid that biases or societal stereotypes are reflected. 
            When this prompt is submitted to any LLM, the answer should be as neutral as possible.
            Consider the following general points:
            - Make sure you consider the diversity aspects of all people in the prompt. Suggest balancing in terms of gender, age, race, class, and sexuality when relevant.
            
            Consider the following particular research results for the selected language:"""+selected_data+"""
             Return the optimized prompt and a 1 sentence explanation of your changes in the following structure:
             prompt:
             explanation:

            Keep the original language of the prompt. Add your explanation in the same language. Do not use any formatting, just text.
             """

            messages1 = [
                {"role": "system", "content": agent2_system},
                {"role": "user", "content": f"Optimize this prompt:\n\n{user_prompt}"}
            ]

            response_1 = call_mistral(messages1, model=model_mapping[model_option])
            improved_prompt_1, explanation_1 = parse_response(response_1)

            # Display Result
            st.success("✅ Optimization done!")
            st.info("### 📋 Your Optimized Prompt")
            # st.markdown(f'<div class="result-box">{improved_prompt_2}</div>',
            # unsafe_allow_html=True)
            st.markdown('''<div class="intro-text"><b>Improved Prompt: </b>''' + improved_prompt_1,
                        unsafe_allow_html=True)
            st.markdown('''<div class="intro-text"><b>Agent 1's Explanation: </b>''' + explanation_1,
                        unsafe_allow_html=True)
            st.markdown('''<div class="intro-text"><b>Extracted Infos: </b>''' + selected_data,
                        unsafe_allow_html=True)

            df = add_record(df, language_option, model_option, user_prompt, selected_data, improved_prompt_1, explanation_1)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            filename = f"records_{timestamp}.csv"
            FILE_PATH_OUT = os.path.join(BASE_DIR, filename)

            df.to_csv(FILE_PATH_OUT, sep=";", index=False)

            print(df)
            print(f"Saved to {filename}")

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