# 笔记

## NoneBot2 启动的准备工作

1. 运行 `nonebot.init` 初始化函数，读取配置文件，初始化 NoneBot 和后端驱动
  ***todo***
2. 注册协议适配器，本次采用的是 ONEBOT 适配器，
3. 加载插件，本次采用的是读取 toml 文件

***一个坑：使用 go-cqhttp 时，如果多次登录可能会触发腾讯的安全机制。***
## onebot-11  API 的使用

***一个坑：CQ at 返回的 qq 号是字符串，而 get_group_member 得到的是整型***
autoescape 默认是不转义

### 消息

#### 格式

分为两种格式：字符串和数组

1. 字符串
   一条消息对应一个字符串。消息中的多媒体内容用 CQ 码表示，格式为 `[CA:功能名<,参数列表>]`，详见 [onebot-11/string.md at master · botuniverse/onebot-11 (github.com)](https://github.com/botuniverse/onebot-11/blob/master/message/string.md##CQ 码格式)
2. 数组：数组格式将消息表示为消息段的数组
   - 消息段
   - 消息段数组

#### 来源

经过测试，利用 `get_session_id` 获取得到的消息时，有如下格式：

|来源|格式|
|-|-|
|好友|qq 账号|
|群成员|grop_<群号>_<群成员账号>|

## 异步

[async 和 await](https://blog.csdn.net/qq_43380180/article/details/111573642)
[阻塞和非阻塞](https://segmentfault.com/a/1190000022478666)

