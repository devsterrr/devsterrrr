import random

player = {
    "name": "",
    "hp": 100,
    "attack": 20,
    "gold": 0
}

game_over = False


def create_character():
    name = input("Введи ім'я героя: ")
    player["name"] = name
    print(f"\n Ласкаво просимо, {name}!")
    print("Твоя пригода починається...\n")


def show_status():
    print("\n СТАТУС ГЕРОЯ")
    print(f"Ім'я: {player['name']}")
    print(f"HP: {player['hp']}")
    print(f"Атака: {player['attack']}")
    print(f"Золото: {player['gold']}\n")


def player_choice():
    print("Що ти хочеш зробити?")
    print("1 - Атакувати")
    print("2 - Захищатися")
    print("3 - Втекти")

    try:
        choice = int(input("Твій вибір: "))
        if choice in (1, 2, 3):
            return choice
        else:
            print("Неправильна команда")
            return None
    except ValueError:
        print("Введи число!")
        return None


def battle():
    enemy_hp = random.randint(30, 60)
    enemy_attack = random.randint(5, 12)

    print("\nЗ'явився ворог!")
    print(f"HP ворога: {enemy_hp}")

    while enemy_hp > 0 and player["hp"] > 0:
        choice = None
        while choice is None:
            choice = player_choice()

        if choice == 1:
            damage = player["attack"]
            enemy_hp -= damage
            print(f"Ти завдав {damage} шкоди ворогу")

        elif choice == 2:
            reduced = enemy_attack // 2
            player["hp"] -= reduced
            print(f"Ти захищаєшся, ворог завдав {reduced} шкоди")

        elif choice == 3:
            if random.random() < 0.5:
                print("Ти успішно втік!")
                return
            else:
                print("Втеча не вдалася!")

        if enemy_hp > 0:
            player["hp"] -= enemy_attack
            print(f"Ворог атакує і завдає {enemy_attack} шкоди")

        print(f"HP героя: {player['hp']}")
        print(f"HP ворога: {enemy_hp}\n")

    if player["hp"] > 0:
        gold = random.randint(10, 30)
        player["gold"] += gold
        print(f" Ти переміг ворога і отримав {gold} золота!")


def end_game():
    global game_over
    game_over = True
    print("\n ГРА ЗАВЕРШЕНА")
    show_status()


def main():
    create_character()

    while not game_over and player["hp"] > 0:
        show_status()
        battle()

        if player["gold"] >= 60:
            print("Ти зібрав 70 золота і переміг у грі!")
            end_game()
            return

    if player["hp"] <= 0:
        print("Твій герой загинув...")
        end_game()
    
if __name__ == "__main__":
    main()