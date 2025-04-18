import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from handlers import start, main_menu, complaint_flow, photo_upload, add_manager

async def main():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        start.router,
        main_menu.router,
        complaint_flow.router,
        photo_upload.router,
        add_manager.router,
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())