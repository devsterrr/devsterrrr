# import random
# numb = random.randint(1, 10)
# tries = 3
# print("Я загадав число від 1 до 10, вгадай за 3 спроби!")
# for i in range(tries):
#     guess = int(input("Твій варіант: "))
#     if guess == numb:
#         print(" Вгадав!")
#         break
#     else:
#         print(" Не вгадав")
# else:
#     print(" Спроби закінчились. Число було:", numb)


# import time

# minutes = int(input("Введи кількість хвилин: "))
# seconds = minutes * 60

# while seconds > 0:
#     print("Залишилось:", seconds, "сек")
#     time.sleep(1)
#     seconds -= 1

# print(" Час вийшов!")





# import time

# input("Натисни Enter щоб почати")
# start = time.time()
# laps = []
# for i in range(3):
#     input(f"Enter для заміру {i+1}")                     #AI
#     now = time.time()
#     lap = now - start
#     laps.append(lap)
#     print("Час:", round(lap, 2), "сек")

# print("Усі заміри:", laps)



# import random

# char = "abcdefghijklmnopqrstuvwxyz0123456789"
# password = ""

# for i in range(8):
#     password += random.choice(char)
# print(password)



# import random

# choice = input("Орел чи решка? ").lower()

# coin = random.choice(["орел", "решка"])
# print("Випало:", coin)

# if choice == coin:
#     print(" вВадав!")
# else:
#     print(" Не вгадав")
    
    
    

# import time

# t = time.time()
# for i in range(1000000):
#     pass         #AI
# print(time.time() - t)



# import random
# import time

# print(" ПЕНАЛЬТІ!")
# print("Куди бити? вліво / центр / вправо")
# keeper = random.choice(["вліво", "центр", "вправо"])
# start = time.time()
# kick = input("Твій удар: ").lower()
# end = time.time()
# if kick not in ["вліво", "центр", "вправо"]:
#     print(" Невірний вибір. Спроба не зарахована.")

# elif end - start > 3:
#     print(" Запізно! Воротар зловив м'яч!")

# elif kick == keeper:
#     print(" СЕЙВ! Воротар вгадав і стрибнув:", keeper)

# else:
#     print(" ГОЛ!!! Воротар стрибнув:", keeper)