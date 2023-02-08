from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment

from . import listener
from ..send import special as send_special, general as send_general
from .. import info
from .exception import GroupError
from .. import format


# 测试指令的指令选项
from nonebot import on_command
test = on_command(('test', 'option'))


@test.handle()
async def test_test(bot: Bot, e: Event):
    # msg = await send_special.get_friend_list(bot)
    await bot.send(
        event=e,
        message="get"
    )

# -----------------


@listener.list.handle()
async def send_list(bot: Bot, e: Event):
    msg = await send_special.get_friend_list(bot)
    await bot.send(
        event=e,
        message=msg
    )

    # 指令格式为 /urge @号码


@listener.group_urge.handle()
async def urge_group_member(bot: Bot, e: Event):
    [gid, list] = await info.get_qq(bot, e)
    # 检验是否是 at 格式
    try:
        cmd = e.get_message()[1]
        print("指令后的内容是: {str}".format(str=cmd))
        receiver = int(cmd.data['qq'])
        if receiver not in list:
            error = "用户不在群内! " + \
                "群用户有: {l}, ".format(l=list) + \
                "接收者为: {id}".format(id=receiver)
            raise GroupError(error)
    except (KeyError, IndexError) as e:
        error = "请输入正确的指令格式: \n" + format.urge
        print(e)
        await bot.send_group_msg(group_id=gid, message=error)
        return
    except GroupError as e:
        print(e)
        await bot.send_group_msg(group_id=gid, message=error)
        return

    if str(receiver) in format.superuser:
        warning = "不能骚扰机器人管理员"
        await bot.send_group_msg(group_id=gid, message=warning)
    else:
        friend_list = await info.get_friends_qq(bot, e)
        if receiver in friend_list:
            success = "私信成功"
            await bot.send_group_msg(group_id=gid, message=success)
            await send_general.spam(bot, receiver)
        else:
            msg = MessageSegment.image(
                "imgs/urge.webp")
            # await bot.send_group_msg(group_id=gid, message=msg)
            await bot.send_private_msg(userid=receiver, message=msg)
            msg = MessageSegment.at(user_id=receiver)
            await bot.send_group_msg(group_id=gid, message=msg)
