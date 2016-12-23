from functools import reduce
import math
import matplotlib.pyplot as plt
import numpy as np

#1
def summa1(list1):
    a=0
    for b in list:
        a+=b
    return(a)

def summa2(list):
    a=0
    b=0
    while b<len(list):
        a+=list[b]
        b+=1
    return(a)

def summa3(list):
    if len(list)==1:
        return list[0]
    return list[-1]+srec(list[:-1])


#2
def steptwo(N):
    b=0
    c=1
    while c<=N:
        r=[b,c]
        c*=2
        b+=1
    return r

#3
 def mid(list0):
    a = len(list0)
    return reduce(lambda x, y: x + y, list0) / float(a)

#4
def fib(N):
    q=0
    m=1
    b=2
    while m<N:
        m,q,b=m,q+m,b+1
    if m==N:
        print b
  else:
      print -1

#5
def fact(N):
    if N==0:
        return 1
     res=N*fact(N-1)
     return res
#6
 def zamena(list0):
    m = 0
    q = 0
    k = len(list0)
    for i in range(m):
        if list0[i] == min(list0):
            q = i
        if list0[i] == max(list0):
            k = i
    list0[q], list0[k] = list0[k], list0[q]
    return list0

#7

 def ro(x1, x2, y1, y2):
         r =((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
         return r

#8   
        def graf(a, b):
   
    g = 3.711
    m = b * math.pi / 180
    t1 = 1
    t2 = 1
    while t2 > 0:
        t2 = a * math.sin(m) * t1 - (g * t1 ** 2) / 2
        t1 += 0.01
    t = np.arange(0, t1, 0.01)
    s = a * math.cos(m) * t
    h = (a * math.sin(m) * t - (g * t ** 2) / 2)
    plt.plot(s, h)
    plt.axis('equal')
    plt.xlabel(r'$S$')
    plt.ylabel(r'$H$')
    plt.title(r'$Speed$ $on$ $Mars$')
    plt.grid(True)
    plt.show()
