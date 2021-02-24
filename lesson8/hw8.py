from datetime import datetime
import random
import string

def congratulate(users):
    today = datetime.now()
    while today.weekday() != 6:
        try:
            tomorrow = today.day + 1
            today = today.replace(day=tomorrow)
        except ValueError:
            a = today.month + 1
            today = today.replace(month=a, day=1)
    else:
        for _ in range(30):
            try:
                tomorrow = today.day + 1
                today = today.replace(day=tomorrow)
            except ValueError:
                a = today.month + 1
                today = today.replace(month=a, day=1)
            for user in users:
                temp = datetime.strptime(user["birthday"], "%d.%m.%y")

                if (today.month == temp.month and today.day == temp.day):
                    b = temp.strftime("%A")
                    c = temp.strftime("%d.%m")
                    if (temp.weekday() == 0 or temp.weekday() == 1 or temp.weekday() == 2 or temp.weekday() == 3 or temp.weekday() == 4):
                        print(f"{b}({c}) : {user['name']} \n")
                    else:
                        print(f"Monday({c}) : {user['name']} \n")

def main():
    users = [{},
    {},
    {},
    {},
    {},
    {},
    {}]
    for i in range(7):
        day = str(random.randint(1, 28))
        mounth = str(random.randint(1, 12))
        year = str(random.randint(80, 99))
        users[i]["name"] = "".join(random.choices(string.ascii_letters, k=10)).capitalize()
        users[i]["birthday"] = day + "." + mounth + "." + year
    
    congratulate(users)

if __name__ == "__main__":
    main()