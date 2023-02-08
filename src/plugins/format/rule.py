from nonebot.adapters import Event, Bot
from nonebot.adapters.onebot.v11 import Message


async def group_checker(e: Event):
    sid = e.get_session_id()
    return sid.startswith("group")


async def user_checker(e: Event):
    sid = e.get_session_id()
    return not sid.startswith("group")
