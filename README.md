# [AutoAction](https://github.com/Saujyun/AutoAction)简介
    该github工程主要是为了解决疫情期间华工需要不断地申报自身健康而建立,工程中使用GitHub Action来实现每天自动打卡工作。
# 准备工作
    1.一个github账号
    2.一个163邮箱账号：用于发送签到成功邮件，推荐添加，为了方便验证是否签到成功（可选）
#	上手教程
1.把代码clone到本地或者直接点击fork按钮将工程复制到你的仓库
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618170529885.png)
2.邮件SMTP配置，本文以配置163邮箱为例。点击开启按钮，开启smtp。然后点击新增授权码，按步骤最后会得到一串字符（授权码），将字符串复制，并把它放到第三步里面的MAIL_PASSWORD变量

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618182701545.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618182802385.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
3.配置你的账号和密码。在工程的secrets里面放置你的账号和密码。同样的，如果你不需要发送邮件通知可以不添加邮件配置。（SCUT_PASSWORD和SCUT_USER两个变量名需要跟signinaction.yml代码里面的一致）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618173121361.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
4.打开.github/workflows/signinaction.yml文件,删除或者注释下面的代码（如果不想收到邮件通知，可以把下面的邮件发送代码删掉）记得把里面的邮箱换成自己的邮箱账号。同时，可以删除掉.github/workflows/weather.yml文件，该文件是直接从[阮一峰博客](http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)复制过来的每天自动发送城市天气邮件工作流。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618172029327.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618172155813.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618183430699.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
5.同样的，按照上面的方式打开autoclick.py文件，并删除或者注释掉下面红框代码。最后记得像上面一样提交。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618172541226.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
6.打开Action查看工作流
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618222752943.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618181215341.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
7.yml文件中设置了每天北京5：00、每次代码提交、仓库被star都会触发工作流
```
on:
  watch:
    types: started
  push:
  schedule:
    - cron: '0 21 * * *'
```
8.点击star运行action
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618223210719.png)
9.运行情况
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020061822350874.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
10.若出现问题可以点击查看log信息![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618183751835.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618183704916.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
11.运行结束后，会有邮件发送
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618223940995.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
参考链接：[GitHub Actions 入门教程](http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)
[GitHub Actions 教程：定时发送天气邮件](http://www.ruanyifeng.com/blog/2019/12/github_actions.html)
[Python实现自动签到脚本](https://blog.csdn.net/ydydyd00/article/details/80882183)
[手动触发 GitHub Actions 的几种方式](https://p3terx.com/archives/github-actions-manual-trigger.html)
[GitHub Actions 中 python 脚本获取仓库 secrets](https://blog.csdn.net/sculpta/article/details/106474324)
[Selenium2+python自动化46-js解决click失效问题](https://www.cnblogs.com/yoyoketang/p/6569226.html)
