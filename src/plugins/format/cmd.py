from nonebot.config import Config
import nonebot

driver = nonebot.get_driver()
cmd_prefix = driver.config.command_start
prefix = ' | '.join(cmd_prefix)
prefix = '[ ' + prefix + ' ]'

superuser = driver.config.superusers


class Format:
    urge: str = prefix + 'urge @<member>'
    list: str = prefix + 'list'
