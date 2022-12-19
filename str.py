
class str :
    counter=0
    alph={"A":1,"B":2,"C":3,"D":4, "E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    al={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,"u":21,'v':22,"w":23,"x":24,"y":25,"z":26}
    d=[]
    ope=0
    x=0
    def __init__ (self,word,letter):
        self.word=word
        self.letter=letter
    def l (self):
        for i in list(self.word):
            str.counter+=1
            print(str.counter)
    def sp (self,q=1):
        for i in range (str.counter):
            str.d.append(a[q-1:q])
            q+=1
        print(str.d)
    def f(self):
        if self.letter in str.d:
            print(self.letter)
        else:
            print ("there isnt in it")
    def op (self):
        for i in self.word:
            if i in str.alph:
                str.ope=str.alph.keys(i)
                print(str.values(str.ope))
            else:
                str.x+=1
   
        
             
        
a=input()
b=input()
s=str(a,b)
s.l()
s.sp()
s.f()