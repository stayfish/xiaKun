from nonebot import on_command
from nonebot import get_bot
from nonebot.adapters import Event, Bot

listener = on_command("list")


@listener.handle()
async def get_list_(bot: Bot, e: Event):
    await bot.send(
        event=e,
        message="list friends"
    )
