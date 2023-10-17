
import multiprocessing as mp
import time

stringD = "hello world"

def fun1(a):
    print("1"+a)

def fun2(a):
    print("2"+a)

def fun3(a):
    print("3"+a)

if __name__ == '__main__':
    p1 = mp.Process(target=fun1, args=(stringD,))
    p2 = mp.Process(target=fun2, args=(stringD,))
    p3 = mp.Process(target=fun3, args=(stringD,))
    
    p1.start()
    p2.start()
    p3.start()
    

