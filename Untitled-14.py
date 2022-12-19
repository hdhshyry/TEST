import time 
# for i in range(3):
#     time.sleep(0.001)
#     print (time.localtime())
T=time.localtime()
# print (type(T))
# while range(50):
x=time.strftime("%y / %m / %d     %H : %M : %S ",T)
print(x)
print (T)

