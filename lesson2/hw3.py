print('Программа калькулятор' )
while True:
    try:

        x = float(input('Введите первое значение: '))
        o = input('''Введите оператор " + , - , * ,/ ''')
        y = float(input('Введите второе значение: '))
        r = input('Введите " = " ')

    except ValueError:
        print("Некоректно введено значение, повторите попытку")
        break

    
    if o == '+':
        print('{} + {} = '.format(x, y))
        print(x + y)
        break
    elif o =='++':
        print('Ошибка ввода оператора')
        break

    
    elif o == '-':
        print('{} - {} = '.format(x, y))
        print(x - y)
        break
    elif o == '--':
        print('Ошибка ввода оператора')
        break

   
    elif o == '*':
        print('{} * {} = '.format(x, y))
        print(x * y)
        break
    elif o =='**':
        print('Ошибка ввода оператора')
        break

   
    elif o == '/':
        try:
            print('{} / {} = '.format(x, y))
            print(x / y)
            break
        except ZeroDivisionError:
            print("Деление на ноль запрещено!")
        break

    elif o == '//':
        print('Ошибка ввода оператора')
        break
    else:
        print('''Что то пошло не так как нужно! 
        Перепроверьте правильность ввода''')
        break


 