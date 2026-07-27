import os
from datetime import datetime

from pefile import count_zeroes


# pt = os.path.abspath('.')
# print(pt)
# p = os.path.join('data', 'test.txt')
# print(p)
# pt = os.path.abspath(p)
# print(pt)
# # os.mkdir('data')
# print(os.path.exists('data'))
# os.makedirs(r'C:\Users\Windows\PycharmProjects'
#             r'\acmay26\data\new', exist_ok=True)
# os.open(r'C:\Users\Windows\PycharmProjects'
#             r'\acmay26\data\new\new.txt',
#         os.O_CREAT)
# with open(r'C:\Users\Windows\PycharmProjects'
#             r'\acmay26\data\new\new.py', 'a', encoding='utf-8') as f:
#     pass
# t = os.path.getmtime(r'C:\Users\Windows\PycharmProjects'
#             r'\acmay26\data\new\new.txt')
# print(datetime.fromtimestamp(t))
# t = os.path.getmtime(r'C:\Users\Windows\PycharmProjects'
#             r'\acmay26\data\indata\indata.txt')
# print(datetime.fromtimestamp(t).strftime('%d-%m-%Y %X'))

def seek(target):
    if not os.path.exists(target):
        print(f'вызов должен быть из '
              f'корневого дирректория {os.path.abspath(".")}')
    count_folder = 0
    count_file = 0
    size = 0
    ps = os.path.join(target)
    p = os.path.abspath(ps)
    for i in os.listdir(p):
        ps = os.path.join(p, i)
        if os.path.isfile(ps):
            count_file += 1
            size += os.path.getsize(ps)
        else:
            count_folder += 1
            # size += os.path.getsize(ps)[0]
            cz, cf, cfl = seek(ps)
            size += cz
            count_folder += cf
            count_file += cfl
    return size, count_folder, count_file


print(seek('data'))