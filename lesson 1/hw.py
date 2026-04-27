jobs = [
    {"title": "Python Developer", "city": "Kyiv", "salary": 2000, "remote": True},
    {"title": "Frontend Developer", "city": "Lviv", "salary": 1500, "remote": False},
    {"title": "Backend Developer", "city": "Kyiv", "salary": 2500, "remote": True},
    {"title": "QA Engineer", "city": "Odesa", "salary": 1200, "remote": False},
    {"title": "DevOps", "city": "Kharkiv", "salary": 3000, "remote": True},
    {"title": "Designer", "city": "Kyiv", "salary": 1000, "remote": False},
    {"title": "Project Manager", "city": "Lviv", "salary": 1800, "remote": True},
    {"title": "Data Analyst", "city": "Dnipro", "salary": 1700, "remote": False},
    {"title": "Mobile Developer", "city": "Kyiv", "salary": 2200, "remote": True},
    {"title": "Support Engineer", "city": "Odesa", "salary": 900, "remote": False}
]
sum_salary = 0
for i in jobs:
    sum_salary += i["salary"]

avg_salary = sum_salary / len(jobs)
print("Середня зарплата:", avg_salary)

max_salary = jobs[0]["salary"]
best_vacancy = jobs[0]

for i in jobs:
    if i["salary"] > max_salary:
        max_salary = i["salary"]
        best_vacancy = i

print("Найдорожча вакансія:")
print(best_vacancy)
       


def show_all():
    for i in jobs:
        print(i)

def filter_city():
    city = input("Введіть місто: ")
    for i in jobs:
        if i["city"].lower() == city.lower():
            print(i)

def filter_salary():
    min_salary = int(input("Мінімальна зарплата: "))
    for i in jobs:
        if i["salary"] >= min_salary:
            print(i)

def remote_only():
    for i in jobs:
        if i["remote"]:
            print(i)

while True:
    print("\n  МЕНЮ")
    print("1. Показ всіх вакансій")
    print("2. Фільтр по місту")
    print("3. Фільтр по зарплаті")
    print("4. Тільки remote")
    print("5. Вийти")

    choice = input("Оберіть пункт: ")

    if choice == "1":
        show_all()
    elif choice == "2":
        filter_city()
    elif choice == "3":
        filter_salary()
    elif choice == "4":
        remote_only()
    elif choice == "5":
        print("Вихід")
        break
    else:
        print("Невірний вибір!")