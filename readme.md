## LocalAgent

Local agentic AI demo

### Prerequisites

- Ollama (running ollama server on port 11434)
- Gemma4 / Qwen3.5 / Model optimized for agentic work
- uv

### Tools

Tools are used to expose functions to the LLM, which it can invoke through its output, Ollama models ouput tool call tokens that looks like this ```[ToolCall(function=Function(name='read', arguments={'fn': 'example.txt'}))]```

This project ships with some [tools](tools/), users can add their own .py's and exposing select functions using ```__all__```.

### Use

Ensure ollama server is already running!

> Recommended read: [ollama docs](docs/ollama-server.md)

Start the program with ```python main.py```. 
