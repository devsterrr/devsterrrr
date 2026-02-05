class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(90)
acc.deposit(50)
acc.withdraw(20)
print(acc.get_balance())



class UserProfile:
    def __init__(self, email):
        self.__email = email

    def set_email(self, value):
        self.__email = value

    def get_email(self):
        return self.__email

user = UserProfile("test111@mail.com")
user.set_email("neww@mail.com")
print(user.get_email())



class Battery:
    def __init__(self, charge):
        self.__charge = charge

    def get_charge(self):
        return self.__charge


batt = Battery(100)
print(batt.get_charge())



class Speaker:
    def __init__(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume


sp = Speaker(25)
print(sp.get_volume())



class Character:
    def __init__(self, health):
        self.__health = health

    def damage(self, amount):
        self.__health -= amount

    def heal(self, amount):
        self.__health += amount

    def get_health(self):
        return self.__health


hero = Character(100)
hero.damage(30)
hero.heal(10)
print(hero.get_health())



class PasswordManager:
    def __init__(self, password):
        self.__password = password

    def change_password(self, old, new):
        self.__password = new


pm = PasswordManager("12345678")
pm.change_password("12345678", "newpassword")                                   #AI