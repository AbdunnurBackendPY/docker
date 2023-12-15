# функция чтения лабиринта из файла basic_lab.txt
def load_lab():
    lab = {}
    with open("basic_lab.txt", "r") as f:
        for k in f.__iter__():
            # paramlist - список параметров текущего зала
            paramlist = k.split('\t')
            # извлекаем перечень дверей, преобразуя его в список
            doorlist = []
            for door in paramlist[1].split(','):
                doorlist.append(int(door))
            # формируем словарь, содержащий параметры текущего зала
            hall = {
                'doors': doorlist,
                'name': paramlist[2],
                'coins': int(paramlist[3]),
                'monster': paramlist[4],
                'monstlevel': int(paramlist[5]),
                # с помощью тернарного опертора: если принцесса есть, то True, иначе False
                'princess': True if paramlist[6][0] == '1' else False
            }
            # записываем текущий зал в лабиринт
            lab.update({int(paramlist[0]): hall})
    return lab


# функция, описывающая 1 ход игрока
def turn(hall, hallparams, coins, level):
    print(f'You are in the hall No {hall}')
    print(f'hallparams: {hallparams}')
    # прибавляем монеты, лежащие в зале. Потом добавить сюда удаление монет из параметров лабиринта
    coins += hallparams['coins']
    print(f'Now you have {coins} coins')
    # смотрим, есть ли монстр. Сюда потом вставить вызов функции боя
    if hallparams['monstlevel'] != 0:
        print(f"Attention! There is a monster! It is {hallparams['monster']}")
        level += hallparams['monstlevel']
    # считаем, что монстра победили, смотрим, есть ли принцесса
    if hallparams['princess']:
        return (coins, hallparams['doors'],hallparams['princess'], level)
    # если принцессы нет, смотрим на двери
    print(f"Doors available: {hallparams['doors']}")
    return (coins, hallparams['doors'], hallparams['princess'], level )


coins = 0
level = 1
curhall = 0 # переменная, хранящая номер текущего зала
labirint = load_lab()
print(labirint)
halltuple = (0,False)
# главный цикл игры
while True:
    # запрашиваем кортеж результатов прохождения зала
    halltuple = turn(curhall, labirint[curhall], coins, level)
    # получаем монеты и уровень
    coins = halltuple[0]
    level = halltuple[3]
    # мы выиграли, если нашли принцессу
    if halltuple[2]:
        print(f'You won! The princess is here! Your level is {level}')
        break
    # если принцессы не было, продолжаем игру
    userchoice = int(input('Select a door'))
    # Нужна проверка, есть ли такой зал вообще (проверяем через halltuple[1])
    while userchoice not in halltuple[1]:
        userchoice = int(input('Select a door e gen'))

    curhall = userchoice


def fight()