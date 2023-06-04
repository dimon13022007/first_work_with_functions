from time import perf_counter
from threading import Thread
import os
import threading

#1 задание

def files():
    for i in range(100):
        filenames = f"papka_z_filamy_{i}.doc"
        with open(filenames, "w") as f:
            f.write("Hi")


start_time = perf_counter()

files()
end_time = perf_counter()
print(f'Виконання зайняло {end_time-start_time:0.2f} секунд')





# 2 задание в котором я не понимал в чем ошибка
# def add(filename, pidstroka, stroka):
#     print(f'{filename}')
#     with open(filename, 'w') as f:
#         content = f.read()
#
#     content = content.replace(pidstroka, stroka)
#
#     with open(filename, 'w') as f:
#         f.write(content)

# def files():
#     global filenames
#     for i in range(100):
#         filenames = f"papka_z_filamy_{i}.doc"
#         with open(filenames, "w") as f:
#             f.write("Hi")
#     potoky = [Thread(target=add, args=(filename, 'Hi', 'Bye')) for filename in filenames]
#
#     for potik in potoky:
#         potik.start()
#
#     for potik in potoky:
#         potik.join()
#
#     for filename in filenames:
#         add(filename, 'Hi', 'Bye')
#
#
# start_time = perf_counter()
#
# files()
# end_time = perf_counter()
# print(f'Виконання зайняло {end_time - start_time:0.2f} секунд')



# 2 задание в котором Chat gpt обьяснил как правльно сделать
# from threading import Thread, Lock
#
# mutexes = {}
#
# def add(filename, pidstroka, stroka):
#     with mutexes[filename]:
#         with open(filename, 'r') as f:
#             content = f.read()
#
#         content = content.replace(pidstroka, stroka)
#
#         with open(filename, 'w') as f:
#             f.write(content)
#
# def files():
#     global filenames
#     filenames = []
#     for i in range(100):
#         filename = f"papka_z_filamy_{i}.doc"
#         with open(filename, "w") as f:
#             f.write("Hi")
#         filenames.append(filename)
#         mutexes[filename] = Lock()
#
#     potoky = [Thread(target=add, args=(filename, 'Hi', 'Bye')) for filename in filenames]
#
#     for potik in potoky:
#         potik.start()
#
#     for potik in potoky:
#         potik.join()
#
#     for filename in filenames:
#         add(filename, 'Hi', 'Bye')
#
# start_time = perf_counter()
#
#
# files()
# end_time = perf_counter()
# print(f'Виконання зайняло {end_time - start_time:0.2f} секунд')
