import aiohttp
from config import MANAGER_GROUP_USERNAME

async def send_to_telegram_group(bot, fop_name, summary, photo_ids):
    try:
        chat = await bot.get_chat(MANAGER_GROUP_USERNAME)
        forum_topics = await bot.get_forum_topic_list(chat.id)

        topic_id = None
        for topic in forum_topics:
            if topic.name == fop_name:
                topic_id = topic.message_thread_id
                break

        if topic_id is None:
            msg = await bot.send_message(chat.id, f"🧾 Рекламація від {fop_name}", message_thread_id=None)
            topic_id = msg.message_thread_id

        await bot.send_message(chat.id, summary, message_thread_id=topic_id)

        for photo_id in photo_ids:
            await bot.send_photo(chat.id, photo=photo_id, message_thread_id=topic_id)

    except Exception as e:
        print("❌ Error sending to Telegram group:", e)