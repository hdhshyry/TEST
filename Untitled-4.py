a =  int (input ("enter number"))
b = 0
c = 0
d=0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
if a>999999999 :
    b = a/1000000000
    a=a&1000000000
    a = a/100000000
    a=a&100000000
elif a>99999999 :
    c = a/100000000
    a=a&100000000
elif a>9999999 :
    d=10000000
elif a>999999 :
    e =a/1000000
elif a>99999 :
    f=a/100000
elif a>9999 :
    g = a/1000
elif a>999 :
    h=a/1000
elif a>99 :
    i = a/100
elif a>9 :
    j = a/10
else :
    k = a
print(f"{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}")

    
