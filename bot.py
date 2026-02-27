import asyncio
from telegram import Bot

TOKEN = "8797113384:AAHVgv1dgPY_YUspuCPDT1n-ZihBCAsGRMM"

SOURCE_CHANNEL = -1002839275504  # your source
DESTINATION_CHANNELS = [
    -1003547480082,
    -1002907412341,
    -1002967800111,
    -1003132017414,
    -1003224337028
]

bot = Bot(token=TOKEN)

async def auto_post():
    last_message_id = 0

    while True:
        updates = await bot.get_updates()

        for update in updates:
            if update.channel_post and update.channel_post.chat.id == SOURCE_CHANNEL:
                message_id = update.channel_post.message_id

                if message_id > last_message_id:
                    for channel in DESTINATION_CHANNELS:
                        await bot.copy_message(
                            chat_id=channel,
                            from_chat_id=SOURCE_CHANNEL,
                            message_id=message_id
                        )

                    last_message_id = message_id

        await asyncio.sleep(30)

asyncio.run(auto_post())
