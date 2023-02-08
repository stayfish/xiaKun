from nonebot import on_command
from nonebot.permission import SUPERUSER

from . import rule


list = on_command("list", rule=rule.user_checker,
                  permission=SUPERUSER)

group_urge = on_command("urge", rule=rule.group_checker)
