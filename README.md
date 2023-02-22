# Speech Translation using Azure Cognitive Services

This Python script allows for real-time speech translation from one language to another using the Azure Cognitive Services Speech SDK. 

## Requirements

- Python 3.5 or later
- `azure.cognitiveservices.speech` library
- A Speech API key and region from Azure Cognitive Services. You can obtain a free key with a free subscription [here](https://azure.microsoft.com/free/services/cognitive-services/).

## Installation

1. Install Python 3.5 or later. You can download it [here](https://www.python.org/downloads/).
2. Install the `azure.cognitiveservices.speech` library by running the following command in your terminal: 

```bash
pip install azure.cognitiveservices.speech
```

3. Replace `SPEECH_KEY` and `SPEECH_REGION` with your own Speech API key and region, respectively.

## Usage

1. Open a terminal window in the directory where the script is saved.
2. Run the script by typing `python transcribe.py` in the terminal, replacing `transcribe.py` with the name of the actual script file.
3. Speak into your microphone and the script will automatically translate your speech from the source language to the target language.
4. The translated text will be printed to the console.
