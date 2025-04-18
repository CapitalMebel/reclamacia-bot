from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from states import Complaint
from utils import build_summary
from services.google_sheets import append_to_google_sheet
from services.telegram_topics import send_to_telegram_group

router = Router()
photo_storage = {}

@router.message(Complaint.uploading_photos, F.photo)
async def receive_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    fop = data.get("fop", "Клієнт")
    photos = photo_storage.setdefault(fop, [])
    photos.append(message.photo[-1].file_id)

    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📸 Додати ще фото")],
            [KeyboardButton(text="✅ Надіслати на оформлення")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    await message.answer("Фото збережено. Оберіть дію:", reply_markup=kb)

@router.message(Complaint.uploading_photos, F.text == "✅ Надіслати на оформлення")
async def finalize(message: Message, state: FSMContext):
    data = await state.get_data()
    fop = data.get("fop", "Клієнт")
    summary = build_summary(data)
    
    # Google Sheet
    try:
        append_to_google_sheet(data)
    except Exception as e:
        await message.answer("⚠️ Не вдалося зберегти до Google Таблиці")

    # Telegram Group
    try:
        await send_to_telegram_group(message.bot, fop, summary, photo_storage.get(fop, []))
    except Exception as e:
        await message.answer("⚠️ Не вдалося надіслати до групи менеджерів")

    await message.answer(summary)
    await state.clear()