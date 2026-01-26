import json

file_name = "planner.json"

def load_events():
     try:
        with open(file_name, "r", encoding="utf-8") as file:
            planner = json.load(file)
        if planner:
            event_id = max(map(int, planner.keys())) + 1            
        else:
            event_id = 1

        return planner, event_id

     except FileNotFoundError:
        return {},1 
def save_events(planner):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(planner, file, ensure_ascii=False, indent=4)
        
def show_menu():
    print("\n --- Персональний планувальник ---")
    print("1. Додати подію")
    print("2. Переглянути всі події")
    print("3. Видалити подію")
    print("4. Знайти події за датою")
    print("5. Вийти")
    
    
def add_event(planner, event_id):
    title = input("Назва події: ")
    date = input("Дата: ")
    time = input("Час: ")
    description = input("Опис: ")
    
    planner[str(event_id)] = {
        "title": title,
        "date": date,
        "time": time,
        "description": description
    } 

    save_events(planner)
    print(" Подію додано")

    return event_id + 1


def show_events(planner):
    if not planner:
        print(" Подій немає")
        return

    for event_id, event in planner.items():
        print(f"\n ID: {event_id}")
        print(" Назва:", event["title"])
        print(" Дата:", event["date"])
        print(" Час:", event["time"])
        print(" Опис:", event["description"])


def delete_event(planner):
    event_id = input("Введіть ID події для видалення: ")

    if event_id in planner:
        del planner[event_id]
        save_events(planner)
        print(" Подію видалено")
    else:
        print(" Подію не знайдено")


def find_by_date(planner):
    date = input("Введіть дату для пошуку: ")
    found = False
    for event_id, event in planner.items():
        if event["date"] == date:
            print(f"\ nID: {event_id}")
            print(" Назва:", event["title"])
            print(" Час:", event["time"])
            print(" Опис:", event["description"])
            found = True

    if not found:
        print(" Подій на цю дату немає")


def main():
    planner, event_id = load_events()

    while True:
        show_menu()
        choice = input("Оберіть дію: ")

        if choice == "1":
            event_id = add_event(planner, event_id)
        elif choice == "2":
            show_events(planner)
        elif choice == "3":
            delete_event(planner)
        elif choice == "4":
            find_by_date(planner)
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()