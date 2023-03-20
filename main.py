import os
import sys
import shutil



def get_dir(): #Получение дириктории
 pass
def create():
    name=input('введите название папки')
    os.mkdir(name)
    return 0
def delete_folder():
    name=input('Введите папку которую хотите удалить')
    os.rmdir(name)
    pass
def copy():
    name_old=input('Ввелите имя файла/папки, который хотите копировать')
    name_new = input('Ввелите новое имя файла/папки')
    shutil.copy(name_old, name_new)
    pass
def look_dir():
    print(os.listdir())
    pass
def look(c):
    print(c)
    path=os.getcwd()
    print(path)
    for dirs, folder,files in os.walk(path):
        if c =='4': print('Выбранный каталог', dirs)
        elif c=='5': print('Папки', folder)
        elif c=='6': print('Файлы', files)
    pass
def look_files():
    path = os.getcwd()
    for folder in os.walk(path):
        print(folder)
    pass
def play_games(i):
    if i=='9':
        import Victory
    else: import Wallet
####
i=input('''Что необходимо слелать?
1-создать папку+
2-удалить (файл/папку)+
3-копировать (файл/папку)+
4-просмотр содержимого рабочей директории+
5-посмотреть только папки
6-посмотреть только файлы
7-просмотр информации об операционной системе
8-создатель программы
9-играть в викторину
10-мой банковский счет
11-смена рабочей директории
0-выход\n''')
###


if i=='1':
    create()
elif i=='2':
    delete_folder()
elif i=='3':
    copy()
elif i=='4':
    look(i)
elif i=='5':
    look(i)
elif i=='6':
    look(i)
elif i=='7':
    print(sys.platform)
elif i=='8':
    print(Alex)
elif i=='9':
    play_games(i)
elif i=='10':
    play_games(i)
elif i=='11':
    print(os.getcwd())
    os.chdir(input('Введите путь к новой дириктории'))
    print(os.getcwd())
else:
    print('Досвидания')
    pass