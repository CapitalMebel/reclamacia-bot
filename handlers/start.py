from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Registration

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await message.answer("👋 Вітаємо, вкажіть, будь ласка, назву Вашого ФОП:")
    await state.set_state(Registration.waiting_for_fop)

@router.message(Registration.waiting_for_fop)
async def get_fop(message: Message, state: FSMContext):
    await state.update_data(fop=message.text)
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Поділитись номером", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("📞 Надішліть, будь ласка, номер телефону:", reply_markup=kb)
    await state.set_state(Registration.waiting_for_phone)

@router.message(Registration.waiting_for_phone, F.contact)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📦 Подати рекламацію")],
            [KeyboardButton(text="👤 Додати менеджера")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    await message.answer("✅ Реєстрацію завершено!
Оберіть дію нижче:", reply_markup=kb)
    await state.clear()