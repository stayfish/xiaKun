from nonebot import on_command
from nonebot.adapters import Event, Bot
from nonebot.permission import SUPERUSER

listener = on_command("list", permission=SUPERUSER)


async def get_friend_list(bot: Bot):
    list = await bot.get_friend_list()
    print(list)
    msg = []
    n = len(list)
    msg.append("共有{total}个好友\n".format(total=n-1))
    msg.append("-----------------\n")
    count = 1
    for friend in list:
        if friend['user_id'] == bot.self_id:
            pass
        message = ("好友 {n}\n"
                   "账号  : {uid}\n"
                   "用户名: {nickname}\n"
                   "备注  : {remark}\n"
                   "-----------------\n")
        message = message.format(
            n=count, uid=friend['user_id'], nickname=friend['nickname'], remark=friend['remark'])
        count = count + 1
        msg.append(message)
    return msg


@listener.handle()
async def send_list(bot: Bot, e: Event):
    msg = await get_friend_list(bot)
    await bot.send(
        event=e,
        message=msg
    )
