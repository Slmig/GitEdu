dictsold = {}
for i in range(0,5):
    dictsold['Призывник'+str(i+1)]=input('Введите фамилию призывника №'+str(i+1))
    dictsold['Призывник'+str(i+1)]+='.'+input('Введите имя призывника №'+str(i+1))
    dictsold['Призывник'+str(i+1)]+='.'+input('Введите отчество призывника №'+str(i+1))
    dictsold['Призывник'+str(i+1)]+='.'+input('Введите год рождения призывника №'+str(i+1))
    dictsold['Призывник'+str(i+1)]+='.'+input('Введите заболевание призывника №'+str(i+1))
'''#Запись данных в словарь. Для каждого призывника создаётся уникальный ключ.
Записываются все данные разделённые точкой, чтобы
их можно было легко получить с помощью split()'''
print(93*'-')
print('|Призывники ',end='')
for i in 'Фамилия','Имя','Отчество','Гор рождения','Заболевание':
    print('|'+'{:^15}'.format(i),end='')
print('|')
print(93*'-',end='')
'''Тут выводится верхняя строка таблицы, чтобы было понятно, чему
соответствует каждый столбец таблицы. Так же присутсвуют "|",'-' для
табличного вида'''
for i in range(0,5):
    print()
    print('|'+'Призывник№'+str(i+1)+'|',end='')
    for j in dictsold['Призывник'+str(i+1)].split('.'):
        print('{:^15}'.format(j)+'|',end='')
    print('')
print(93*'-',end='')
'''Берётся информация из словаря с помощью ключа, который
мы знаем заранне, т.к знаем, каким образом он формируется.
После чего выводятся полученные с помощью split() данные
Данные полученные с помощью split() представляют собой
итерируемый объект. Поэтому я воспользовался циклом for
и вывел все характеристики призывника по очереди.
Опять же символы '-','|' для рамки таблицы'''




