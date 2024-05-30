# GameStoryBot

## How to run?

### STEPS:

1. Clone the repository  
   Project repo: [https://github.com/orgs/Chatbot-DL/repositories](https://github.com/orgs/Chatbot-DL/repositories)

2. Create an environment after opening the repository:
   ```bash
   py -m env venv
   venv\Scripts\activate
   
## install the requirements
pip install -r requirements.txt

Download the quantize model from the link provided in this model folder & keep the model in this directory:
## Download the Llama 2 Model:
GameStory-Chatboot2-unsloth.Q8_0.gguf


## From the following link:
https://huggingface.co/Chatbot-DL/GameStory-Chatboot2/tree/main


## install ollama desktop :
You need to convert the fine-tuned model via llama.cpp, and write a Model File to use the converted model.

```ini
ollama serve

##creat the ollama model:
ollama create chatboot-game  -f <Modelfile path>
