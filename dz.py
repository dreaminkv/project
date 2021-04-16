#2.3.
some_list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
some_list2 =[]
for el in some_list1:
        if el[-1].isdigit() and int(el) < 10:
            el = '"' + el[:-1] + '0' + el[-1] + '"'
            some_list2.append(el)
        else:
            some_list2.append(el)
print(' '.join(some_list2))


some_list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(some_list1)):
    el = some_list1.pop(i-i)
    if el[-1].isdigit() and int(el) < 10:
        el = '"' + el[:-1] + '0' + el[-1] + '"'
        some_list1.append(el)
    else:
        some_list1.append(el)
        
        
print(' '.join(some_list1))

#4 Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида:
#     'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?


workers_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
workers_str = ' '.join(workers_list)
workers_str = workers_str.lower()
workers_list = workers_str.split(' ')
workers_list[1] = workers_list[1].capitalize()
workers_list[4] = workers_list[4].capitalize()
workers_list[-1] = workers_list[-1].capitalize()
workers_list[-3] = workers_list[-3].capitalize()
print('Привет', workers_list[1])
print('Как дела', workers_list[-1], '?')
print('Ты сегодня хорошо выглядишь,', workers_list[4])
