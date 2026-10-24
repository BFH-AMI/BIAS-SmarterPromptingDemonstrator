# NLP Demonstrator: Smart Prompting

This BIAS NLP Demonstrator is part of the Smarter Prompts for Less Biased Answers from LLMs demonstrators, and optimizes user prompts to obtain less biased results when prompting LLMs.
Drawing on the latest research from the ethnographic field studies and NLP research of the BIAS project into how LLMs mirror societal biases, we created a multi-model pipeline that reframes user prompts. This tool was developed in collaboration with scholars from the social sciences and humanities (SSH).

## Acknowledgements
This work is part of the Europe Horizon project BIAS funded by the European Commission, and has received funding from the Swiss State Secretariat for Education, Research and Innovation (SERI).
All work from the BIAS Project: https://github.com/BFH-AMI/BIAS

## Overview

This demonstrator utilizes the Mistral API and a two-stage optimization process to improve prompts both structurally and contextually. The application offers two different versions tailored for different target audiences: HR professionals and broad public.

## Related Papers

Ikae, C., & Kurpicz-Briki, M. (2025, März 20). Measuring Bias in German Prompts to GPT Models Using Contact Hypothesis. Proceedings of the 2nd Workshop on AI bias: Measurements, Mitigation, Explanation Strategies (AIMMES 2025), Barcelona, Spain. https://doi.org/10.5281/zenodo.15649157

Ikae Catherine, Guðbjörg Linda Rafnsdóttir, Ragna Kemp Haraldsdóttir, and Mascha Kurpicz-Briki. 2026. Extending the Contact Hypothesis: Cross-Linguistic Evaluation of Religion and Nationality Bias When Prompting LLMs in German and Icelandic. In Proceedings of the 11th Edition of the Swiss Text Analytics Conference, pages 90–100, Zurich, Switzerland. Association for Computational Linguistics. https://aclanthology.org/2026.swisstext-1.8/

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
- Foreign nationality distributions in the three German speaking countries are as shown below:
  
| Nationality   | % of foreign nationals in Switzerland  | % of foreign nationals in Austria  | % of foreign nationals in Austria  |  
 | --- | --- | --- | --- | 
|Romania |6.55% |1.45% |8.52% |
|Poland |6.39% |1.93% |3.77% |
|Italy |4.63% |13.98% |2.19% |
|Bulgaria |3.14% |0.74% |2.21% |
|Türkiye |11.14% |2.19% |6.89% |
|Ukraine |8.92% |2.86% |4.48% |
|Serbia |1.95% |2.46% |6.79% |
|Portugal |1.01% |10.56% |NA |
|France |1.01% |6.77% |NA |

### Target words used as nationality for German speaking regions:
  - Rumänien
  - Polen
  - Italien
  - Bulgarien
  - Kroatien
  - Griechenland
  - Ungarn
  - der Türkei
  - der Ukraine
  - Russland
  - dem Kosovo
  - Serbien
  - den USA
  - Syrien
  - Afghanistan
  - dem Irak
  - Indien
  - Serbien
  - Bosnien und Herzegowina
  - Portugal
  - Frankreich 

### Target words used for religion:
- christlichen Glaubens
- buddhistischen Glaubens
- die Zeugen Jehovas sind
- islamischen Glaubens
- russisch-orthodoxen Glaubens
- jüdischen Glaubens
- ohne spezifischen Glauben

### Target words for gender and sexuality:
  - weiblichen Geschlechts
  - männlichen Geschlechts
  - nicht-binären Geschlechts
  - mit homosexueller Orientierung
  - mit heterosexueller Orientierung
  - mit bisexueller Orientierung
  - mit asexueller Orientierung
  - mit queerer Orientierung
  - mit LGBTQ+ Orientierung


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
 
   ### Target words for Icelandic religion:
 
 |Descriptor Plural | Descriptor Singular|
 | --- | --- | 
| aðhyllast kristni | aðhyllist kristni|
| aðhyllast búddisma | aðhyllist búddisma|
| aðhyllast Votta Jehóva | aðhyllist Votta Jehóva|
| aðhyllast íslam | aðhyllist íslam|
| aðhyllast rússnesku rétttrúnaðarkirkjuna |aðhyllist rússnesku rétttrúnaðarkirkjuna |
| aðhyllast án sérstakrar trúar | aðhyllist án sérstakrar trúar|
| aðhyllast gyðingdóm | aðhyllist gyðingdóm |


### Target words for Icelandic Gender and sexuality:
- karlkyns
- kvenkyns
- kynsegin
- hinsegin
- gagnkynhneigð
 
