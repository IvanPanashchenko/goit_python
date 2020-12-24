
r = 0
o = None
while o != "=":
    try:
        x = input("Введите число: ")
        y = float(x)
    except ValueError:
        print("Ошибка ввода")
        continue
    if o == None:
        r = y
    elif o == "+":
        r += y
    elif o == "-":
        r -= y
    elif o == "*":
        r *= y
    elif o == "/":
        try:
            r /= y
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            continue
    o = input("Введите операотр: ")
    while o not in ('+', "-", '*', '/', '='):
        print("Ошибка ввода оператора")
        o = input("Введите оператор: ")
    if o == "=":
        continue
print(f' {r} ')