from aiogram import Router
from aiogram.types import Message
from aiogram.filters.text import Text

router = Router()

@router.message(Text("📦 Подати рекламацію"))
async def start_complaint(message: Message):
    from states import Complaint
    from aiogram.fsm.context import FSMContext
    state: FSMContext = message.bot.get("fsm_context")
    await message.answer("🔍 Оберіть фабрику (поки заглушка)...")
    await state.set_state(Complaint.choosing_factory)

@router.message(Text("👤 Додати менеджера"))
async def add_manager(message: Message):
    await message.answer("📨 Ваш запит на додавання менеджера надіслано.")
    # Заглушка: реализация отправки уведомления в группу будет в telegram_topics.py
