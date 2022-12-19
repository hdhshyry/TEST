dot=int(input("how many ??  :"))
dot=dot-1
a=[]
b=2
c=0
for i in range(dot):
    dot=dot-b
    if dot==0:
        print("possible")
    elif dot>1 :
        b=b+2
    elif dot<1:
        print("impossible") 

# for i in range (1000):
#     a.append(c)
#     b=b+2
#     c=c+b
# print(a)
# if dot in a:
#     print("possible")
# else:
#     print("impossible")

# for i in range(dot):

























