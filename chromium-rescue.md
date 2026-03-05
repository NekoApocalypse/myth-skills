# Chromium Self-Heal

Your browser tool is failing because Chromium has crashed or stopped. Follow these steps to fix it. You are already inside the gateway container — run all commands directly.

## Step 1 — Diagnose

```bash
ps aux | grep chromium | grep -v grep
curl -s http://127.0.0.1:18800/json/version
```

If the first returns nothing and the second errors, Chromium is dead. Proceed.

## Step 2 — Clear stale lock files

```bash
rm -f \
  /home/node/.openclaw/browser/openclaw/user-data/SingletonLock \
  /home/node/.openclaw/browser/openclaw/user-data/SingletonCookie \
  /home/node/.openclaw/browser/openclaw/user-data/SingletonSocket
```

## Step 3 — Restart Chromium

```bash
node /app/openclaw.mjs browser start
```

Expected output: `🦞 browser [openclaw] running: true`

## Step 4 — Verify

```bash
curl -s http://127.0.0.1:18800/json/version
```

Expected: a JSON object with `"Browser": "Chrome/..."`. Browser tool is ready.

## If Step 3 fails

Clear the full user-data directory and try again:

```bash
rm -rf /home/node/.openclaw/browser/openclaw/user-data
node /app/openclaw.mjs browser start
```

If it still fails, escalate to the human operator — a container restart is needed.
