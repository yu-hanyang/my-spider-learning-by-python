



async def func(): #async 表示这个函数是协程异步函数
    print('Hi ,I am seliya')




if __name__ == '__main__':
     g= func()#这个函数是协程异步函数，此时函数执行得到的是协程对象
     print(g)