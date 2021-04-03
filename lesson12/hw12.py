from datetime import datetime
from datetime import timedelta
from collections import UserDict
import pathlib
import pickle
import re


class NameError1(Exception):
    pass


class NameError2(Exception):
    pass


class NameError3(Exception):
    pass


class NameError4(Exception):
    pass


class NameError5(Exception):
    pass


def input_error(func):
    def inner(adress_book, com):
        my_error_1 = "You wrote wrong the second key or it's missing"
        my_error_2 = "Wrong phone-number (must be in format XXX-XXX-XX-XX) or birthday (must be in format XX-XX-XXXX)!"
        my_error_3 = "You maked the fail by inputing the command!"
        my_error_4 = "You maked the fail by inputing the number of arguments!"
        my_error_5 = "You wrote wrong the compound commmnd 'good bye'!"
        my_error_6 = "You wrote wrong the compound command 'show all'!"
        my_error_7 = "Missing name in database!"
        my_error_8 = "Phone-number in database is not exiest yet!"
        my_error_9 = "Date of birthday in database is not exiest yet!"
        try:
            res = func(adress_book, com)
        except KeyError:
            return my_error_1
        except ValueError:
            return my_error_2
        except UnboundLocalError:
            return my_error_3
        except IndexError:
            return my_error_4
        except NameError1:
            return my_error_5
        except NameError2:
            return my_error_6
        except NameError3:
            return my_error_7
        except NameError4:
            return my_error_8
        except NameError5:
            return my_error_9
        else:
            return res

    return inner


@input_error
def parser(com, my_adressbook):
    commands = {
        "add": my_adressbook.add,
        "change": my_adressbook.change,
        "delete": my_adressbook.delete,
        "find": my_adressbook.findall,
        "hello": my_adressbook.hello,
        "help": my_adressbook.help,
        "name": my_adressbook.findname,
        "phone": my_adressbook.findphone,
        "birthday": my_adressbook.findbirthday,
        "show all": my_adressbook.showall,
        "exit": my_adressbook.ausgang,
        "close": my_adressbook.ausgang,
        "good bye": my_adressbook.ausgang,
    }
    arguments = {
        "add": "<name> <value>",
        "change": "<name> <old_value> <new_value>",
        "delete": "<name> <value>",
        "find": "<second_key (all, phone, birthday)> <name>",
        "hello": "<nothing>",
        "help": "<nothing>",
        "name": "<part or full name>",
        "phone": "<part or full phone-number>",
        "birthday": "<part or full date of birthday>",
        "show all": "<nothing>",
        "exit": "<nothing>",
        "close": "<nothing>",
        "good bye": "<nothing>",
    }

    if com[0] == "exit" or com[0] == "close":
        result = commands[com[0]]()
    elif com[0] == "good" and len(com) > 1:
        if com[1] == "bye":
            result = commands[com[0] + " " + com[1]]()
        else:
            raise NameError1
    elif com[0] == "add":
        result = commands[com[0]](com[1], com[2])
    elif com[0] == "change":
        result = commands[com[0]](com[1], com[2], com[3])
    elif com[0] == "delete":
        result = commands[com[0]](com[1], com[2])
    elif com[0] == "find":
        result = commands[com[0]](com[1], com[2])
    elif com[0] == "hello":
        result = commands[com[0]]()
    elif com[0] == "help":
        result = commands[com[0]](commands, arguments)
    elif com[0] == "name":
        result = commands[com[0]](com[1])
    elif com[0] == "phone":
        result = commands[com[0]](com[1])
    elif com[0] == "birthday":
        result = commands[com[0]](com[1])
    elif com[0] == "show" and len(com) > 1:
        if com[1] == "all":
            result = commands[com[0] + " " + com[1]]()
        else:
            raise NameError2
    return result


class Adressbook(UserDict):
    def add_Record(self, name, value, type_value="phone"):
        if self.data == dict():
            myRecord = {name: {type_value: value}}
        else:
            myRecord = self.data
        return myRecord

    def change_Record(self, name, value):
        self.data.update({name: value})
        return self.data

    def iterator(self):
        item = self.data.popitem()
        yield str(item)


class Field(Adressbook):
    def __init__(self):
        self.__value = ""

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    def is_name(self, field):
        for key in self.data.keys():
            if key == field:
                return True


class Phone(Field):
    def is_phone(self, field):
        for value_list in self.data.values():
            for v in value_list["phone"]:
                if v == field:
                    return True


class Birthday(Field):
    def is_birthday(self, field):
        for v in self.data.values():
            if v["birthday"] == field:
                return True


class Record(Name, Phone, Birthday):
    def __init__(self):
        self.name = ""
        self.phone = []
        self.birthday = ""
        self.data = {}

    def __add_item_phone(self, name, phone):
        if "phone" in self.data[name]:
            self.data[name]["phone"].append(phone)
        else:
            self.data[name]["phone"] = [phone]

    def __add_phone(self, name, phone):
        if not self.is_name(name):
            self.data = self.add_Record(name, {"phone": [phone]})
            self.data = self.change_Record(name, {"phone": [phone]})
        else:
            self.__add_item_phone(name, phone)
            self.data = self.change_Record(name, self.data.get(name))
        return "added phone-number"

    def __add_birthday(self, name, birthday):
        if not self.is_name(name):
            self.data = self.add_Record(name, {"birthday": birthday}, "birthday")
            self.data = self.change_Record(name, {"birthday": birthday})
        else:
            self.data[name]["birthday"] = birthday
            self.data = self.change_Record(name, self.data.get(name))
        return str(self.day_to_birthday(name)) + " days to birthday"

    def __change_phone(self, name, old_phone, new_phone):
        if self.is_name(name):
            if self.is_phone(old_phone):
                self.data[name]["phone"].remove(old_phone)
                self.__add_item_phone(name, new_phone)
                self.data = self.change_Record(name, self.data.get(name))
                return "changed phone-number"
            else:
                raise NameError4
        else:
            raise NameError3

    def __change_birthday(self, name, old_birthday, new_birthday):
        if self.is_name(name):
            if self.is_birthday(old_birthday):
                self.data[name]["birthday"] = new_birthday
                self.data = self.change_Record(name, self.data.get(name))
                return "changed date of birthday"
            else:
                raise NameError5
        else:
            raise NameError3

    def __delete_phone(self, name, phone):
        if self.is_name(name):
            if self.is_phone(phone):
                self.data[name]["phone"].remove(phone)
                self.data = self.change_Record(name, self.data.get(name))
                return "deleted phone-number"
            else:
                raise NameError4
        else:
            raise NameError3

    def __delete_birthday(self, name, birthday):
        if self.is_name(name):
            if self.is_birthday(birthday):
                self.data[name].pop("birthday")
                self.data = self.change_Record(name, self.data.get(name))
                return "deleted date of birthday"
            else:
                raise NameError5
        else:
            raise NameError3

    def add(self, name, value):
        self.value = value
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", self.value):
            return self.__add_phone(name, self.value)
        elif re.match(r"\d{2}-\d{2}-\d{4}", self.value):
            _ = datetime.strptime(self.value, "%d-%m-%Y")
            return self.__add_birthday(name, self.value)
        else:
            raise ValueError

    def change(self, name, old_value, new_value):
        self.value = new_value
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", self.value):
            return self.__change_phone(name, old_value, self.value)
        elif re.match(r"\d{2}-\d{2}-\d{4}", self.value):
            return self.__change_birthday(name, old_value, self.value)
        else:
            raise ValueError

    def delete(self, name, value):
        self.value = value
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", self.value):
            return self.__delete_phone(name, self.value)
        elif re.match(r"\d{2}-\d{2}-\d{4}", self.value):
            return self.__delete_birthday(name, self.value)
        else:
            raise ValueError

    def findall(self, arg, name):
        if self.is_name(name):
            temp = str(self.day_to_birthday(name)) + " days to birthday"
            if arg == "all":
                return str(self.data.get(name)) + " " + temp
            elif arg == "phone" or arg == "birthday":
                return str(self.data.get(name).get(arg)) + " " + temp
            else:
                raise KeyError
        else:
            raise NameError3

    def hello(self):
        return "How can I help you?"

    def showall(self):
        result = ""
        serialized_data = pickle.dumps(self.data, 5)
        while True:
            try:
                result += "\n\t\t\t" + str(next(self.iterator()))
            except KeyError:
                self.data = pickle.loads(serialized_data)
                return result

    def ausgang(self):
        return "Good bye!"

    def day_to_birthday(self, name):
        my_date_str = self.data[name]["birthday"]
        my_date = datetime.strptime(my_date_str, "%d-%m-%Y")
        date_birthday = timedelta(days=my_date.timetuple().tm_yday)
        date_now = timedelta(days=datetime.now().timetuple().tm_yday)
        oldyear = timedelta(days=datetime(year=1, month=12, day=31).timetuple().tm_yday)
        newyear = timedelta(days=datetime(year=1, month=1, day=1).timetuple().tm_yday)
        if date_birthday == date_now:
            result = 0
        elif date_birthday > date_now:
            result = date_birthday - date_now
        else:
            result = (oldyear - date_now) + (date_birthday - newyear)
        return result.days

    def help(self, commands, arguments):
        result = "You can to write next commands for working with me:"
        for command in commands.keys():
            result += "\n\t\t\t" + str(command) + " " + str(arguments[command])
        return result

    def findname(self, name):
        result = ""
        for elem in self.data.keys():
            if re.findall(name, elem):
                result += "\n\t\t\t" + str(elem) + " " + str(self.data[elem])
        if result:
            return result
        else:
            raise NameError3

    def findphone(self, phone):
        result = ""
        for name in self.data.keys():
            for elem in self.data[name]["phone"]:
                if re.findall(phone, elem):
                    result += "\n\t\t\t" + str(name) + " " + str(elem)
        if result:
            return result
        else:
            raise NameError4

    def findbirthday(self, birthday):
        result = ""
        for name in self.data.keys():
            temp = self.data[name]["birthday"]
            if re.findall(birthday, temp):
                result += "\n\t\t\t" + str(name) + " " + str(temp)
        if result:
            return result
        else:
            raise NameError5


def main():
    my_record = Record()
    my_record.data = {
        "nanov": {
            "phone": ["006-222-33-33", "073-888-78-89"],
            "birthday": "25-09-1953",
        },
        "okov": {
            "phone": ["098-333-44-44", "063-999-45-56"],
            "birthday": "07-03-1983",
        },
        "midov": {
            "phone": ["050-444-55-66"],
            "birthday": "14-12-1998",
        },
        "perov": {
            "phone": ["098-777-44-44", "050-444-55-66"],
            "birthday": "07-07-1983",
        },
        "serov": {
            "phone": ["098-777-44-44", "050-444-55-66"],
            "birthday": "03-09-1983",
        },
    }

    result = ""
    key = ""

    if pathlib.Path("my.txt").is_file():
        with open("my.txt", "rb") as file:
            my_record = pickle.load(file)

    print("{:>20}{:<300}".format("Your assistent: ", "Hello"))
    while result != "Good bye!":
        if key == "" in my_record.data.keys():
            my_record.data.pop(key)
        command = input("{:>20}".format("User: "))
        com = command.lower().split(" ")
        result = parser(com, my_record)
        print("{:>20}{:<300}".format("Your assistent: ", result))

    with open("my.txt", "wb") as file:
        pickle.dump(my_record, file, 5)


if __name__ == "__main__":
    main()