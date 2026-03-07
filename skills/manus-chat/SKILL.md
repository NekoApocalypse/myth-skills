---
name: manus-chat
description: "Send non-blocking tasks to Manus AI Agent via your personal Telegram account. Usage: /manus-chat [prompt]. The agent will automatically dispatch a background Sub-Agent to wait for the final response and report back to you."
user-invocable: true
disable-model-invocation: false
---

# Manus Telegram Chat (Non-Blocking)

This skill sends requests to `@manus_ai_agent_bot` over an MTProto proxy daemon and leverages OpenClaw's background sub-agents to wait for the result so your main chat isn't blocked.

## Usage

```bash
# As the operator (via chat)
/manus-chat "your prompt here"
```

## How it works

1. The agent pings the local `manus_daemon.py` which instantly fires the message via Telegram.
2. The agent spawns a background `sessions_spawn` Sub-Agent.
3. The Sub-Agent loops `sleep 30` reading `/home/node/.openclaw/workspace/skills/manus-chat/state.json`.
4. Once it detects a non-placeholder reply from Manus, the Sub-Agent sends it back to your chat and terminates itself.