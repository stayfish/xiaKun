# xiaKun

## 简介

项目是基于 [nonebot2](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 创建，驱动器选择的是 `fastapi`，适配器是 `OneBot V11`

## 配置

在 .env 中的 `ENVIRONMENT` 项设置配置文件后缀，在配置文件中，可以如下设置：

```docs
LOG_LEVEL=DEBUG
HOST=127.0.0.1
PORT=8800
SUPERUSERS=["your admin number"]  # 配置 NoneBot 超级用户
NICKNAME=["kun"]  # 配置机器人的昵称
COMMAND_START=["/", "$", "!"]  # 配置命令起始字符
COMMAND_SEP=["."]  # 配置命令分割字符
LOG_LEVEL=DEBUG
FASTAPI_RELOAD=true
LOG_LEVEL=DEBUG
```

## 完成进度

- [x] 内置指令 `\echo`
- [x] 列出机器人的好友指令（管理员权限）`\list`
- [ ] 催促功能
  - [x] 发送默认的催促消息
  - [ ] 通过指令提供催促消息
- [ ] 群聊日程待办
- [ ] 备忘录功能
- [ ] 为所有包添加 `Config`

## 文档

文档可以参考 [onebot-11 api](https://github.com/botuniverse/onebot-11) 和 [nonebot2 docs](https://v2.nonebot.dev/)
