import threading
def a():
    for i in range(20):
        print("victory")
def b():
    for ii in  range(20):
        print ("you re loser,victory was a pashm.")
t=threading.Thread(target=a)
t2=threading.Thread(target=b)
t.start()
t2.start()