from study import study_6  #导入函数文件
from test_data import test_1   #导入测试数据 文件

from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)

#调用函数 ---1、先取参数  2、传参到函数调用里
#1、取参 ---字典取值
url=test_1.url['url'] #字典 取值url
user=test_1.login_date["username"]
pwd=test_1.login_date["password"]
s_key=test_1.s_key["s_key"]  #取值  搜索的 关键字
# print(url,user,pwd,s_key)

#2、函数的调用   传参
# 给函数定义了一个返回值 --调用的时候用一个变量接收返回值
result=study_6.search_key(driver=driver, url=url, username=user, password=pwd, s_key=s_key)
if s_key in result:
    print("搜索结果是正确的！")
else:
    print("用例测试不通过!")


