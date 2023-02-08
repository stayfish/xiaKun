from nonebot.adapters import Bot, Event

from ..format import output
output.import_succeeded(__name__)


async def get_qq(bot: Bot, e: Event):
    gid = e.get_session_id().split('_')[1]
    list = await bot.get_group_member_list(group_id=gid)
    qq_member_list = []
    for member in list:
        if member['user_id'] == bot.self_id:
            pass
        qq_member_list.append(member['user_id'])
    return [gid, qq_member_list]


async def get_friends_qq(bot: Bot, e: Event):
    list = await bot.get_friend_list()
    qq = [elem['user_id'] for elem in list]
    return qq
