# bot.py
import nonebot

nonebot.init(custom_config3="config on init")

config = nonebot.get_driver().config
config.custom_config3 = "changed after init"
config.custom_config4 = "new config after init"