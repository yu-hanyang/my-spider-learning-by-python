import re

#findall:匹配字符串中所有符合正则的内容，返回列表
lst = re.findall(r'\d+','我的电话是10000，我女朋友的电话是：10086')
print(lst)

print('------------------------------------------------------------------')

#findalliter：匹配字符串中所有符合正则的内容，返回迭代器 ,从迭代器中拿到内容需要.group
it = re.finditer(r'\d+','我的电话是10000，我女朋友的电话是：10086')
print(it)
print('-----')
for i in it:
    print(i)
    print(i.group())
print('-----')
