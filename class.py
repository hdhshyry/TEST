class worker :
    cost=0
    salary1={"worker":30,"workman":50,"boss":100}
    def __init__(self,name,age,code,work,phone):
        self.name=name
        self.age=age
        self.code=code
        self.work=work
        self.phone=phone
    def info (self) :
        print(self.name)
        print(self.age)
        print(self.code)
        print(self.work)
        print(self.phone) 
    def salary(self,t1,t2):
        worker.cost=t1*worker.salary1.get(self.work)+t2*(worker.salary1.get(self.work)+10)
        return worker.cost       
w=worker("ali",30,6484613548,"boss",4645561561)
w.info()
# w.salary()
print(w.salary(100,20))