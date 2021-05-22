#多线程
from threading import Thread #线程类

# def func():
#     for i in range(100):
#         print('func',i)
#
# if __name__ == '__main__':
#     t=Thread(target=func)#创建线程并给线程安排任务
#     t.start()#多线程状态为可以开始工作状态，具体执行时间由CPU决定
#
#     for i in range(100):
#         print('main',i)

# class MyThread(Thread):
#     def run(self):
#         for i in range(100):
#             print('child',i)
#
# if __name__ == '__main__':
#     t=MyThread()
#     t.start()
#     for i in range(100):
#         print('parent',i)

def func(name):
    for i in range(100):
        print(name,i)

if __name__ == '__main__':
    t1=Thread(target=func,args=('周杰伦',))#传递的参数必须为元组，只有一个参数时必须加逗号
    t1.start()

    t2 = Thread(target=func,args=('王力宏',))
    t2.start()
