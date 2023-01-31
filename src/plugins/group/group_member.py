from nonebot.adapters import Bot, Event
from nonebot import on_command
from .. import format
from ..contact import urge
from .exception import GroupError
from nonebot.adapters.onebot.v11 import MessageSegment


# 返回群号和群成员号


async def get_qq(bot: Bot, e: Event):
    gid = e.get_session_id().split('_')[1]
    list = await bot.get_group_member_list(group_id=gid)
    qq_member_list = []
    for member in list:
        if member['user_id'] == bot.self_id:
            pass
        qq_member_list.append(member['user_id'])
    return [gid, qq_member_list]


group_msg = on_command("urge", rule=format.group_checker)


# 指令格式为 /urge @号码
@group_msg.handle()
async def urge_group_member(bot: Bot, e: Event):
    # sid = e.get_session_id()
    # if sid.startswith("group") == False:
    #     return
    [gid, list] = await get_qq(bot, e)
    # 检验是否是 at 格式
    try:
        cmd = e.get_message()[1]
        print("输入的指令是: {str}".format(str=cmd))
        receiver = int(cmd.data['qq'])
    except (KeyError, IndexError) as e:
        error = "请输入正确的指令格式: \n" + format.Format.urge
        print(e)
        await bot.send_group_msg(group_id=gid, message=error)
    else:
        try:
            if receiver not in list:
                print(type(receiver))
                print(type(list[0]))
                error = "用户不在群内! " + \
                    "群用户有: {l}, ".format(l=list) + \
                    "接收者为: {id}".format(id=receiver)
                raise GroupError(error)
        except GroupError as e:
            print(e)
            await bot.send_group_msg(group_id=gid, message=error)
        else:
            if str(receiver) in format.superuser:
                warning = "不能骚扰机器人管理员"
                await bot.send_group_msg(group_id=gid, message=warning)
            else:
                friend_list = await bot.get_friend_list()
                friend_list = [elem['user_id'] for elem in friend_list]
                print(friend_list)
                if receiver in friend_list:
                    success = "私信成功"
                    await bot.send_group_msg(group_id=gid, message=success)
                    await urge.urge_user(bot, receiver)
                else:
                    msg = MessageSegment.image(
                        "urge.webp") + MessageSegment.at(user_id=receiver)
                    await bot.send_group_msg(group_id=gid, message=msg)
