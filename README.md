# MyRSS

## Bilibili

1. 获取 bilibili 关注的 up 更新情况
2. 使用邮件将更新情况发送给自己

### 1 获取 bilibili 关注的 up 更新情况

1.1 登录 bilibili

实际操作中我们发现 up 主主页是可以不用登陆就可以查看的，因此如果简单实现的话就不需要登录。如果想要更方便的自动化运行就可以加入登录功能。
不管使用哪种方式，我们的配置文件可以考虑使用 json（yaml也行，后续可以添加上来）。

1.1.1 解析 json 配置文件  OK

- 没有配置文件时自动生成文件 OK

1.1.2 使用账号与密码登录 bilibili 并保存登录信息

1.2 查询关注列表

1.2.a 得到所有的已关注 up 的最新内容

1.2.b 与上次内容作比较，得到最新的没有看过的内容

### 2 使用邮件将更新情况发送给自己
