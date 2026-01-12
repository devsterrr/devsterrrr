# while True:
#     try:
#         x = int(input("Введи число: "))
#         print("Ти ввів:", x)
#         break
#     except ValueError:
#         print(" Це не число, спробуй ще раз")



# try:
#     a = int(input("Введи перше число: "))
#     b = int(input("Введи друге число: "))

#     print("1 - +")
#     print("2 - -")
#     print("3 - *")
#     print("4 - /")

#     choice = input("Обери дію: ")

#     if choice == "1":
#         print("Результат:", a + b)
#     elif choice == "2":
#         print("Результат:", a - b)
#     elif choice == "3":
#         print("Результат:", a * b)
#     elif choice == "4":
#         try:
#             print("Результат:", a / b)
#         except ZeroDivisionError:
#             print("На нуль ділити не можна")
#     else:
#         print("Невірний пункт меню")

# except ValueError:
#     print("Треба вводити числа")


# name = input("Введи імʼя: ")

# while True:
#     try:
#         age = int(input("Введи вік: "))
#         if 1 <= age <= 120:
#             print(f"Привіт, {name}! Тобі {age} років.")
#             break
#         else:
#             print(" Вік має бути від 1 до 120")
#     except ValueError:
#         print(" Вік має бути числом")


# numbers = [1, 2, 3, 4, 5]

# try:
#     index = int(input("Введи індекс (0-4): "))
#     print("Елемент:", numbers[index])
# except ValueError:
#     print(" Індекс має бути числом")
# except IndexError:
#     print(" Такого індексу немає")
    
    
# filename = input("Введи назву файлу: ")

# try:
#     file = open(filename, "r", encoding="utf-8")
#     print(file.read())                                         #AI
#     file.close()
# except:
#     print("Файл не знайдено")
    
# rate = 43  
# try:
#     uah = float(input("Введи суму в гривнях: "))
#     if uah < 0:
#         print(" Сума не може бути відʼємна")
#     else:
#         usd = uah / rate
#         print("В доларах:", round(usd, 2))
# except ValueError:
#     print(" Треба ввести число")


# try:
#     a = int(input("Введи число A: "))
# except:
#     print("Помилка: A не число")
#     a = 1

# try:
#     b = int(input("Введи число B: "))
# except:
#     print("Помилка: B не число")
#     b = 1

# try:
#     print("A / B =", a / b)
# except:
#     print("Помилка: на нуль ділити не можна")