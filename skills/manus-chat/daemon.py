import asyncio
import json
import time
from aiohttp import web
from telethon import TelegramClient, events

api_id = 2040
api_hash = 'b18441a1ff607e10a989891a5462e627'
session_name = '/home/node/.openclaw/workspace/tg_manus'
target = '@manus_ai_agent_bot'
state_file = '/home/node/.openclaw/workspace/skills/manus-chat/state.json'

client = TelegramClient(session_name, api_id, api_hash)
state = {"latest_messages": {}}

def save_state():
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)

async def handle_send(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Invalid JSON"}, status=400)
        
    prompt = data.get('prompt')
    if not prompt:
        return web.json_response({"error": "No prompt provided"}, status=400)
    
    print(f"Sending prompt to Manus: {prompt[:50]}...")
    sent = await client.send_message(target, prompt)
    return web.json_response({"status": "sent", "message_id": sent.id})

async def init_app():
    app = web.Application()
    app.router.add_post('/send', handle_send)
    return app

async def main():
    await client.connect()
    print("Telegram socket connected.")
    
    @client.on(events.NewMessage(chats=target))
    async def handler(event):
        msg_id = str(event.message.id)
        state["latest_messages"][msg_id] = {
            "text": event.message.message,
            "timestamp": time.time(),
            "is_edit": False
        }
        save_state()
        print(f"New message from Manus (ID: {msg_id})")
            
    @client.on(events.MessageEdited(chats=target))
    async def edit_handler(event):
        msg_id = str(event.message.id)
        state["latest_messages"][msg_id] = {
            "text": event.message.message,
            "timestamp": time.time(),
            "is_edit": True
        }
        save_state()
        print(f"Manus edited message (ID: {msg_id})")

    runner = web.AppRunner(await init_app())
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 17171)
    await site.start()
    
    print("Manus TG IPC Daemon running on http://127.0.0.1:17171")
    save_state() # Initialize the file
    await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())