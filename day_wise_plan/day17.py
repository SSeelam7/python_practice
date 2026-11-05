
'''#Creating BankAccount class
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} Deposited")
        else:
            print("Invalid Amount")

    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.__balance:
                print(f"{amount} withdrawn from account")
                self.__balance -= amount

            else:
                print("Insufficient Account Balance")

        else:
            print("Invalid Amount")



    def get_balance(self):
        print(f"Account Balance {self.__balance}")

account = BankAccount("Sairam", 10000)

account.deposit(2500)
account.withdraw(3000)
account.withdraw(20000)
account.deposit(-500)
account.get_balance()

#Checking whether encapsulation working or not
account.__balance = 20000
account.get_balance()


#2:
class Student:

    def __init__(self,name, age, course):
        self.name = name
        self.__age = age
        self.course = course

    def get_age(self):
        print(self.__age)

    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative")
        elif age > 100:
            print("Sorry, Too old to register for class")
        else:
            self.__age = age


    def display_student(self):
        print(f"Student Name: {self.name}, Age: {self.__age}, Course: {self.course}")

student = Student("Rahul", 22, "Python")

student.display_student()

student.set_age(25)
student.display_student()

student.set_age(-5)
student.display_student()


#3:
class Product:
    def __init__(self,name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        if amount <= 0:
            print("Invalid Price")
        else:
            self.__price = amount


product = Product("laptop", 75000)
print(product.price)
product.price = 80000
print(product.price)
product.price = -5000
print(product.price)
product.price = 0.1
print(product.price)
product.price = 999999
print(product.price)
product.price = -100
print(product.price)




#4:
class Company:
    company = "TCS"

    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    def display(self):
        print(f"Name: {self.name}")
        print(f"Exp: {self.exp}")
        print(f"Company: {self.company}")
        print("----------------")


emp1 = Company("sairam", 5.9)
emp2 = Company("trinadh", 5.6)
emp3 = Company("ramesh", 5.0)

emp1.display()
emp2.display()
emp3.display()

Company.company = "CGI"

emp1.display()
emp2.display()
emp3.display()

#Obseraved the changes.


#5:
class Employee:
    employee_count = 0

    def __init__(self,name, exp):
        self.name = name
        self.exp = exp

        Employee.employee_count += 1

    @classmethod
    def no_of_employees(cls):
        print(cls.employee_count)


emp1 = Employee("sairam", 5.9)
emp2 = Employee("trinadh", 5.6)
emp3 = Employee("ramesh", 5.0)


Employee.no_of_employees()



#6:
class MathUtils:

    @staticmethod
    def is_even(number):
        if number % 2 == 0:
            print(f"{number} is Even Number")
        else:
            print(f"{number} is not Even Number")
            #intentianlly just ignoring other case, just to focus on staticmethod

    @staticmethod
    def is_prime(number):
        flag = 0

        for num in range(2,(number//2)+1):
            if number % num == 0:
                flag += 1
                break
        if flag == 0:
            print(f"{number} is PRIME")
        else:
            print(f"{number} is NOT PRIME")



    @staticmethod
    def calculate_percentage(value, total):
        percentage = (value/total) * 100
        print(f"{value} is {percentage} percent of {total}")


MathUtils.is_even(10)
MathUtils.is_prime(15)
MathUtils.is_prime(17)
MathUtils.calculate_percentage(45,50)



#7:
class CPU:

    def process(self):
        print("CPU Processing...")

class Computer:

    def start(self):
        print("Computer starting...")
        self.cpu = CPU()
        self.cpu.process()
        print("Computer started successfully")



computer = Computer()
computer.start()

'''
from encodings.punycode import selective_find


#8:

class Customer:

    def __init__(self, name, email):
        self.name = name
        self.email = email

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:

    def __init__(self, customer):
        self.products = []
        self.customer = customer

        def add_product(product):
            pass

        def calculate_total():
            pass

        def display_order():
            pass




