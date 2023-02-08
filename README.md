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

## 使用

插件名为 xiaKun，在 xiaKun 目录下有若干子目录，子目录为：

|子目录|功能|
|-|-|
|handler|对特定事件做出响应，实现机器人 xiaKun 的功能|
|format|一些通用的规范，包括匹配规则，格式化的输出信息|
|info|获取数据|
|send|发特定的消息|

- 对于 handler 包，子目录为：

|子目录|功能|
|-|-|
|handler|事件响应的操作|
|listener|自定义事件的监听器|
|rule|自定义的一些检查规则|

- 对于 format 包，子目录为：

|子目录|功能|
|-|-|
|cmd|指令规范和一些常量|
|output|在终端输出 DEBUG 信息的函数|

- 对于 send 包，子目录为：

|子目录|功能|
|-|-|
|general|一些通用的发送|
|special|一些特定的发送|

## 完成进度

- [x] 内置指令 `\echo`
- [x] 列出机器人的好友指令（管理员权限）`\list`
- [ ] 催促功能
  - [x] 发送默认的催促消息
  - [ ] 通过指令提供催促消息
  - [ ] 对群聊中的非好友用户实现临时对话
- [ ] 群聊日程待办
- [ ] 备忘录功能
- [ ] 为所有包添加 `Config`

## 文档

文档可以参考 [onebot-11 api](https://github.com/botuniverse/onebot-11) 和 [nonebot2 docs](https://v2.nonebot.dev/)
