# name=input("请输入姓名：")
# gender=input("请输入性别：")
# age=input("请输入年龄：")
# print('*'*20)
# print('''name:%s
# gender:%s
# age:%s
# '''%(name,gender,age))
# print("""*****
# gender:{}
# age:{}
# name:{}""".format(gender,age,name))

# str1='hello,world!'
# #替换
# print(str1.replace("hello","hi"))
# #找起始位置
# print(str1.find("g"))
# print(str1.index("g"))

'''
常用的数据类型：列表（list）、元组、字典、集合
列表(list):[] ，元素之间用英文逗号隔开
1、元素可以是任意的数据类型：int flat bool str list  tuple...
2、取值：索引取值——类比字符串
取多个值:切片
拓展：列表的嵌套取值
3、列表的元素是可以改变的！  ---增加，修改，删除
4、列表的元素是可以重复的   ---统计元素的个数--count
5、len()  ---统计元素个数
'''

# list1 = [20, 3.14, True, "土木", "荷花", [1, 2, 3, 4]]  # 空列表
# print(list1[3:5])
# print(list1[5][1])
# # 增加
# list1.append("换蓝")  # 默认追加元素到列表的末尾
# list1.insert(5, "kingo")  # 指定位置进行元素的插入
# list1.extend(["十又", "bingo", "陌上花开", "大且"])  # 两个列表合并
# print(list1)
# # 删除
# list1.pop(0)  # 默认删除最后一个元素，也可以指定位置（索引）进行删除
# list1.remove(3.14)  # 指定元素本身进行删除
# # list1.clear()   # 清除所有元素
# print(list1)
# # 修改   --取值-重新赋值
# list1[4] = "Amiee"
# list1[0] = "方圆"
# print(list1)
# # 统计
# print(list1.count('方圆'))
# print(len(list1))


'''
元组：tuple,()
1、元素可以是任意的数据类型：int flat bool str list  tuple...
2、取值：索引取值——类比字符串
取多个值:切片
拓展：列表的嵌套取值
3、元组的元素是不可以改变的！！！！ 
4、元组的元素是可以重复的   ---统计元素的个数--count
5、len()  ---统计元素个数
6、list tuple ---拓展:数据类型转化
'''
# tuple1 = (20, 3.14, True, "土木", "荷花", [1, 2, 3, 4])
# # tuple1[-1]='小丑'  ---不可以
# print(tuple1.count(3.14))
##转化
# list1=list(tuple1)   # 把元素转化为列表
# list1[-1]='小丑'
# print(list1)
# tuple2=tuple(list1)


'''
字典：dict {}
1、元素：key:value （键值对）
2、场景：存储数据属性：人--名字 身高 体重
key: 1)不能是可以改变的数据类型（list，dict) --字符串；
     2）不能重复的，唯一的
value:可以是任意数据类型 --可以被改变==增删改
3、字典是没有顺序的！！! --不能是索引取值-   取值：通过key  取value
4、len() --长度
'''
# dict1 = {"name": "tan", "height": "173", "weight": "160"}  # 空字典
# print(dict1["height"])  # key --value
# print(dict1.get("weight"))  # key --value
# dict1["weight"] = "150"  # key存在，修改对应key的value
# print(dict1)
# # 增加
# dict1["age"] = 18  # key不存在，新增加键值对
# print(dict1)
# dict1.update({"city": "北京", "hobby": "学习python", "gender": "Boy"})  # 字典的合并
# # 删除
# dict1.pop("weight")  # 指定key删除 对应的键值对
# print(dict1)
# # del dict1   #变量存储 删除——对象不存在了
# # print(dict1)

'''
集合：set  {}，元素单个   --了解
1、无序
2、元素不可以重复 ——使用场景：去重
'''
# list2 = [11, 22, 11, 33, 11, 11]  # 去重
# set1=set(list2)   # set() --set2转换为集合
# print(set1)
# list3=list(set1)  # list() --set1转换为列表



'''
控制流：代码的执行顺序  --从上至下依次执行：判断 循环
判断：if 语法
if 条件： ---成立  ---冒号:缩进（四个空格=tab键）
    子代码（执行语言）
elif 条件：---成立
    执行语句（子代码）
else：可以没有
    执行语句（子代码）  
'''
money=int(input("请你输入你的余额："))  #input（）控制台输入--数据类型 --字符串
# money=500
if money>=500:
    print("买别墅")
elif money>=200:
    print("买栋楼")
elif money>=50:
    print("买车！")
else:
    print("滚去工作")


