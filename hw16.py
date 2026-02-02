class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print(self.get_info())

    def get_info(self):
        return f"Подія: {self.title}, Дата: {self.date}"


class Training(Event):
    def __init__(self, title, date, sport):
        super().__init__(title, date)
        self.sport = sport

    def show(self):
        print(self.get_info())

    def get_info(self):
        return f"Тренування: {self.title}, Дата: {self.date}, Вид спорту: {self.sport}"


class Birthday(Event):
    def __init__(self, title, date, person):
        super().__init__(title, date)
        self.person = person

    def show(self):
        print(self.get_info())

    def get_info(self):
        return f"День народження: {self.title}, Дата: {self.date}, Іменинник: {self.person}"


class OnlineEvent(Event):
    def __init__(self, title, date, link):
        super().__init__(title, date)
        self.link = link

    def show(self):
        print(self.get_info())

    def get_info(self):
        return f"Онлайн-подія: {self.title}, Дата: {self.date}, Посилання: {self.link}"



events = [
    Training("Ранкове тренування", "05.02.2026", "Футбол"),
    Birthday("Свято", "10.02.2024", "Ярослав"),
    Event("Зустріч", "12.02.2025"),
    OnlineEvent("Вебінар з Python", "15.01.2025", "https://exmpl.com")
]

for event in events:
    print(event.get_info())