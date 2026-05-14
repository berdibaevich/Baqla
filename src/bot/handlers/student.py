from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery

from ..callback import (
    UserAction,
    RoleCbData,
    GroupCbData
)
from ..states import StudentProfileStates
from ..keyboards import get_select_groups_ik

from apps.students.services import get_groups
from utils import is_valid_full_name


student_private_router = Router()


@student_private_router.callback_query(
    RoleCbData.filter(F.role == "student")
)
async def show_groups(query: CallbackQuery, state: FSMContext):
    list_groups = await get_groups()
 
    last_message = await query.message.edit_text(
        text="<b>Siz qaysi toparda oqiysiz?</b>\n<i>(Ózińizge tiyisli topardi tańlań)</i>",
        reply_markup=get_select_groups_ik(list_groups),
        parse_mode="HTML"
    )
    await query.answer()

    data = await state.get_data()

    message_ids = data.get("message_ids", [])
    message_ids.append(last_message.message_id)
    await state.update_data(message_ids = message_ids)
    await state.set_state(StudentProfileStates.group_id)



@student_private_router.callback_query(
    GroupCbData.filter(
        F.action == UserAction.SELECT), 
        StudentProfileStates.group_id
)
async def handle_group_selection(query: CallbackQuery, callback_data: GroupCbData, state: FSMContext):
    await state.update_data(group_id = callback_data.id)
    await state.set_state(StudentProfileStates.full_name)

    await query.message.edit_text(
        text=(
            "<b>Endi toliq ati-familiyanizdi kirgiziń.</b>\n\n"
            "<b>Esletpe: Tek latin háriplerinen paydalaniń (Misali: Jetkerbay Kenesbayev).</b>"
        ),
        parse_mode="HTML"
    )
    await query.answer()


@student_private_router.message(StudentProfileStates.full_name)
async def handle_full_name(message: Message, state: FSMContext):
    full_name = message.text.strip()
    
    if not is_valid_full_name(full_name):
        # data = await state.get_data()

        last_message = await message.answer(
            (
                "<b>Atińiz yamasa familiyańizda qáte barǵa usaydi.</b>\n\n"
                "<b>Esletpe: Tek latin háriplerinen paydalaniń\nMisali: Jetkerbay Kenesbayev.</b>"
            ),
            parse_mode="HTML"
        )
        #await state.update_data(message_ids=[sent_msg.message_id])
        return

    await state.update_data(full_name=full_name)
    await state.set_state(StudentProfileStates.github_username)

    last_message = await message.answer(
        (f"Ájayip, <b>{full_name}</b>!\n\n"
        "Endi GitHub <b>Username</b> atińizdi kirgiziń:"),
        parse_mode="HTML"
    )

