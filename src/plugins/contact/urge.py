from nonebot.adapters import Event, Bot
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Message, MessageSegment

bomb = 10
default_msg = MessageSegment.image("urge.webp") + MessageSegment.shake()


# False 是有表情还是没有？
async def urge_user(bot: Bot, uid: int, msg: Message = default_msg, escape=True):
    for i in range(bomb):
        await bot.send_private_msg(user_id=uid, message=msg, auto_escape=escape)
