# import tkinter as tk 
# import random 
# # root=tk.Tk()
# # # root.title("My app")
# # # root.geometry("600x400")
# # # label=tk.Label(root,text="Hello this is my app")
# # # label.pack(pady=20, padx=20)
# # # root.mainloop()

# # # def click():
# # #     label.config(text="Button Clicked")
# # # root=tk.Tk()
# # # root.title("My app")
# # # root.geometry("600x400")
# # # label=tk.Label(root,text="Hello this is my app")
# # # label.pack(pady=20, padx=20)
# # # button=tk.Button(root,text="Click Me", command=click, bg="blue", fg="white")
# # # button.pack(pady=10)
# # # root.mainloop()

# # def add():
# #     result=int(entry1.get())+int(entry2.get())
# #     label_result.config(text="Result: "+str(result))
# # root=tk.Tk()
# # root.title("Simple Calculator")
# # root.geometry("300x200")
# # entry1=tk.Entry(root)
# # entry1.pack(pady=5)
# # entry2=tk.Entry(root)
# # entry2.pack(pady=5)
# # button=tk.Button(root,text="Add", command=add)
# # button.pack(pady=5)
# # label_result=tk.Label(root, text="Result: ")
# # label_result.pack(pady=5)
# # root.mainloop()


# # number = random.randint(1, 100)
# # attempts = 0

# # def check_number():
# #     global attempts
# #     guess = int(entry.get())    
# #     attempts += 1
# #     if guess < number:
# #         result_label.config(text="Більше!")
# #     elif guess > number:
# #         result_label.config(text="Менше!")
# #     else:
# #         result_label.config(text=f"Ви вгадали за {attempts} спроб!")

# # root = tk.Tk()
# # root.title("Вгадай число")


# # label = tk.Label(root, text="Вгадайте число від 1 до 100")
# # label.pack()
# # entry = tk.Entry(root)
# # entry.pack()


# # button = tk.Button(root, text="Перевірити", command=check_number)
# # button.pack()

# # result_label = tk.Label(root, text="")
# # result_label.pack()
# # root.mainloop()

# def add():
#     a = float(entry1.get())
#     b = float(entry2.get())
#     result_label.config(text="Результат: " + str(a + b))

# def a1():
#     a = float(entry1.get())
#     b = float(entry2.get())
#     result_label.config(text="Результат: " + str(a - b))

# def a2():
#     a = float(entry1.get())
#     b = float(entry2.get())
#     result_label.config(text="Результат: " + str(a * b))

# def a3():
#     a = float(entry1.get())
#     b = float(entry2.get())
#     if b != 0:
#         result_label.config(text="Результат: " + str(a / b))
#     else:
#         result_label.config(text="Не можна ділити на 0")

# root = tk.Tk()
# root.title("Калькулятор")

# tk.Label(root, text="Перше число").pack()
# entry1 = tk.Entry(root)
# entry1.pack()

# tk.Label(root, text="Друге число").pack()
# entry2 = tk.Entry(root)
# entry2.pack()

# tk.Button(root, text="+", command=add).pack()
# tk.Button(root, text="-", command=a1).pack()
# tk.Button(root, text="*", command=a2).pack()
# tk.Button(root, text="/", command=a3).pack()

# result_label = tk.Label(root, text="")
# result_label.pack()

# root.mainloop()

import tkinter as tk
import random


options = ["Камінь", "Ножиці", "Папір"]


def play(user_choice):
    computer_choice = random.choice(options)

    result = ""

    if user_choice == computer_choice:
        result = "Нічия"

    elif (
        (user_choice == "Камінь" and computer_choice == "Ножиці") or
        (user_choice == "Ножиці" and computer_choice == "Папір") or
        (user_choice == "Папір" and computer_choice == "Камінь")
    ):
        result = "Ти виграв"

    else:
        result = "Комп'ютер виграв"

    label_user.config(text="Твій вибір: " + user_choice)
    label_computer.config(text="Комп'ютер: " + computer_choice)
    label_result.config(text=result)



window = tk.Tk()
window.title("Камінь Ножиці Папір")
window.geometry("350x300")


title = tk.Label(window, text="Гра: Камінь Ножиці Папір", font=("Arial", 14))
title.pack(pady=10)


btn1 = tk.Button(window, text="Камінь", width=10, command=lambda: play("Камінь"))
btn1.pack(pady=5)

btn2 = tk.Button(window, text="Ножиці", width=10, command=lambda: play("Ножиці"))
btn2.pack(pady=5)

btn3 = tk.Button(window, text="Папір", width=10, command=lambda: play("Папір"))
btn3.pack(pady=5)


label_user = tk.Label(window, text="")
label_user.pack(pady=5)

label_computer = tk.Label(window, text="")
label_computer.pack(pady=5)

label_result = tk.Label(window, text="", font=("Arial", 14))
label_result.pack(pady=10)

window.mainloop()