## Ollama Server

This guide configures Ollama server for Ubuntu machines, specifically when using the Ubuntu instance as a remote accelerator.

### Instructions

1. **Log in to desired host.**
   
2. **Install Ollama:**
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

3. **Config Ollama:**
   ```sudo systemctl edit ollama.service```

   Add lines 3 & 4 to the file.

```
### Editing /etc/systemd/system/ollama.service.d/override.conf
### Anything between here and the comment below will become the contents of the drop-in file

[Service]
Environment="OLLAMA_HOST=0.0.0.0"
Environment="OLLAMA_KEEP_ALIVE=-1" # prevent deallocation (see bottom of this .md)

### Edits below this comment will be discarded


### /etc/systemd/system/ollama.service
# [Unit]
# Description=Ollama Service
# After=network-online.target
# 
# [Service]
# ExecStart=/usr/local/bin/ollama serve
# User=ollama
# Group=ollama
# Restart=always
# RestartSec=3
# Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
# 
# [Install]
# WantedBy=default.target
```

4. **Restart Ollama:**
   ```bash
   sudo systemctl daemon-reload && sudo systemctl restart ollama
   ```

5. **Verify:**
    ```
    % sudo lsof -i :11434
    COMMAND  PID     USER FD   TYPE DEVICE SIZE/OFF NODE NAME
    ollama  1408   ollama 3u  IPv6   7730      0t0  TCP *:11434 (LISTEN)
    ```

    ```*:11434``` is what to look for, it means Ollama is listening on all interfaces on port 11434

6. **Connect:**

    ```python
    from dotenv import load_dotenv

    load_dotenv()

    llm_host = os.getenv("LLM_HOST")
    llm_model = os.getenv("MODEL")

    ollama_server = ollama.Client(host=llm_host)
    stream = ollama_server.chat(model=llm_model, messages=message_history, stream=True)
    ```

    This is just an example that assumes you have something like ```LLM_HOST=http://192.168.X.X:11434``` in a .env file.

## Hotloading Models

Ollama naturally deallocates models after a short period of inactivity, and waiting for them to get loaded back into memory can be a significant time waste, so you can instruct Ollama to keep models loaded via:

```Environment="OLLAMA_KEEP_ALIVE=-1"``` in the ollama.service file.

Beware that if you are testing using multiple models on a remote server, you can quickly clog its memory!
