## Ollama Server

This guide sets up ollama server access when using LLMs on Ubuntu machines.

### Instructions

1. Log in to desired ollama host

2. ```sudo systemctl edit ollama.service```

Add lines 3 & 4.

```
### Editing /etc/systemd/system/ollama.service.d/override.conf
### Anything between here and the comment below will become the contents of the drop-in file

[Service]
Environment="OLLAMA_HOST=0.0.0.0"

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

3. Restart ollama server

```
sudo systemctl daemon-reload && sudo systemctl restart ollama
```

4. Verify

```
% sudo lsof -i :11434
COMMAND  PID     USER FD   TYPE DEVICE SIZE/OFF NODE NAME
ollama  1408   ollama 3u  IPv6   7730      0t0  TCP *:11434 (LISTEN)
```

looks good! listening on all interfaces on port 11434.

now you can connect by setting LLM_HOST in a dotenv file
