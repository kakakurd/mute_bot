import asyncio
import re
from telethon import TelegramClient, events

# Your credentials
api_id = 24428962
api_hash = '7ce956e625de207e3c07ee88e3748282'
bot_token = '7508364990:AAGhHqzzB9fFSyviMdyoGLHi_uKxfSgniGQ'

# Create a new event loop explicitly
asyncio.set_event_loop(asyncio.new_event_loop())

client = TelegramClient('mute-ali-bot', api_id, api_hash)

async def main():
    # Start the bot
    await client.start(bot_token=bot_token)

    # Listen for new messages
    @client.on(events.NewMessage())
    async def handler(event):
        text = event.raw_text or ''
        # Match either "ali" (English) or "عەلی" (Kurdish/Arabic)
        if re.search(r'(?i)\bali\b', text) or 'عەلی' in text:
            chat = await event.get_chat()
            sender = await event.get_sender()
            try:
                # Mute the user
                await client.edit_permissions(chat, sender, send_messages=False)
                await event.reply("بەخۆت عەلی ها، جاریکە جوونی نەدەی.")
            except Exception as e:
                print("Failed to mute. Make sure the bot is admin with restrict permission.", e)

    print("Bot is running... keep this window open.")
    await client.run_until_disconnected()

# Run the bot
asyncio.run(main())