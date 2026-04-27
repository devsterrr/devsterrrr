# vacation_spots = [
#     {
#         'title':'Python Developer',
#         'location':'Remote',
#         'salary':100000,
#         'city':'New York'
#     },
#     {
#         'title':'Data Scientist',
#         'location':'Remote',
#         'salary':120000,
#         'city':'San Francisco'
#     },
#     {
#         'title':'Web Developer',
#         'location':'Remote',
#         'salary':90000,
#         'city':'Los Angeles'
#     },
#     {
#         'title':'Software Engineer',
#         'location':'Remote',
#         'salary':110000,
#         'city':'Chicago'
#     }
# ]

# # for i in range(len(vacation_spots)):
# #     if vacation_spots[i]['salary'] > 100000:
# #         print(vacation_spots[i])

# word= input("Enter a keyword to search for: ")
# for i in range(len(vacation_spots)):
#     if word.lower() in vacation_spots[i]['title'].lower():
#         print(vacation_spots[i])
        
        
vacancies = [
    {"title": "Mobile Developer", "city": "Kyiv", "salary": 38000, "remote": True},
    {"title": "Game Developer", "city": "Lviv", "salary": 36000, "remote": False},
    {"title": "System Administrator", "city": "Dnipro", "salary": 27000, "remote": False},
    {"title": "Cybersecurity Specialist", "city": "Kharkiv", "salary": 47000, "remote": True},
    {"title": "AI Engineer", "city": "Kyiv", "salary": 55000, "remote": True},
    {"title": "Technical Support", "city": "Odesa", "salary": 22000, "remote": False},
    {"title": "Business Analyst", "city": "Lviv", "salary": 40000, "remote": True},
    {"title": "Cloud Engineer", "city": "Kyiv", "salary": 52000, "remote": True},
    {"title": "Tester (Manual)", "city": "Zaporizhzhia", "salary": 25000, "remote": False},
    {"title": "Fullstack Developer", "city": "Vinnytsia", "salary": 43000, "remote": True}
]

def show_all():
    for i in vacancies:
        print(i)

def filter_city():
    city = input("Введіть місто: ")
    for i in vacancies:
        if i["city"].lower() == city.lower():
            print(i)

def filter_salary():
    min_salary = int(input("Мінімальна зарплата: "))
    for i in vacancies:
        if i["salary"] >= min_salary:
            print(i)

def remote_only():
    for i in vacancies:
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