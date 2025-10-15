## LocalAgent

Local agentic AI demo

### Prerequisites

pip install -r requirements.txt

Need ollama installed and running ollama server on port 11434.

### Modules

Modules are used to add functions to the LLM, which it can invoke through its output. Any LLM that outputs "<super>" followed by a JSON command struct can use these modules. The LLM is made aware of which modules it has access to in a system prompt.

This project ships with models that allow the agent to read and write files on the local machine.

You can write your own modules by creating a new subdirectory in modules/, your subdirectory needs an __init__.py, a source file and a documentation file.

Documentation files are plain text, they should contain a simple yet comprehensive description of a module's functionality, and they should describe how to LLM should structure its invokation of the module and the format it can expect data to be returned in.

### Use

Ensure ollama server is already running!

Start the program with ```python3 main.py```, it may take a while, the system has to register all modules and download the language model if it is not already installed. And abliterated version of GPT OSS 20b is used by default (see footnotes).

### Footnotes

Some models like GPT OSS will refuse to work, because the notion of macros/super commands is considered dangerous.

Some small models like deepseek-r1:8b will generate <super> when not asked to, or will format incorrectly by appending a </super>. The closing super tag wont break the program, but the system prompt also doesn't instruct to use it.

A model finetuned specifically to interpret user requests as actions would probably be better suited for this project.
