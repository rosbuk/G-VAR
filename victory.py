churchil = 1874
washington = 1732
hitler = 1889
longfello = 1807
beethoven = 1770 
balzac = 1799

game = 'Да'
while game == 'Да':
    print('Пиши только цифры года.')
    q = 'В каком году родился '

    churchil_q = input(q + 'Черчиль'+'?   ')  # Черчиль родился в 1874 году
    washington_q = input(q + 'Вашингтон'+'?   ')  # Вашингтон родился в 1732 году
    hitler_q = input(q + 'Гитлер'+'?   ')  # Гитлер родился в 1889 году
    longfello_q = input(q + 'Лонгфелло'+'?   ')  # Лонгфелло родился в 1807 году
    beethoven_q = input(q + 'Бетховен'+'?   ')  # Бетховен родился в 1770 году
    balzac_q = input(q + 'Бальзак'+'?   ')  # Бальзак родился в 1799 году

    i=0
    if churchil_q == str(churchil):
        i+=1
    if washington_q == str(washington):    
        i+=1
    if hitler_q == str(hitler):    
        i+=1
    if longfello_q == str(longfello):    
        i+=1
    if beethoven_q == str(beethoven):    
        i+=1
    if balzac_q == str(balzac):    
        i+=1

    print('Правильных ответов', i)
    print('Неправильных ответов', 6-i)
    print('Процент правильных ответов', i*100/6)
    print('Процент неправильных ответов', 100-i*100/6)

    game = input('Хочешь сыграть еще раз? ')
    if game == 'Нет':
        break

    



