
from threading import Thread
from time import sleep, perf_counter


#
# def task():
#     print('ПОчали виконання задачі...')
#     sleep(1)
#     print('Виконано')
#
# start_time = perf_counter()
#
# task()
# task()
#
# end_time = perf_counter()
# print(f'Виконання зайняло {end_time-start_time:0.2f} секунд')







# def fn():
#     print('ПОчали виконання задачі...')
#     sleep(1)
#     print('Виконано')
#
#
#
# start_time = perf_counter()
#
# new_theard = Thread(target=fn)
# potik2 = Thread(target=fn)
#
# new_theard.start()
# potik2.start()
#
#
# new_theard.join()
# potik2.join()
# end_time = perf_counter()
# print(f'Виконання зайняло {end_time -start_time:02f} секунд')


# def fn(id):
#     print(f'Починаэмо виконання задачі... {id}')
#     sleep(1)
#     print(f'Задачу {id} виконано')
#
# strat_time = perf_counter()
#
# potok = []
# for n in range(1, 11):
#     t = Thread(target=fn, args=(x,))
#     potok.append(t)
#     t.start()
#
#
# for t in potok:
#     t.join()
#
# end_time =  perf_counter()
# print(f'Виконання зайняло {end_time-strat_time:0.2f} секунд')
from time import perf_counter

# def add(filename):
#     print(f'{filename}')
#     with open(filename, 'r') as f:
#         content =f.read()
#
#     content = content.replace()
#     with open(filename, 'w') as f:
#         f.write('My ids')
#
# def files():
#     filenames = [
#         'test1.txt',
#         'test2.txt',
#         'test3.txt',
#         'test4.txt',
#         'test5.txt',
#         'test6.txt',
#         'test7.txt',
#         'test8.txt',
#         'test9.txt',
#         'test10.txt'
#
#     ]
#     potoky = [Thread(target=add(), args=(filename), 'My', 'Him' )

#
#     for filename in filenames:
#         add(filename)
#
#
# start_time = perf_counter()
#
# files()
# end_time = perf_counter()

# print(f'Виконання зайняло {end_time-start_time:0.2f} секунд')

from threading import Thread
import time

def show_timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f'Пройшло {count} секунд')

t = Thread(target=show_timer, daemon=True)
t.start()
answer = input('Чи хочете завершити? \n')



















































