import json 
# l=[1,2,3,4,5]
# with open('demo.json','w')as f:
#     json.dump(l,f)

# dict1={
#     'name':'nitish',
#     'gender':'male',
#     'age':35
# }
# with open('demo.json','w')as f:
#     json.dump(dict1,f,indent=3)

# with open('demo.json','r')as f:
#     print(json.load(f))

# t=(565,245,234,1235)
# with open('demo.json','w') as f:
#     json.dump(t,f)

# class Person:
#     def __init__(self,name,gender,age):
#         self.name=name
#         self.gender=gender
#         self.age=age
# def show_object(person):
#     if isinstance(person,Person):
#         return "{} age-->{} gender-->{}".format(person.name,person.age,person.gender) #in the form of str
# person=Person('shivi prajapati','female',22)
# with open('demo.json','w')as f:
#     json.dump(person,f,default=show_object)

class Person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
def show_object(person):
    if isinstance(person,Person):
        return {'name':person.name,'age':person.age,'gender':person.gender} #in the form of dict
person=Person('shivi prajapati','female',22)
with open('demo.json','w')as f:
    json.dump(person,f,default=show_object,indent=3)