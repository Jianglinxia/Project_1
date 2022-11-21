"""
web自动化：
Chrome
https://blog.csdn.net/zhoukeguai/article/details/113247342

cmd安装: pip -V
pip install selenium
查看：pip list
"""
import time

"""
代码        翻译（中间人）     浏览器
Python ----> 浏览器驱动---->  Chrome
selenium: Python的工具，三个部分
1）ide:录制脚本 --用的少
2）webdriver:库--提供对网页的各种操作+结合语言使用 --Python  Java  --重点
3）grid:分布式  --用的少

"""


#import selenium  #工具里的所有的内容都导入
from selenium import webdriver  #从selenium工具里导入webdriver库
# import time
driver=webdriver.Chrome()  #选择chrome这个浏览器，初始化driver ===可以跟浏览器进行沟通 建立会话 =session
driver.implicitly_wait(10)  #隐式等待，默认等待10s ==最多等到10s
# #1、打开一个网址
driver.get("http://erp.lemfix.com/login.html")   #打开一个网址
# #2、浏览器窗口最大化
# driver.maximize_window()
# #3、打开新页面
# time.sleep(2)
# driver.get("http://baidu.com")
# #4、向前  退后  刷新
# driver.back()   #退回上一个页面
# time.sleep(2)
# driver.forward()   #前进到下一个页面
# time.sleep(2)
# driver.refresh()   #刷新页面
# #5、退出
# driver.quit()  #关闭驱动 session关闭
#driver.close() #关闭当前窗口，不会退出会话

#以上浏览器的常规操作
'''基础知识：web页面=HTML+CSS+Javascript
html: 标签语言<标签名>值</标签名> ==呈现页面内容
css: 页面布局设置，字体颜色，字体大小
JS: 依据不同效果

元素的特征：根据页面设计，有些特征是唯一的 
id: 类比身份证号  ==仅限于当前页面 username  password
注意：如果id不是固定的话，就不能使用来定位!

xpath:
一、、绝对路径：/html/body/div/div/div[1]/a/b  ---根节点  顺序性、继承关系---易失效  ==不用，不稳定
二、、相对路径：只靠自己的特征定位  //开头  --加上我关心的标签名
1、标签名+属性 =//标签名[@属性名=属性值]
//input[@id="username"] --xpath表达方式
driver.find_element(By.XPATH,"//input[@id='username']")
2、层级属性定位：//div[@class='login-logo']//b
3、文本属性定位：//b[text()='柠檬ERP']
4、包含属性定位：//b[contains(text(),'柠檬')]

对页面进行相应的操作：
1、找元素:find_element(By.  ,"value)
2、点击:click()
3、传值:send_key("value")
4、获取页面文本:text
5、获取属性: get.attribute()


但凡是切换了页面，页面没有加载完，元素不显示   ====最好加个等待
三种等待方式：
1、强制等待：time.sleep()  ==没有完成等待时间  不往下执行
2、智能等待：
   隐式等待：可以设置一个等待时间，再这个等待时间没有结束之前元素找到了，不继续等待，而是继续执行下面的代码  --灵活
     注意: 一个session 里面只执行一次。  driver.implicitly_wait(10) 
   显示等待：expected_condition 

八大元素定位方式
三大等待
四大操作
'''

from selenium.webdriver.common.by import By
##废弃，老版本：driver.find_element_by_id("username").send_keys("test123")
driver.find_element(By.ID,"username").send_keys("test123")
driver.find_element(By.ID,"password").send_keys("123456")
driver.find_element(By.ID,"btnSubmit").click()

# driver.find_element(By.XPATH,"//input[@id='username']").send_keys("123")
# page_test=driver.find_element(By.XPATH,"//div[@class='login-logo']//b").text   #层级定位
# print(page_test)
# page_test=driver.find_element(By.XPATH,"//b[text()='柠檬ERP']").text   #文本属性定位
# print(page_test)
page_test=driver.find_element(By.XPATH,"//b[contains(text(),'柠檬')]").text
print(page_test)
page_tile=driver.title #获取页面标题
print("这个页面的标题是{}".format(page_tile))
if page_test=='柠檬ERP':
    print("这个页面的标题是：{}".format(page_test))
else:
    print("这个测试用例不通过")

#需等待
time.sleep(5)
login_user=driver.find_element(By.XPATH,"//p[text()='测试用户']").text
if login_user=='测试用户':
    print("这个登录的用户是：{}".format(login_user))
else:
    print("这条测试用例不通过")

#点击零售出库
driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
#点击搜索
# driver.find_element(By.ID,"searchNumber").send_keys("314")

'''
1、识别是否有子页面的方式：页面层级路径里出现iframe，就需要去切换iframe 才可以进行元素的定位
2、怎么去切换：
1）找到这个iframe元素，切换
 
切换三种方式：
1、通过id来切换
2、通过元素定位(xpath)来切换iframe
3、iframe下标：从0开始   html-页面=0，第一个宝宝-1 ，第二个宝宝-2
'''

# id=driver.find_element(By.XPATH,"//iframe[@id='tabpanel-15fba97e5f-frame']")
# driver.switch_to.frame('tabpanel-15fba97e5f-frame')   ---XXXX
# 通过找到这个元素 --获取id 属性
P_id=driver.find_element(By.XPATH,"//div[text()='零售出库']/..").get_attribute("id")   #/..找上一级（父级）
F_id=P_id+"-frame"
print(F_id)
# 1、通过id进行iframe的切换
driver.switch_to.frame(F_id)
driver.find_element(By.ID,"searchNumber").send_keys("246")
# 2、通过元素定位（xpath)来切换iframe   ------p2拓展
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='{}']".format(F_id)))
# driver.find_element(By.ID,"searchNumber").send_keys("314")
# 3、通过iframe的下标来切换
# driver.switch_to.frame(1)
# driver.find_element(By.ID,"searchNumber").send_keys("314")
#点击查询------XPATH  四种方法
driver.find_element(By.XPATH,"//span[@class='l-btn-text icon-search l-btn-icon-left']").click()
# driver.find_element(By.XPATH,"//span[text()='查询']").click()
# driver.find_element(By.XPATH,"//span[@class='l-btn-left']/span").click()
#driver.find_element(By.XPATH,"//*[@id='searchResetBtn']/span/span").click()

time.sleep(1)

#找到单据编号
num=driver.find_element(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
if "123" in num:
    print("搜索结果是正确的！")
else:
    print("用例测试不通过")



'''
from selenium.webdriver.common.by import By
selenium 定位元素代码
inputTag=driver.driver.find_element(By.ID,"value")   #利用ID查找
inputTag=driver.driver.find_element(By.CLASS_NAME,"value")   #利用类名查找
inputTag=driver.driver.find_element(By.NAME,"value")   #利用name属性查找
inputTag=driver.driver.find_element(By.TAG_NAME",value")   #利用标签名查找
inputTag=driver.driver.find_element(By.XPATH,"'value")   #利用xpath查找
inputTag=driver.driver.find_element(By.CSS_SELECTOR",value")   #利用CSS选择器查找
'''


