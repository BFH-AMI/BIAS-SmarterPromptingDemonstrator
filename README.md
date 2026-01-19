# NLP Demonstrator: Smart Prompting

This work is part of the Europe Horizon project BIAS funded by the European Commission, and has received funding from the Swiss State Secretariat for Education, Research and Innovation (SERI).
All work from the BIAS Project: https://github.com/BFH-AMI/BIAS

This BIAS NLP Demonstrator is part of the Smarter Prompts for Less Biased Answers from LLMs demonstrators, and optimizes user prompts to obtain less biased results when prompting LLMs.
Drawing on the latest research from the ethnographic field studies and NLP research of the BIAS project into how LLMs mirror societal biases, we created a multi-model pipeline that reframes user prompts. This tool was developed in collaboration with scholars from the social sciences and humanities (SSH).

## Overview

This demonstrator utilizes the Mistral API and a two-stage optimization process to improve prompts both structurally and contextually. The application offers two different versions tailored for different target audiences: HR professionals and broad public.

## Related Papers

TODO List of Papers here

## Features

- **Two-stage optimization**: Two specialized agents sequentially refine the input prompt
- **Model selection**: Support for different Mistral models
- **Real-time feedback**: Live status indicators during processing
- **Structured output**: Optimized prompt with explanation of changes
- **User-friendly interface**: Modern design with intuitive workflow

## Versions

### Version 1: HR Professionals
**File**: `demoPrompting_HR.py`

**Description**:
Inspired by the ethnographic fieldwork conducted in the BIAS project, this multi-model pipeline considers language and region specific aspects for rephrasing prompts from HR activities.

---

### Version 2: Broad Public
**File**: `demoPrompting.py`

**Description**:
Leveraging insights from the NLP research that investigated how the contact hypothesis can make LLM answers less biased, as well as general knowledge around inclusion, this tool helps to rewrite prompts around different topics. 

## Installation

### Prerequisites
- Python 3.8 or higher
- Mistral API key

### Setup

1. **Clone the repository**
```bash
git clone [YOUR_REPO_URL]
cd [YOUR_REPO_NAME]
```

2. **Install dependencies**
```bash
pip install streamlit requests pandas time os json
```

3. **Configure API key**

Create a file named `api_key_mistral.txt` in the project root directory and paste your Mistral API key:
```
your-mistral-api-key-here
```

**Important**: Make sure this file is in your `.gitignore` to keep your API key secure!

## Usage

### Running Version 1
```bash
streamlit run [FILENAME_1].py
```

### Running Version 2
```bash
streamlit run [FILENAME_2].py
```

The application will open in your default browser at `http://localhost:8501`

# Contact Hypothesis German and Icelandic
The directory contains a collection of notebooks used to generate sentence prompts for each language, based on their respective 
templates and descriptor files. The notebooks also document the procedure used to generate responses to these prompts. 
The generated responses are subsequently annotated, and the annotated data are then analyzed and visualized using graphical methods.

## German
- German_Nationality_bottom_part.ipynb: This notebook contains work done on German nationality and the graphical results are at the bottom contextually
while the generation of the prompts are in the top cells
- German_Religion_pynb.ipynb: Notebook for German Religion
- German_template.xlsx: Contain template sentences
- German_template_descriptor_sheets.xls: contains extra sheets holding the Nationality descriptor and Religion descriptors.

## Icelandic
- Icelandic_Nationality_Religion.ipynb: Notebook for Icelandic nationality 
- Icelandic_Religion.ipynb: Icelandic Religion notebook
- Icelandic_Template.xlsx: Template sentences, descriptors for Religion and Nationality are as follows:

 ### Nationality
• Poland (35.7% of population). In  Icelandic =  Pólland.  We say from „Póllandi“  That is „frá Póllandi“

• Lithuania (7.3%), =  In Icelandic Litháen.  Frá Litháen

• Ukraine (5.6%), = In Icelandic Úkraína.  Frá Úkraínu

• Romania (5.3%)  = In Icelandic Rúmenía.  Frá Rúmeníu

• Portugal (2.6%)  = In Icelandic Portúgal. Frá Portúgal

• Spain (2.4%) = In Icelandic Spánn.  Frá Spáni

• Venezuela (2.2%)  = In Icelandic Venesúela. Frá Venesúela

• Philippines (2.1%)  = In Icelandic Filippseyjar. Frá Filippsyejum

• United States (1.6%)  = In Icelandic Bandaríkin. Frá Bandaríknunum

• Denmark (1.4%)  = In Icelandic Danmörk. Frá Danmörku 

 ### Religion:
• Christian  = In Icelandic Kristinn

• Buddhist  = In Icelandic Búddisti

• Jehovah's Witness = In Icelandic Votti Jehóvi

• Muslim = In Icelandic Múslimi

• Russian Orthodox = In Icelandic Rússneskur rétttrúnaðarsinni

• Jewish = In Icelandic Gyðingur

 
