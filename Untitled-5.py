import random
a=random.randint(10,1000)
for i in range (5):
    b = int(input("bozorgtar az   :"))
    if a>b :
        print("yes")
    else :
        print("no")
    c = int(input("kochaktar az   :"))
    if a<c :
        print("yes")
    else :
        print("no")
z =int( input ("guess what is  the number  :"))
if z==a :
    print("you win ,")
else : 
    print("you lose ,")
    print(a)