# from datetime import datetime                                    # AI

# text = input("Що сьогодні сталося? ")
# with open("diary.txt", "a", encoding="utf-8") as file:
#     file.write(f"{datetime.now()}: {text} \n")

# print("Запис збережено")


# grades = [5, 4, 5, 4, 4]

# with open("grades.txt", "w", encoding="utf-8") as file:
#     file.write(" ".join(map(str, grades)))

# with open("grades.txt", "r", encoding="utf-8") as file:
#     grades_from_file = list(map(int, file.read().split()))
# average = sum(grades_from_file) / len(grades_from_file)

# print("Середнє значення:", average)

# login = input("Логін: ")
# password = input("Пароль: ")

# with open("pass.txt", "a", encoding="utf-8") as file:
#     file.write(f"{login}:{password}\n")

# print("Користувача збережено")

# import os

# filename = input("Введи назву файлу: ")

# if os.path.exists(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         print(file.read())
# else:
#     print("Файл не існує")


# a = float(input("Число 1: "))
# b = float(input("Число 2: "))
# result = a + b

# with open("calc_history.txt", "a", encoding="utf-8") as file:
#     file.write(f"{a} + {b} = {result}\n")

# print("Результат:", result)


# import json

# event = {
#     "date": input("Введи дату: "),
#     "title": input("Назва події: "),
#     "place": input("Місце: ")
# }

# with open("planner.json", "w", encoding="utf-8") as file:
#     json.dump(event, file, ensure_ascii=False, indent=4)

# with open("planner.json", "r", encoding="utf-8") as file:
#     data = json.load(file)


# print("\n ЗБЕРЕЖЕНА ПОДІЯ:")
# print("Дата:", data["date"])
# print("Подія:", data["title"])
# print("Місце:", data["place"])

# with open("numbers.txt", "r", encoding="utf-8") as file:
#     numbers = list(map(int, file.read().split()))

# numbers.sort()

# print("Відсортовані числа:", numbers)

# numbers = [12, 5, 8, 20, 3]

# with open("data.txt", "w", encoding="utf-8") as file:
#     file.write(" ".join(map(str, numbers)))

# with open("data.txt", "r", encoding="utf-8") as file:
#     numbers_from_file = list(map(int, file.read().split()))

# numbers_from_file.sort()


# with open("sorted_data.txt", "w", encoding="utf-8") as file:
#     file.write(" ".join(map(str, numbers_from_file)))
