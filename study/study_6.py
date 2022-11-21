##完成任意整数序列相加 --range() -生产一个整数序列，里面全是数字，求里面所有数字的和
# def add_fun(num):
#     sum =0
#     num =int(input("input正数："))  #字符串
#     for i in range(num):
#         sum += i
#     print(sum)
# add_fun(100)

##
# def function_len(object):
#     # if type(object)==dict or type(object)==list or type(object)==str:
#     if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
#         leng=len(object)
#         if leng>=5:
#             print("True")
#         else:
#             print("False")
#     else:
#         print("数据类型不能计算长度！")  #容错性友好
# function_len((1,2,3,4))

'''
元素定位
'''
import time

from selenium.webdriver.common.by import By

'''
练习
'''
'''#登录
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://erp.lemfix.com/login.html")
driver.find_element(By.ID,"username").send_keys("test123")
driver.find_element(By.ID,"password").send_keys("123456")
driver.find_element(By.ID,"btnSubmit").click()

#切换了页面，页面没有加载完，元素不显示  ---加等待
# time.sleep(5) #强制等待
driver.implicitly_wait(10)  #隐式等待

#定位右侧菜单
driver.find_element(By.XPATH,"//span[text()='基本资料']").click()
# driver.find_element(By.XPATH,"//a[@title='基本资料']/span").click()
# driver.find_element(By.XPATH,"//*[@id='leftMenu']/ul/li[8]/a/span[1]").click()
# driver.find_element(By.XPATH,"//span[contains(text(),'资料')]").click()

#定位右侧二级菜单
driver.find_element(By.XPATH,"//span[text()='供应商信息']").click()

#定位筛选框
#获取当前页面的iframe的id
P_id=driver.find_element(By.XPATH,"//div[text()='供应商信息']/..").get_attribute("id")
F_id=P_id+'-frame'
print(F_id)
#切换iframe
driver.switch_to.frame(F_id)  #通过id
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='{}']".format(F_id)))  #通过XPATH
# driver.switch_to.frame(1)  #通过frame下标

#正常定位元素
#输入框输入
driver.find_element(By.ID,"searchSupplier").send_keys('1')
time.sleep(2)
#点击查询
driver.find_element(By.XPATH,"//span[@class='l-btn-text icon-search l-btn-icon-left']").click()
driver.find_element(By.XPATH,"//span[text()='查询']").click()
time.sleep(5)
#重置
driver.find_element(By.XPATH,"//span[text()='重置']").click()
time.sleep(5)

#前进、后退、刷新
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
'''
import time
def open_url(url,driver):  #打开网页
    driver.get(url)
    driver.maximize_window()

def login_page(username,password,driver):  # 参数 --参数化  --提高代码复用率
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "btnSubmit").click()

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)   #调用网页
    login_page(username,password,driver)  #调用登录页面

    driver.find_element(By.XPATH, "//span[text()='零售出库']").click()
    P_id = driver.find_element(By.XPATH, "//div[text()='零售出库']/..").get_attribute("id")  # /..找上一级（父级）
    F_id = P_id + "-frame"
    driver.switch_to.frame(1)

    driver.find_element(By.ID,"searchNumber").send_keys("246")
    driver.find_element(By.XPATH,"//span[text()='查询']").click()
    time.sleep(1)

    num = driver.find_element(By.XPATH, "//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num

