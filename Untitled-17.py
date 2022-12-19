
a=input('what s your word?')
d=[]
x=0
q=1
len1=len(a)
for i in range (len(a)):
    d.append(a[q-1:q])
    q+=1
d.sort
# for i in  a.split():
# d.append(a.split())
print(d)
print(d[-1])

# ........--
# d=[]
# e=0
# for i in range (20):
#     a.append(i+1)
#     b.append(i*c)
# for z in range(20):
#     d.append(a[e])
#     d.append(b[e])
#     e+=1
# print(d)
