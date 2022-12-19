
import time
import threading
T=time.localtime()
print(T)
a=T.tm_year
d=T.tm_yday
e=T.tm_mon
rr=int(input("age?"))
print(rr)
def age(b=a,ww=rr):
    # z=int(input("how old are you ?"))
    z=ww
    b=b-z
    print(f"you are live since  {b} .")
def x (z=e,x=d,lll=rr):
    # n=int(input("how old are you ?"))
    n=lll
    l=int(input("what month did you born ?"))
    o=int(input("what day did ypu born ?"))
    u=n*365
    j=l*30
    o=o+j
    m=n*12
    u=u+x
    u=u-o
    m=m+z
    m=m-l
    print(f"you are live for {m} month and {u} day")
    #day is not exacly becase i dont know what day you borned
if __name__=='__main__':
    t=threading.Thread(target=age)
    t2=threading.Thread(target=x)
    t.start()
    t2.start()

