import random 
import os 

COLOR_CODE = {
        "BLUE": "\033[34m",
        "RESET": "\033[0m",
}
os.system("cls")
print(f'''{COLOR_CODE["BLUE"]} 
                                                                                 
                                                                                 
                                                                                     
                                                                                     
▓█████▄  ▄▄▄     ▄▄▄█████▓ ▄▄▄       ▄▄▄▄    ▄▄▄        ██████ ▓█████ 
▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒████▄    ▓█████▄ ▒████▄    ▒██    ▒ ▓█   ▀ 
░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒███   
░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░█▀  ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄ 
░▒████▓  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░▒████▒
 ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ░ ▒  ▒   ▒   ▒▒ ░   ░      ▒   ▒▒ ░▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░
 ░ ░  ░   ░   ▒    ░        ░   ▒    ░    ░   ░   ▒   ░  ░  ░     ░   
   ░          ░  ░              ░  ░ ░            ░  ░      ░     ░  ░
 ░                                        ░                           

                          ''')                                      

first_names = ["Иван", "Александр", "Елена", "Ольга", "Мария", "Дмитрий", "Анна", "Сергей"]
last_names = ["Иванов", "Петров", "Сидорова", "Смирнов", "Козлов", "Васильева", "Морозов"]
cities = ["Москва", "Санкт-Петербург", "Киев", "Минск", "Астана", "Ташкент"]
ages = list(range(18, 70))

def generate_fake_person():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    city = random.choice(cities)
    age = random.choice(ages)
    
    return f"{first_name} {last_name}, {age} лет, город {city}"

fake_people = [generate_fake_person() for _ in range(10)]

for person in fake_people:
    print(person)