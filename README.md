# xiaKun

## 简介

项目是基于 `nonebot` 和 `go-cqhttp` 创建，驱动器选择的是 `fastapi`，适配器是 `OneBot V11` 
可以用 host:port/go-cqhttp 进行可视化的管理账号

## 完成进度

- [x] 内置指令 `\echo`
- [x] 列出机器人的好友指令（管理员权限）`\list`
- [ ] 催促功能
  - [x] 发送默认的催促消息
  - [ ] 通过指令提供催促消息
- [ ] 群聊日程待办
- [ ] 备忘录功能

## How to start

1. generate project using `nb create` .
2. create your plugin using `nb plugin create` .
3. writing your plugins under `src/plugins` folder.
4. run your bot using `nb run --reload` .

## Documentation

See [Docs](https://v2.nonebot.dev/)
