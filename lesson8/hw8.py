from datetime import datetime, timedelta

def congratulate(users):
    day_name = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
    employers_list = {i: list() for i in range(1, 6)}

    today = datetime.now()
    today_isoweekday = today.isoweekday()
    monday_date = today - timedelta(days = today_isoweekday - 1)
    employers_list[1] = (find_users(users, monday_date)) 

    employers_list[1].extend(find_users(users, monday_date - timedelta(days = 1))) 
    employers_list[1].extend(find_users(users, monday_date - timedelta(days = 2))) 
    
    for i in range(2, 6):
        employers_list[i] = find_users(users, monday_date + timedelta(days = i - 1)) 


    for d, list_user in employers_list.items():
        if len(list_user) > 0:
            print(f'{day_name[d]}: ' + ", ".join(list_user))

def find_users(users, day):
    result_list = []
    for name, birthday in users.items():
        if birthday.date() == day.date():
            result_list.append(name)

    return result_list


if __name__ == '__main__':
    users = {
            'Jobajo': datetime(2021, 2, 23),
            'Yuzufe': datetime(2021, 2, 24),
            'Neduwu': datetime(2021, 2, 25),
            'Dunobe': datetime(2021, 2, 23),
            'Yavini': datetime(2021, 2, 26),
            'Gatija': datetime(2021, 2, 22),
            'Xohefo': datetime(2021, 2, 27),
            'Muchek': datetime(2021, 2, 28),
            }

congratulate(users)