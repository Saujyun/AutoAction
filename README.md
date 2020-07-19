# [AutoAction](https://github.com/Saujyun/AutoAction)简介
    该github工程主要是为了解决疫情期间华工需要不断地申报自身健康而建立,工程中使用GitHub Action来实现每天自动打卡工作。
# 准备工作
    1.一个github账号
    2.一个163邮箱账号：用于发送签到成功邮件，推荐添加，为了方便验证是否签到成功（可选）
#	上手教程
由于github上无法查看图片，建议移步到csdn查看上手教程：[csdn](https://blog.csdn.net/police_1/article/details/106837694)

1.把代码clone到本地或者直接点击fork按钮将工程复制到你的仓库
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618170529885.png)
2.邮件SMTP配置，本文以配置163邮箱为例。点击开启按钮，开启smtp。然后点击新增授权码，按步骤最后会得到一串字符（授权码），将字符串复制，并把它放到第三步里面的MAIL_PASSWORD变量

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618182701545.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618182802385.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
 3.配置你的账号和密码。在工程的secrets里面放置你的账号和密码。同样的，如果你不需要发送邮件通知可以不添加邮件配置。（SCUT_PASSWORD和SCUT_USER两个变量名需要跟signinaction.yml代码里面的一致）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618173121361.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)

4.点击打开autoclick.py文件，并删除或者注释掉下面红框代码。
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618172029327.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618172541226.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618172155813.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
5.打开Action查看工作流
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618222752943.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
6.新建工作流main.yml文件，将原本.github/workflows/signinaction.yml文件代码复制到main.yml,复制过程中删除或者注释红框的代码（如果不想收到邮件通知，可以把下面的邮件发送代码删掉。如果不删，记得把里面的邮箱换成自己的邮箱账号。）复制完成之后，请把.github/workflows/signinaction.yml删掉，不然每天它都会运行一次。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200619094611775.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020061909494572.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020061909543129.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200619095721133.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
7.yml文件中设置了每天北京5：00、每次代码提交、仓库被star都会触发工作流
```
on:
  watch:
    types: started
  push:
  schedule:
    - cron: '0 21 * * *'
```
8.上面代码提交之后，会自动运行。同时你也可以点击star运行action
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618223210719.png)
9.运行情况
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020061822350874.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
10.若出现问题可以点击查看log信息![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618183751835.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618183704916.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
11.如果出现上图所示的selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document错误：可以尝试将autoclick.py第30行里面的

```
 time.sleep(10)改为 time.sleep(30)延长等待时间 
```

12.运行结束后，会有邮件发送
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200618223940995.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
13.之后要是不需要每天填报了，那进入setting-》action-》选择Disable Actions for this repository。该仓库的工作流将不再运行。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200619100121815.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BvbGljZV8x,size_16,color_FFFFFF,t_70)
参考链接：[GitHub Actions 入门教程](http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)
[GitHub Actions 教程：定时发送天气邮件](http://www.ruanyifeng.com/blog/2019/12/github_actions.html)
[Python实现自动签到脚本](https://blog.csdn.net/ydydyd00/article/details/80882183)
[手动触发 GitHub Actions 的几种方式](https://p3terx.com/archives/github-actions-manual-trigger.html)
[GitHub Actions 中 python 脚本获取仓库 secrets](https://blog.csdn.net/sculpta/article/details/106474324)
[Selenium2+python自动化46-js解决click失效问题](https://www.cnblogs.com/yoyoketang/p/6569226.html)
[GitHub action fork之后无法触发action](https://github.community/t/forked-repo-doesnt-trigger-action/16259)
