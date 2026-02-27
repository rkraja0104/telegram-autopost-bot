import asyncio
from pyrogram import Client
import asyncio

TOKEN = "8797113384:AAHVgv1dgPY_YUspuCPDT1n-ZihBCAsGRMM"

SOURCE_CHANNEL = -1002839275504
DESTINATION_CHANNELS = [
    -1003547480082,
    -1002907412341,
    -1002967800111,
    -1003132017414,
    -1003224337028
]

bot = Client("my_bot", bot_token=TOKEN)

async def forward_posts():
    while True:
        async for message in bot.get_chat_history(SOURCE_CHANNEL, limit=20):
            for channel in DESTINATION_CHANNELS:
                try:
                    await bot.forward_message(
                        chat_id=channel,
                        from_chat_id=SOURCE_CHANNEL,
                        message_id=message.message_id
                    )
                except Exception as e:
                    print(e)

        await asyncio.sleep(3600)

async def main():
    async with bot:
        await forward_posts()

asyncio.run(main())
