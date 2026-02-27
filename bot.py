import asyncio
from telegram import Bot

BOT_TOKEN = "8797113384:AAHVgv1dgPY_YUspuCPDT1n-ZihBCAsGRMM"

SOURCE_CHANNEL = -1002839275504

DESTINATION_CHANNELS = [
    -1003547480082,
    -1002907412341,
    -1002967800111,
    -1003132017414,
    -1003224337028
]

bot = Bot(token=BOT_TOKEN)

async def auto_post():
    last_message_id = 0

    while True:
        updates = await bot.get_updates()

        new_messages = []

        for update in updates:
            if update.channel_post and update.channel_post.chat.id == SOURCE_CHANNEL:
                if update.channel_post.message_id > last_message_id:
                    new_messages.append(update.channel_post)

        new_messages = new_messages[-20:]

        for msg in new_messages:
            for channel in DESTINATION_CHANNELS:
                await bot.copy_message(
                    chat_id=channel,
                    from_chat_id=SOURCE_CHANNEL,
                    message_id=msg.message_id
                )

            last_message_id = msg.message_id

        print("Checked for new posts...")
        await asyncio.sleep(3600)

asyncio.run(auto_post())
