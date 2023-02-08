from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.adapters import Bot


# False 是有表情还是没有？
default_msg = MessageSegment.image("1.png")


async def spam(bot: Bot, uid: int, repeat=10, msg: Message = default_msg, escape=True):
    for i in range(repeat):
        await bot.send_private_msg(user_id=uid, message=msg, auto_escape=escape)
