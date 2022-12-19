d=0
T=True
a1=[]
e=1
def zamin (a):   
    for i in range (a):
        i+=1
        if a%i==0:
            a1.append(i)
while T:
    try:
        x=int(input("num1 :"))
        b=int(input("num2 :"))
        zamin(x)
        # re2=zamin(b)
        # print(f"{re}     {re2}")
        T=False    
    except:
        T=True
        print("error")