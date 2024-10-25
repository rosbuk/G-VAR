bornyear = ''
while not (bornyear == '1799' or bornyear == 'В 1799' or bornyear == 'В тысяча семьсот девяноста девятом' 
           or bornyear == '1799.' or bornyear == 'В 1799.' or bornyear == 'В тысяча семьсот девяноста девятом.'):
    bornyear = input('В каком году родился А.С. Пушкин?  ')
print('Верно')

month = ''
while not  (month == '6' or month == 'июнь' or month == 'В июне' or month == 'в июне' 
            or month == '6.' or month == 'июнь.' or month == 'В июне.' or month == 'в июне.' ):
    month = input('А в каком месяце?  ')
print('Верно')

day = ''
while not (day == '6' or day == 'Шестого' or day == 'шестого'
           or day == '6.' or day == 'Шестого.' or day == 'шестого.'):
    day = input(' А какого числа?  ')

print('Верно') 