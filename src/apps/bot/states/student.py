from aiogram.fsm.state import State, StatesGroup


class StudentProfileStates(StatesGroup):
    """Student Profile State"""
    group_id = State()
    full_name = State()
    github_username = State()
    phone_number = State()
    confirm_profile = State()


