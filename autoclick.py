import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
#window电脑本地
# browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

# IamOK自动签到
def scut():
    browser.get('https://sso.scut.edu.cn/cas/login?service=https%3A%2F%2Fiamok.scut.edu.cn%2Fcas%2Flogin')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='un']").send_keys(os.environ['SCUT_USER'])
    browser.find_element_by_xpath(
        "//*[@id='pd']").send_keys(os.environ['SCUT_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@id='index_login_btn']").click()
    time.sleep(50)
    try:
        browser.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/button").click()
        print("IamOK签到成功")
        time.sleep(3)
        saveFile("IamOK签到成功！\n")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        # js = 'document.getElementById("btn").click();'
        # browser.execute_script(js)
        saveFile("IamOK签到代码存在异常"+str(e))



# 司徒云自动签到脚本
def situyun():
    browser.get('http://situcloud.xyz/auth/login')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='email']").send_keys(os.environ['SITUYUN_USER'])
    browser.find_element_by_xpath(
        "//*[@id='password']").send_keys(os.environ['SITUYUN_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@id='app']/section/div/div/div/div[2]/form/div/div[5]/button").click()
    time.sleep(10)
    try:
        if("明日再来" in browser.find_element_by_xpath("//*[@id='checkin-div']").text):
            saveFile("明日再来!")
        else:
            # browser.find_element_by_xpath("//*[@id='checkin-div']/a").send_keys(Keys.ENTER)
            js = 'document.getElementById("checkin-div").children[0].click();'
            browser.execute_script(js)
            print("司徒云打卡成功")
        time.sleep(3)
        saveFile("司徒云签到成功！")
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("司徒云签到代码存在异常"+str(e))

# n3ro自动签到脚本        
def n3ro():
    browser.get('https://n3ro.wtf/auth/login')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='email']").send_keys(os.environ['N3RO_USER'])
    browser.find_element_by_xpath(
        "//*[@id='passwd']").send_keys(os.environ['N3RO_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@id='login']").click()
    time.sleep(10)
    try:
        if("您今日已签到" in browser.find_element_by_xpath("//*[@class='btn btn-outline-default disabled']").text):
            saveFile("n3ro今日已签到！\n")
        else:  
            js = 'document.getElementById("checkin").click();'
            browser.execute_script(js)
            print("n3ro签到成功")
            saveFile("n3ro签到成功！\n")
        time.sleep(3)  
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("n3ro签到代码存在异常"+str(e)) 

# Jikess自动签到脚本
def jikess():
    browser.get('https://jikess.com/user/login.php')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='email']").send_keys(os.environ['JIKESS_USER'])
    browser.find_element_by_xpath(
        "//*[@id='passwd']").send_keys(os.environ['JIKESS_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@id='login']").click()
    time.sleep(10)
    try:
        
        if("不能签到" in browser.find_element_by_xpath("//*[@class='skin-blue']").text):
            saveFile("Jikess今日已签到！\n")
        else:  
            js = 'document.getElementById("checkin").click();'
            browser.execute_script(js)
            print("Jikess签到成功")
            saveFile("Jikess签到成功！")
        time.sleep(3)      
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("Jikess签到代码存在异常"+str(e)) 

# Jikess自动签到脚本
def jikess2():
    browser.get('https://jikess.com/user/login.php')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "//*[@id='email']").send_keys(os.environ['JIKESS_USER2'])
    browser.find_element_by_xpath(
        "//*[@id='passwd']").send_keys(os.environ['JIKESS_PASSWORD2'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@id='login']").click()
    time.sleep(10)
    try:
        
        if("不能签到" in browser.find_element_by_xpath("//*[@class='skin-blue']").text):
            saveFile("Jikess2今日已签到！\n")
        else:  
            js = 'document.getElementById("checkin").click();'
            browser.execute_script(js)
            print("Jikess2签到成功")
            saveFile("Jikess2签到成功！")
        time.sleep(3)      
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("Jikess2签到代码存在异常"+str(e)) 

# 写邮件
def saveFile(message):
    # 保存email内容
    with open("email.txt", 'a+', encoding="utf-8") as email:
        email.write(message+'\n')
        
if __name__ == '__main__':
    #scut()
    
    #jikess()
    jikess2()
    #n3ro()
    # 脚本运行成功,退出浏览器
    browser.quit()
