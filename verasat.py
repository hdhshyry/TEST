class fl :
    counter=0
    z=[]
    word="MAMmad"
    letter="m"
    def l ():
        for i in list(fl.word):
            fl.counter+=1
            fl.z.append(i)
        print(fl.counter)
    def f():
        if fl.letter in fl.z:
            print("true")
        else:
            print ("false")
class so (fl):
    d=[]
    alph={"A":"a","B":"b","C":'c',"D":'d',"E":'e',"F":'f',"G":'g',"H":'h',"I":'i',"J":'j',"K":'k',"L":'l',"M":'m',"N":'n',"O":'o',"P":'p',"Q":'q',"R":'r',"S":'s',"T":'t',"U":'u',"V":'v',"W":"w","X":"x","Y":"y","Z":"z"}
    counter=0
    def sp (q=1):
        for i in range (s.counter):
            so.d.append(s.word[q-1:q])
            q+=1
        print(so.d)
    def op ():
        for i in so.d:
            if i in so.alph:
                print(so.alph.get(i),end='')
            else:
                print(i,end='')
        

s=fl
s.l()
s.f()
w=so
w.sp()
w.op()
