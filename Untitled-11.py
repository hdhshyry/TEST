# a = {'korosh':13,'amir':14,'sorena':16,'milad':16,'hossein':16}
# b = input('what s your name?   :')
# a.keys{}
# # print(f"your age is :\t{a.get(b,'there is not your name in list')}")
# c = a.keys
# d= a.values
# print (a.keys)
a = {}
for i in range(2):
    b=input("what s your name ?   :")
    c = int(input("what s your age ?  :"))
    a[b]=c
print (a)
f = open('22.txt','w+')
for i in a :
    f.write(f"{str(i)}\n")
n=input("what s your name ?   :")
print(a.get(n))

