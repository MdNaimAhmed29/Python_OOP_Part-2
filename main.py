"""
PART 01

class Profile:
    name = "Naim" #class variable
    age = 30

    def about(self): #class method
        print(f'My name is {self.name} and I am {self.age} years old')

    #def __init__(self): #constructor without params (Auto Executed, fixed name, can't return)
       # print('Auto Executed')

   # def __init__(self,num1,num2): #constructor with params (Auto Executed, fixed name, can't return)
       # sum = num1 + num2
        #print(f'The sum of {num1} and {num2} is {sum}')

    #def __init__(self,num1,num2,ageValue): #constructor can change class variable value
        #sum = num1 + num2
        #print(f'The sum of {num1} and {num2} is {sum}')

        #self.age = ageValue

    def __init__(self,num1,num2,ageValue, dateOfBirthValue): #constructor can produce class variables(Instance Variable)
        sum = num1 + num2
        print(f'The sum of {num1} and {num2} is {sum}')

        self.age = ageValue
        self.dateOfBirth = dateOfBirthValue

profile = Profile(10, 40, 25, "25-08-1995")
profile.about()
print(profile.dateOfBirth)

"""


#PART 02- inheritance
""" 
class Father:

    x = 10
    y = 20

    def add(self):
        sum = self.x + self.y
        print(f'The sum of {self.x} and {self.y} is {sum}')


class Mother:
    a = 30
    b = 20

    def sub(self):
        result = self.a - self.b
        print(f'The sub of {self.a} and {self.b} is {result}')


class Son(Father): #single inheritance
    pass


#inherited from father
son = Son()
son.add()

father = Father()
father.add()

class Student(Father, Mother): #multiple inheritance
    pass

#inherited from father and mother both
student = Student()
student.add()
student.sub()

mother = Mother()
mother.sub()


#multilevel inheritance

class GrandFather:
    x = 10



class Father(GrandFather):
    pass


class Son(Father):
    pass


grandFather = GrandFather()
father = Father()
son = Son()

print(grandFather.x)
print(father.x)
print(son.x)



#override
class GrandFather:
    x = 10



class Father(GrandFather):
    def vote(self):
        print("It is 700000")

class Son(Father):
    def vote(self): #overriding
        print("stole vote")


grandFather = GrandFather()
father = Father()
son = Son()
father.vote()
son.vote()

print(grandFather.x)
print(father.x)
print(son.x)

"""

#Abstraction

class Father:
    def vote(self):
        print("It is 700000")

class Son(Father):
    def vote(self):
        print("stole vote")