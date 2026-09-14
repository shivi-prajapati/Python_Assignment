import pickle
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('hi my name is',self.name,'and i am',self.age,'years old')
p=Person('Shivi',22)
with open('demo.pkl','wb')as f:
    pickle.dump(p,f)
with open('demo.pkl','rb')as g:
    p=pickle.load(g)
    
p.display()