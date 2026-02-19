---
name: manus
description: Create and manage AI agent tasks via Manus API. Manus is an autonomous AI agent that can browse the web, use tools, and deliver complete work products.
homepage: https://manus.im
user-invocable: true
disable-model-invocation: false
metadata:
  clawdbot:
    emoji: "🤖"
    primaryEnv: MANUS_API_KEY
    requires:
      bins: [curl, node]
      env: [MANUS_API_KEY]
---

# Manus AI Agent

Create tasks for Manus, an autonomous AI agent, and retrieve completed work products.

## Authentication

Set `MANUS_API_KEY` env var with your key from [manus.im](https://manus.im).

---

## Commands

All commands execute the bundled `manus.sh` script.

> **Note:** Replace `{baseDir}` with the actual path to this skill directory (e.g., `/app/skills/myth/manus` or `/home/node/.openclaw/workspace/skills/manus`).

### Create a Task

```bash
{baseDir}/scripts/manus.sh create "Your task description here"
{baseDir}/scripts/manus.sh create "Deep research on topic" manus-1.6-max
```

Profiles: `manus-1.6` (default), `manus-1.6-lite` (fast), `manus-1.6-max` (thorough).

### Check Status

```bash
{baseDir}/scripts/manus.sh status <task_id>
```

Returns: `pending`, `running`, `completed`, or `failed`.

### Wait for Completion

```bash
{baseDir}/scripts/manus.sh wait <task_id>
{baseDir}/scripts/manus.sh wait <task_id> 300  # custom timeout in seconds
```

Polls until task completes or times out (default: 600s).

### Get Task Details

```bash
{baseDir}/scripts/manus.sh get <task_id>
```

Returns full task JSON including status and output.

### List Output Files

```bash
{baseDir}/scripts/manus.sh files <task_id>
```

Shows filename and download URL for each output file.

### Download Output Files

```bash
{baseDir}/scripts/manus.sh download <task_id>
{baseDir}/scripts/manus.sh download <task_id> ./output-folder
```

Downloads all output files to the specified directory (default: current directory).

### List Tasks

```bash
{baseDir}/scripts/manus.sh list
```

---

## Typical Workflow

1. **Create task**: `{baseDir}/scripts/manus.sh create "your prompt"`
2. **Wait for completion**: `{baseDir}/scripts/manus.sh wait <task_id>`
3. **Download results**: `{baseDir}/scripts/manus.sh download <task_id>`

---

## Security & Permissions

**What this skill does:**
- Sends task prompts to the Manus API at `api.manus.ai`
- Polls for task completion and downloads output files from Manus CDN
- API key is sent only in the `API_KEY` header to `api.manus.ai`

**Bundled scripts:** `scripts/manus.sh` (Bash) + `scripts/manus.cjs` (Node.js)

Review `scripts/manus.cjs` before first use to verify behavior.
