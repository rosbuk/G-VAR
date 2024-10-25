bornyear = ''
while not bornyear.isdigit():
    bornyear = input('В каком году родился А.С. Пушкин?  ')
if int(bornyear) == 1799:
    month = input('Верно. А в каком месяце?  ')
    if month == '6' or month == 'июнь' or month == 'В июне' or month == 'в июне':
        day = input('Верно. А какого числа?  ')
        if day == '6' or day == 'Шестого' or day == 'шестого':
            print('Верно')
        else:
            print('Неверно')
    else:
        print('Неверно')
else:
    print('Неверно')