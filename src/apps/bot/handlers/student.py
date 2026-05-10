from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery

from ..callback import (
    RoleCbData
)
from ..keyboards import get_select_groups_ik

from apps.students.services import get_groups


student_private_router = Router()


@student_private_router.callback_query(
    RoleCbData.filter(F.role == "student")
)
async def show_groups(query: CallbackQuery, callback_data: RoleCbData, state: FSMContext):
    list_groups = await get_groups()
 
    await query.message.edit_text(
        text="<b>Siz qaysi toparda oqiysiz?</b>\n<i>(Ózińizge tiyisli topardi tańlań)</i>",
        reply_markup=get_select_groups_ik(list_groups),
        parse_mode="HTML"
    )
    await query.answer()
