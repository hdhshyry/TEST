file = open("22.txt","w+")
def py(a,u):
    
    m=0
    for q in u:
         m=int(q)+m
    for w in a:
        file.write(f"{str(w)}\n")
        print (w)
    print(f"your total info is {m}")
    file.write(f"your total is {str(m)}\n")
i = int(input ("how many info do you want to add?   "))
O=[]
A=[]



for i in range(i):
    z = input("what s your name?   ")
    x=input("what kinda information do you want to add?  ")
    n=int(input(f"your {x}  is   : "))
    O.append(z)
    O.append(x)
    O.append(n)
    A.append(n)
py(a=O,u=A)







#.................................
# def p(c,b):
#     print(f'{c} s age is {b}.')
# p('ali',25)


#def name (enter)

# def p():
#     print("sss")
# p()
