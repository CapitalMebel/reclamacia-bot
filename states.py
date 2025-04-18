from aiogram.fsm.state import StatesGroup, State

class Registration(StatesGroup):
    waiting_for_fop = State()
    waiting_for_phone = State()

class Complaint(StatesGroup):
    choosing_factory = State()
    entering_product_number = State()
    entering_order_number = State()
    entering_product_name_color = State()
    entering_reason = State()
    entering_part = State()
    entering_quantity = State()
    uploading_photos = State()