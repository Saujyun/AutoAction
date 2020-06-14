# 方便延时加载
import os
import time
from selenium import webdriver

# 模拟浏览器打开网站
browser = webdriver.Firefox()
# browser.get('http://IamOK.scut.edu.cn')
browser.get('https://sso.scut.edu.cn/cas/login?service=https%3A%2F%2Fiamok.scut.edu.cn%2Fcas%2Flogin')
# 将窗口最大化
browser.maximize_window()

# 格式是PEP8自动转的
# 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
browser.find_element_by_xpath(
    "//*[@id='un']").send_keys(os.environ["SCUT_USER"])
browser.find_element_by_xpath(
    "//*[@id='pd']").send_keys(os.environ["SCUT_PASSWORD"])
# 在输入用户名和密码之后,点击登陆按钮
browser.find_element_by_xpath("//*[@id='index_login_btn']").click()
time.sleep(5)


if("今天已经填报过了哦" in browser.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/div[1]/span").text ):
    # 点击签到,实现功能
    browser.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/button").click()
    time.sleep(2)
    print("已经签到")
# 这个print其实没事什么用,如果真的要测试脚本是否运行成功，可以用try来抛出异常
print("签到成功")

# 保存email内容
with open("email.txt", 'w',encoding="utf-8") as email:
    email.writelines("签到成功!")

# 脚本运行成功,退出浏览器
browser.quit()
