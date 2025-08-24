"""class student:
    def __init__(self,name,age,grade,headmaster,house):
        self.name=name
        self.age=age
        self.grade=grade
        self.headmaster=headmaster
        self.house=house
    def detales(self):
        print(f"name: {self.name} \nage: {self.age} \ngrade: {self.grade} \nheadmaster: {self.headmaster} \nhouse: {self.house} ")



s1=student("andy","12","c","lina","popcorn")
s2=student("anna","12","a","ella","popcorn")

s1.detales()"""


"""class fruits:
    def __init__(self, colour, shape):
        self.colour=colour
        self.shape=shape
    def detales(self):
        print(f"colour: {self.colour} \nshape: {self.shape}")

apple=fruits("red","circle")
banana=fruits("yellow","cylinder")

apple.detales()"""


#python inheritance

class person:
    def __init__(self,name,age,qualification):
        self.name=name
        self.age=age
        self.qualification=qualification

    def detales(self):
        print(f"age: {self.age} \nname: {self.name} \nqualification: {self.qualification}")

#childclass

class employee(person):
    def __init__(self,name,age,qualification,idnum,salary):
        person.__init__(self,name,age,qualification)
        self.idnum=idnum
        self.salary=salary

    def desplay(self):
        print((f"age: {self.age} \nname: {self.name} \nqualification: {self.qualification} \nid num: {self.idnum} \nsalary: {self.salary}"))

andy=employee("andy","22","good","29489203","10000")

andy.detales()
andy.desplay()