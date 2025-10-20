import ollama
import os
import json
import re
import time
import importlib
from dotenv import load_dotenv

load_dotenv()

llm_host = os.getenv("LLM_HOST")
message_history = []
modules = {}


def process_agentic_command(cmd: dict):
    effect = modules[cmd["cmd"]](*cmd["args"])

    if effect is None:
        return {}
    else:
        # have faith that user modules return the format in the docs, or that
        # the llm can interpret it
        return {"return": effect}


def stream_ollama_response(
        prompt: str, model: str = "huihui_ai/gpt-oss-abliterated:20b"):
    message_history.append({'role': 'user', 'content': prompt})
    ollama_server = ollama.Client(host=llm_host)
    stream = ollama_server.chat(
        model=model,
        messages=message_history,
        stream=True)

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
            docs.append(open('modules/' + d.name + '/docs.txt').read())

            # dynamically importing modules - assume module repo has same name
            # as function - not suitable long term
            module_path = "modules." + d.name + "." + d.name
            function_name = d.name

            mod = importlib.import_module(module_path)
            func = getattr(mod, function_name)

            modules[d.name] = func

    # print(docs)

    stream_ollama_response(open('prompt.txt').read() + '\n'.join(docs))

    cnt = True
    while cnt:
        response = stream_ollama_response(input("Input: "))

        super = re.search(r'SUPER\s*(\{.*?\})\s*$', response, re.DOTALL)
        if super:
            try:
                process_agentic_command(json.loads(super.group(1)))

            except json.JSONDecodeError:
                print("MODEL PRODUCED BROKEN JSON")

        exit = re.search(r'EXIT', response, re.DOTALL)
        if exit:
            cnt = False

    with open('sessions/' + str(int(time.time())) + '.json', 'w') as file:
        file.write(json.dumps(message_history, indent=2))
