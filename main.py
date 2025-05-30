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



#Abstraction

from abc import ABC, abstractmethod

class Father(ABC):

    num1 = 200
    num2 = 300

    @abstractmethod
    def add(self):
        res = self.num1 + self.num2
        print(f'The sum of {self.num1} and {self.num2} is {res}')

    def sub(self):
        res = self.num1 - self.num2
        print(f'The sub of {self.num1} and {self.num2} is {res}')

    def multi(self):
        res = self.num1 * self.num2
        print(f'The multiplication of {self.num1} and {self.num2} is {res}')

    def div(self):
        res = self.num1 // self.num2
        print(f'The division of {self.num1} and {self.num2} is {res}')


class Son(Father):
    def add(self):
        res = self.num1 + self.num2
        print(f'The sum of {self.num1} and {self.num2} is {res}')

son = Son()
son.add()



#Overloading

class Bangladesh:

    #using default params
    def dhaka(self, a, b=1, c=2, d=3):
        print(a+b+c+d)

    #variable length arguments
    def shabag(self, *abc):
        print(abc)


bd = Bangladesh()
bd.dhaka(10)
bd.dhaka(10, 10)
bd.dhaka(10, 10, 10)
bd.dhaka(10, 10, 10, 10)

bd.shabag("a")
bd.shabag("a", "b")
bd.shabag("a", "b", "c")
bd.shabag("a", "b", "c", "d")

#aoverall topics called polymorphism



#PART_03- static method

class Addition:

    x = 10
    y = 20

    @staticmethod
    def add():
        res = Addition.x + Addition.y
        print(f'The sum of {Addition.x} + {Addition.y} = {res}')

#no need to create object for static method
Addition.add()



#PART_04- access modifier
# public (call from anywhere)
# protected = _ (limited place)
# private = __ (no where)

class Family:

    Husband = 'Naim'
    _Son = 'XYZ'
    __Wife = 'Akhi'

    def fun1(self):
        print(self.Husband)
        print(self._Son)
        print(self.__Wife)

class RelativesFamliy:

    def fun2(self):
        print(self.Husband)
        print(self._son)
        #print(self.__Wife)#not accessible only accessible on it own class




family = Family()
print(family.Husband)
#print(family._Son)#Not Accessible
#print(self.__Wife)  # not accessible only accessible on it own class

"""

#PART_05- Encapsulation

class DBBL:

    __balance = 0

    def deposit(self, amount):

        if amount <= 0:
            print('Invalid amount for deposit.')

        else:
            self.__balance += amount
            print("Deposit Successful")


    def withdraw(self, amount):
        if amount <= 0 and amount <= self.__balance:
            print('Insufficient amount for withdraw.')

        else:
            self.__balance -= amount
            print("Withdraw Successful")


    def check_balance(self):
        return f'Remaining balance: {self.__balance}'


account = DBBL()
print(account.check_balance())

account.deposit(500)
print(account.check_balance())

account.withdraw(200)
print(account.check_balance())
