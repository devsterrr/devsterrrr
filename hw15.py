class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


    def show_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Курс: {self.course}")


    def change_course(self, new_course):
        self.course = new_course


student1 = Student('Ярослав', 18, 1)
student2 = Student("Олена", 19, 2)

student1.show_info()
student2.show_info()

student1.change_course(2)
student1.show_info()


class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True


tasks = [
    Task("Зробити ДЗ з Python"),
    Task("Прочитати книгу"),
    Task("Піти на тренування")
]

tasks[0].mark_done()

for task in tasks:
    print(f"Завдання: {task.title}, Виконано: {task.completed}")


class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print(f"Подія: {self.title}, Дата: {self.date}")

class Event1(Event):
    def __init__(self, title, date, description):
        super().__init__(title, date)
        self.description = description

    def update_description(self, new_description):
        self.description = new_description

    def show(self):
        print(f"Подія: {self.title}, Дата: {self.date}, Опис: {self.description}")


event = Event1("Кр з фізики", "10.02.2024", "Підготувати формули")
event.show()

event.update_description("Вивчити всі теми")
event.show()