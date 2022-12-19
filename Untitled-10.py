b=[]
file = open ("21.txt","r+")
for i in range (3) :
    z = str(file.readline())
    b.append(z)
    print(b)