
# # class Student:
# #     def __init__(self, name, age, grade):
# #         self.name = name
# #         self.age = age
# #         self.grade = grade


# #     def get_info(self):
# #         return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
# # student1=Student('Alex', 11, 10) 
# # student1.get_info()
# # print(student1.get_info())
    
# # class Rectangle:
# #     def __init__(self, width, height):
# #             self.width = width
# #             self.height = height
            
            
# #     def s(self):
# #         return self.width * self.height

# #     def p(self):
# #         return 2 * (self.width + self.height)
    
# # rect = Rectangle(5, 4)
# # print("Площа:", rect.s())
# # print("Периметр:", rect.p())
    
    
# # from datetime import datetime

# # class Car:
# #     def __init__(self, brand, model, year):
# #         self.brand = brand
# #         self.model = model
# #         self.year = year

# #     def get_age(self):
# #         current_year = datetime.now().year
# #         return current_year - self.year
# # my_car = Car("Ferrari", "F40", 2014)

# # print(f"вік автомобіля: {my_car.brand} {my_car.model}: {my_car.get_age()} років")

# # class Book:
# #     def __init__(self, title, author, pages):
# #         self.title = title
# #         self.author = author
# #         self.pages = pages

# #     def is_big(self):
# #         return self.pages > 300  


# # book1 = Book("Гаррі Поттер", "Дж. К. Роулінг", 350)
# # book2 = Book("інша", "Автор ", 120)


# # print(f"{book1.title} велика книга? {book1.is_big()}")
# # print(f"{book2.title} велика книга? {book2.is_big()}")

# # import math

# # class Circle:
# #     def __init__(self, radius):
# #         self.radius = radius

# #     def plowa(self):
# #         return math.pi * (self.radius ** 2)  

# #     def dovjina(self):
# #         return 2 * math.pi * self.radius  

# # circle = Circle(11)

# # print(f"Радіус: {circle.radius}")
# # print(f"Площа кола: {circle.plowa():.2f}")                       #AI
# # print(f"Довжина кола: {circle.dovjina():.2f}")

# class Bankaaccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#         balance=0

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Внесено: {amount}. Новий баланс: {self.balance}")
#         else:
#             print("Сума внеску повинна бути додатньою.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Знято: {amount}. Новий баланс: {self.balance}")
#         else:
#             print("Недостатньо коштів")
# amount = int(input("Введіть суму для внеску: "))
# account = Bankaaccount("Ярослав", 1000)
# account.deposit(amount)
# withdraw_amount = int(input("Введіть суму для зняття: "))
# account.withdraw(withdraw_amount)

# class Person:
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age

#         def name1(self):
#             return f"Моє ім'я {self.name} і мені {self.age} років."
# student1 = Person("Ярослав", 16)
# print(student1.name1())

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def get_info(self):
#         return f"Моє ім'я {self.name}, мені {self.age} років і я вчусь в {self.student_id} класі."
# student2 = Student('Саша', 15, 10)
# print(student2.get_info())

# class Teacher(Person):
#     def __init__(self, name, age, teacher_id, subject):
#         super().__init__(name, age)
#         self.teacher_id = teacher_id
#         self.subject = subject

#     def get_info(self):
#         return f"Моє ім'я {self.name}, мені {self.age} років і я викладаю {self.subject}."
# teacher1 = Teacher('Олександр', 35, 1, 'математику')
# print(teacher1.get_info())

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Книга '{book}' додана до бібліотеки.")

#     def remove_book(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             print(f"Книга '{book}' видалена з бібліотеки.")
#         else:
#             print(f"Книга '{book}' не знайдена в бібліотеці.")

#     def list_books(self):
#         print("Книги в бібліотеці:")
#         for book in self.books:
#             print(f" ! {book}")
# library = Library()
# library.add_book("Гаррі Поттер")
# library.add_book("1967")
# library.list_books()
# library.remove_book("Гаррі Поттер")
# library.list_books()
# library.remove_book('1967')

# class Animals:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         return "Звук тварини" 
# class Dog(Animals):
#     def __init__(self, name, species): 
#         super().__init__(name, "Собака")
#         self.species=species

#     def make_sound(self):
#         return "Гав гав"
# class Cat(Animals):
#     def __init__(self, name, species):
#         super().__init__(name, "Кіт")
#         self.species=species

#     def make_sound(self):
#         return "Мяу мяу"
# dog1 = Dog("Коргі", "Собака")
# cat1 = Cat("Австралійський", "Кіт")
# print(f"{dog1.name} : {dog1.species}, звук: {dog1.make_sound()}")
# print(f"{cat1.name} : {cat1.species}, звук: {cat1.make_sound()}")

# class Order:
#     def __init__(self, order_id, items):
#         self.order_id = order_id
#         self.items = items

#     def calculate_total(self):
#         return sum(self.items.values())
# order1 = Order(1, {"яблуко": 10, "телевізор": 200, "м'яч": 50})
# print(f"Загальна сума замовлення {order1.order_id}: {order1.calculate_total()} грн")

