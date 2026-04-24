## Ollama Server - MacOS

This guide configures Ollama server for MacOS.

### Instructions

Run the following commands in your terminal:

1. **Install Ollama**:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Add Python package:** Run this command in your project directory
   ```bash
   uv add ollama
   ```

Ollama will automatically respond to chat requests made by a Python script.

## Hotloading Models

Ollama naturally deallocates models after a short period of inactivity, and waiting for them to get loaded back into memory can be a significant time waste, so you can instruct Ollama to keep models loaded via:

```launchctl setenv OLLAMA_KEEP_ALIVE -1``` run in the terminal.

**Note:** Running this command will keep loaded models in memory, to avoid system issues loaded models can be cleared by running ```killall Ollama```.
