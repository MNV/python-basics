

branch = {

    'Ул. Бейкер стрит, 221б': (5, 2),
    'Почтовое отделение': (0, 2),
    'Ул. Грибоедова, 104/25 ': (2, 5),
    'Ул. Большая Садовая, 302-бис': (6, 6),
    'Вечнозелёная Аллея, 742': (8, 3)
}


def distance(start, point2):
    '''

    :param start:  НАЧАЛЬНАЯ ТОЧКА
    :param point2: КОНЕЧНАЯ ТОЧКА
    :return: float
    '''
    return ((point2[0] - start[0]) ** 2 + (point2[1] - start[1]) ** 2) ** 0.5


def short_cut(branch_d):
    '''

    :param branch_d: Получаем словарь
    :return: возвращаем список. Координаты точек, следующие друг за другом
    '''
    point1 = branch_d.pop('Почтовое отделение')  # Определяем начальные координаты забирая со словаря
    s_c = [point1, '->'] # Готовим выходной список с начальной точкой
    start = point1 # start будем менять

    for i in range(len(branch_d)):
        cut = [] #Промежуточный список для поиска ближней точки

        for key, point2 in branch_d.items():

            res = distance(start=start, point2=point2)
            if not cut:
                cut = [key, point2, [res]]
            elif res < cut[2][0]:
                cut = [key, point2, [res]]

        if i >= 1:
            path_sum = s_c[-2][0] + cut[2][0]

            s_c.append(cut[1])

            s_c.append([path_sum])
            s_c.append('->')
        else:
            s_c.append(cut[1])

            s_c.append(cut[2])
            s_c.append('->')

        start = cut[1]
        if len(branch_d) != 1:
            branch_d.pop(cut[0])
        else:
            comeback = distance(start=cut[1], point2=point1)
            path_sum = s_c[-2][0] + comeback

            s_c.append(point1)
            s_c.append([path_sum])
            s_c.append('=')
            s_c.append([path_sum])

    return s_c


print(' '.join(map(str, short_cut(branch))))
