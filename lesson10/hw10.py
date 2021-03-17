import re
from collections import UserDict


class NameError1(Exception):
    pass


class NameError2(Exception):
    pass


class NameError3(Exception):
    pass


class NameError4(Exception):
    pass


def input_error(func):
    def inner(adress_book, com):
        my_error_2 = "Wrong phone-number (must be in format XXX-XXX-XX-XX)!"
        my_error_3 = "You maked the fail by inputing the command!"
        my_error_4 = "You maked the fail by inputing the number of arguments!"
        my_error_5 = "You wrote wrong the compound commmnd 'good bye'!"
        my_error_6 = "You wrote wrong the compound command 'show all'!"
        my_error_7 = "Missing name in database!"
        my_error_8 = "Phone-number in database is exiest already!"
        try:
            res = func(adress_book, com)
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
        else:
            return res

    return inner


@input_error
def parser(com, my_adressbook):
    commands = {
        "hello": my_adressbook.hello,
        "add": my_adressbook.add,
        "change": my_adressbook.change,
        "delete": my_adressbook.delete,
        "phone": my_adressbook.findall,
        "show all": my_adressbook.showall,
        "exit": my_adressbook.ausgang,
        "close": my_adressbook.ausgang,
        "good bye": my_adressbook.ausgang,
    }

    if com[0] == "exit" or com[0] == "close":
        result = commands[com[0]]()
    elif com[0] == "good" and len(com) > 1:
        if com[1] == "bye":
            result = commands[com[0] + " " + com[1]]()
        else:
            raise NameError1
    elif com[0] == "hello":
        result = commands[com[0]]()
    elif com[0] == "add":
        result = commands[com[0]](com[1], com[2])
    elif com[0] == "change":
        result = commands[com[0]](com[1], com[2])
    elif com[0] == "delete":
        result = commands[com[0]](com[1], com[2])
    elif com[0] == "phone":
        result = commands[com[0]](com[1])
    elif com[0] == "show" and len(com) > 1:
        if com[1] == "all":
            result = commands[com[0] + " " + com[1]]()
        else:
            raise NameError2
    return result


class Adressbook(UserDict):
    def add_Record(self, name, phone):
        if self.data == dict():
            myRecord = {name: [phone]}
        else:
            myRecord = self.data
        return myRecord

    def change_Record(self, name, phone):
        self.data.update({name: phone})
        return self.data


class Field(Adressbook):
    pass


class Name(Field):
    def is_name(self, field):
        for key in self.data.keys():
            if key == field:
                return True


class Phone(Field):
    def is_phone(self, field):
        for value_list in self.data.values():
            for value in value_list:
                if value == field:
                    return True


class Record(Name, Phone):
    name = ""
    phone = []
    data = {}

    def hello(self):
        return "How can I help you?"

    def add(self, name, phone):
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", phone):
            if not self.is_name(name):
                self.data = self.add_Record(name, phone)
                self.data = self.change_Record(name, [phone])
            else:
                if not self.is_phone(phone):
                    self.data[name].append(phone)
                    self.data = self.change_Record(name, self.data.get(name))
                else:
                    raise NameError4
            return "added " + str(self.data.get(name))
        else:
            raise ValueError

    def change(self, name, phone):
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", phone):
            if self.is_name(name):
                self.data[name] = [phone]
                self.data = self.change_Record(self.name, self.data.get(name))
                return "chahged " + str(self.data.get(name))
            else:
                raise NameError3
        else:
            raise ValueError

    def delete(self, name, phone):
        if re.match(r"\d{3}-\d{3}-\d{2}-\d{2}", phone):
            if self.is_name(name):
                if self.is_phone(phone):
                    self.data.get(name).remove(phone)
                    self.data = self.change_Record(self.name, self.phone)
                    return "deleted phone-number"
            else:
                raise NameError3
        else:
            raise ValueError

    def findall(self, name):
        if self.is_name(name):
            return "phones " + str(self.data.get(name))
        else:
            raise NameError3

    def showall(self):
        return str(self)

    def ausgang(self):
        return "Good bye!"


def main():
    my_record = Record()
    result = ""
    key = ""

    print("{:>20}{:<300}".format("Your assistent: ", "Hello"))
    while result != "Good bye!":
        if key == "" in my_record.data.keys():
            my_record.data.pop(key)
        command = input("{:>20}".format("User: "))
        com = command.lower().split(" ")
        result = parser(com, my_record)
        print("{:>20}{:<300}".format("Your assistent: ", result))


if __name__ == "__main__":
    main()