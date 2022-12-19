z=0
b=[]
A=[]
print("start")
a=int(input("How many people do you want to register their info  ?:"))
for i in range (a) :
    z = input("Enter your name  :")
    x =int(input("Enter you number  :"))
    A.append([z,x])
# print(A)
f = open ("21.txt","w+")
for i in A :
    f.write(f"{str(i)}\n")
file = open ("21.txt","r+")
for i in range (a) :
    z = str(f.readline())
    b.append(z)
    # e = s
    # 
print(b)
#m = input ('Which name do you look for  ?  :')
# for n in b :
#     if n==m :
#         print('your name exist')
#     else :
#          print ('your name doesn t exist')
