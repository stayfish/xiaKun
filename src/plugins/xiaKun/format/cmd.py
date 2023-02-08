from nonebot.config import Config
import nonebot

driver = nonebot.get_driver()
cmd_prefix = driver.config.command_start
prefix = ' | '.join(cmd_prefix)
prefix = '[ ' + prefix + ' ]'

superuser = driver.config.superusers


instr_urge = prefix + 'urge @<member>'
instr_list = prefix + 'list'
