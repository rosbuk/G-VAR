bornyear = ''
while not bornyear.isdigit():
    bornyear = input('В каком году родился А.С. Пушкин?  ')
if int(bornyear) == 1799:
    print('Верно')
else:
    print('Неверно')

