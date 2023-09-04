#
# contact = []
#
# def append():
#     name = input('vvedi imya')
#     if name in contact:
#         print('imya tam est')
#     else:
#         contact.append(name)
#         print(contact)
#         print(f'{name} dobavlen v spisok')
#
# def delet():
#     name = input('vvedi imya kotoroe xochesh udalit')
#     if name in contact:
#         contact.remove(name)
#         print(f'{name} uvolen')
#         print(contact)
#     else:
#         print('takogo imeni net')
#
# def change():
#     name = input('vvedi kogo xochesh zamenit')
#     if name in contact:
#         new_name = input('vvedi novoe imya')
#         contact[contact.index(name)] = new_name
#
#
#
#
#
#
#
# while True:
#     admin = int(input('vvedi svoy vibor 1-dobavit, 2-udalit, 3-zamenit'))
#     if admin == 1:
#         pass
#     elif admin == 2:
#         pass
#     elif admin == 3:
#         pass
#     else:
#         print("proverte dannie")









# LAMBDA
# a = lambda x:x**2
# print(a(10))
#
# x = lambda a:a**2
# print(x(12))


# x = [1,2,3,'4']
# a = map(lambda d:d*2,x)
# print(list(a))

# def decrement_list(nums):
#     o = list(map(lambda x:x-1, nums))
#     return o
# print(decrement_list([1,2,3,4,5]))

# FILTER
# x = [1,2,3,'4']
# a = filter(lambda d:d*2==4,x)
# print(list(a))
#
# x = ['Hello','Pavel']
# a = filter(lambda d:d=='Hello', x)
# print(list(a))
#
# x = ['pavel','jacky','jordan','77']
# a = list(filter(lambda x:'j' in x)
# print(list(a))

# x=[1,2,-4,-4,-8,-7,4,15,18,19,21,-98]
# y= list(filter(lambda x: x > 0,x))
# print(list(y))

# ls = [1,[2,[3,[4,[5,[6,[7,[8,[9]]]]]]]]]
# print(ls[1][1][1][1][1][1][1][1][0])
#
# dict = {0:{-2:{'3':{7:{'90':{15:{'12':{2:'hello'}}}}}}}}
# print(dict[0][-2]['3'][7]['90'][15]['12'][2])


# UROK_9 CLASS
# class User:
#     name = 'Jordan'
# print(User.name)

# class Car:
#     type = 'Bugatti'
#     color = 'White'
#     max_speed = 300
# print(Car.type, Car.color, Car.max_speed)

# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
# gentra = Car('chevrolet','black', 2021)
# cobalt = Car('ravon','white', 2023)
# print(gentra.model)
# print(cobalt.year)

# class Comment():
#     def __init__(self, name, text, like_comment = 0):
#         self.name = name
#         self.text = text
#         self.like_comment = like_comment
# instagram = Comment('shohjahon','good job',70)
# print(instagram.like_comment,instagram.name, instagram.text)
#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#     def stop(self):
#         print('mashina stop')
# gentra = Car('chevrolet','black', 2021)
# gentra.stop()



# HOMEWORK!!!!!!!!!!!!!!!!!!!!!!!
# class BankAccount():
#     def __init__(self, client_name, balance = 0):
#         self.client_name = client_name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f'deposit{amount} popolnen')
#     def cash(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f'snyali{amount} deneg')
#
#     def my_balance(self):
#         print(f'popolnen {self.client_name} , {self.balance}')
#
#
# # popolneniye
# account1 = BankAccount('Javlon', 500)
# account2 = BankAccount('Mirik', 300)
#
# account1.my_balance()
# account2.my_balance()
#
#
# # popolnit
# account2.deposit(500)
# account1.deposit(300)
#
# account1.cash(100)
# account2.cash(200)

# HOMEWORK
# class Username():
#     def __init__(self, name, mail, years, number):
#         self.name = name
#         self.mail = mail
#         self.years = years
#         self.number = number
#
#     def change_username(self, new_name, new_mail, new_years, new_number):
#         self.name= new_name
#         self.mail= new_mail
#         self.years= new_years
#         self.number= new_number
#
# admin = Username('Pavel', 'pasha_email', 19, 3366)
# admin.new_number('4455')
# admin.number


# LESSON10
# class School:
#     def make_sound(self,a):
#         print(a)
#
# class Teacher(School):
#     pass
# user = Teacher()
# print(user.make_sound('student'))

# class Car:
#     def __init__(self, model, color, year):
#         self.model= model
#         self.color= color
#         self.year = year
#
# class SuperCar(Car):
#     def __init__(self, model,color,year, sponsor):
#         super().__init__(model,color,year)
#         self.sponsor = sponsor

# class MyClass:
#     def __init__(self,value):
#         self.value = value
#     @classmethod
#     def from_string(cls,string):
#      return cls(int(string))
#
# my_obj= MyClass.from_string('99')
# print(type(my_obj.value))


# class Rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
# rectangle = Rectangle(4,5)
# rectangle.wigth = 6
# print(rectangle.area)
# rectangle.height = 7
# print(rectangle.area)

# class Worker():
#     def __init__(self, imya, doljnost ):
#         self.imya = imya
#         self.doljnost = doljnost
# class HR(Worker):
#     def __init__(self,imya,doljnost,password):
#
#         super().__init__(imya,doljnost)
#         self.password = password
#     def show_position(self, worker_name):
#      return worker_name.doljnost
# a= Worker('Jordan', 'director')
# b = HR('Pavel', 'HR', 111)
# print(b.show_position(a))
















