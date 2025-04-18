from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "📦 Подати рекламацію")
async def start_complaint(message: Message):
    from states import Complaint
    from aiogram.fsm.context import FSMContext
    state: FSMContext = message.bot.get("fsm_context")
    await message.answer("🔍 Оберіть фабрику (поки заглушка)...")
    await state.set_state(Complaint.choosing_factory)

@router.message(F.text == "👤 Додати менеджера")
async def add_manager(message: Message):
    await message.answer("📨 Ваш запит на додавання менеджера надіслано.")

