from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Complaint

router = Router()

@router.message(Complaint.choosing_factory)
async def choose_factory(message: Message, state: FSMContext):
    await state.update_data(factory=message.text)
    if "требує номер виробу" in message.text.lower():
        await message.answer("📦 Будь ласка, вкажіть № виробу, зазначений на етикетці 📦")
        await state.set_state(Complaint.entering_product_number)
    else:
        await state.update_data(product_number=None)
        await message.answer("🔢 Вкажіть номер замовлення:")
        await state.set_state(Complaint.entering_order_number)

@router.message(Complaint.entering_product_number)
async def get_product_number(message: Message, state: FSMContext):
    await state.update_data(product_number=message.text)
    await message.answer("🔢 Вкажіть номер замовлення:")
    await state.set_state(Complaint.entering_order_number)

@router.message(Complaint.entering_order_number)
async def get_order_number(message: Message, state: FSMContext):
    await state.update_data(order_number=message.text)
    await message.answer("🖼 Вкажіть назву виробу та колір:")
    await state.set_state(Complaint.entering_product_name_color)

@router.message(Complaint.entering_product_name_color)
async def get_product_name(message: Message, state: FSMContext):
    await state.update_data(product_name=message.text)
    await message.answer("❓ Вкажіть причину рекламації:")
    await state.set_state(Complaint.entering_reason)

@router.message(Complaint.entering_reason)
async def get_reason(message: Message, state: FSMContext):
    await state.update_data(reason=message.text)
    await message.answer("🔩 Вкажіть назву деталі або номер за схемою:")
    await state.set_state(Complaint.entering_part)

@router.message(Complaint.entering_part)
async def get_part(message: Message, state: FSMContext):
    await state.update_data(part=message.text)
    await message.answer("🔢 Вкажіть кількість:")
    await state.set_state(Complaint.entering_quantity)

@router.message(Complaint.entering_quantity)
async def get_quantity(message: Message, state: FSMContext):
    await state.update_data(quantity=message.text)
   await message.answer("📸 Завантажте, будь ласка, фото у довільному порядку.\nПісля кожного фото зʼявляються кнопки:")
📸 Додати ще фото
✅ Надіслати на оформлення"
    )
    await state.set_state(Complaint.uploading_photos)
