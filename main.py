import ollama
import os
import json
import re
import time
import importlib

llm_endpoint = "http://localhost:11434/api/generate"
message_history = []
modules = {}

def process_agentic_command(cmd:dict):
    modules[cmd["cmd"]](*cmd["args"])

def stream_ollama_response(prompt: str, model: str = "huihui_ai/gpt-oss-abliterated:20b"):

    message_history.append({'role': 'user', 'content': prompt})
    stream = ollama.chat(model=model, messages=message_history, stream=True)

    reply = ''
    for chunk in stream:
        if 'message' in chunk and 'content' in chunk['message']:
            delta = chunk['message']['content']
            print(delta, end='', flush=True)
            reply += delta

        elif 'response' in chunk:
            print(chunk['respond'])

    print('\n')

    message_history.append({'role': 'assistant', 'content': reply})

    return reply

if __name__ == "__main__":
    docs = []

    for d in os.scandir('modules'):
        if (d.is_dir() and (d.name != '__pycache__')):
            docs.append( open('modules/' + d.name + '/docs.txt').read())
            
            #dynamically importing modules
            # assume module repo has same name as function - not suitable long term
            module_path = "modules." + d.name + "." + d.name
            function_name = d.name

            mod = importlib.import_module(module_path)
            func = getattr(mod, function_name)

            modules[d.name] = func

    # print(docs)

    stream_ollama_response(open('prompt.txt').read()+ '\n'.join(docs))

    cnt = True
    while cnt:
        response = stream_ollama_response(input("Input: "))

        super = re.search(r'<super>\s*(\{.*?\})\s*$', response, re.DOTALL)
        if super:
            try:
                process_agentic_command(json.loads(super.group(1)))
                
            except json.JSONDecodeError:
                print("MODEL PRODUCED BROKEN JSON")

        exit = re.search(r'<exit>', response, re.DOTALL)
        if exit:
            cnt = False


    with open('sessions/' + str(int(time.time())) + '.json', 'w') as file:
        file.write(json.dumps(message_history, indent=2))
