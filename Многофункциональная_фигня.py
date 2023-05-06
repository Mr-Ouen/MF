import time
from random import randint

device = input('какое устройство используешь? \n 1 - комп\n 2 - телефон')
print('\n')
right = str(randint(1, 100))
print('пароль (сам думай от чего):' + right)
print('Бабл квас ----(... что?)')
print('Привет, я Даки, и я могу выполнить эти действия. выбери действие:')
while True:
    user_action = input('1 - создать файл, \n 2 - удалить его, \n 3 - создать файл с рандомным содержимым, \n 4 - забить память, \n 5 - взломать пентагон, \n 6 - установить Майнкрафт, \n 7 - ответить на вопрос о жизни, вселеной, и вообще, \n 0 - выйти из проги нафиг')
    if user_action == '1':
        if device == '2':
            file_name = input('введите имя файла:')
            content = input('что будет в файле?')
            file = open(file_name + '.txt', 'w')
            file.write(content)
            input('нажмите любую клавишу,чтобы завершить создание')
            file.close()
            print('файл создан. еще один?')
        else:
            file_name = input('введите имя файла:')
            content = input('что будет в файле?')
            file = open('C:\\' + file_name + '.txt', 'w')
            file.write(content)
            input('нажмите любую клавишу,чтобы завершить создание')
            file.close()
            print('файл создан. еще один?')
    else:
        if user_action == '3':
            if device == '2':
                random_file = open(str(randint(1,100000000000)) + '.txt', 'w')
                random_file.write(str(randint(1,10000000000000000)))
                random_file.close()
                print('рандомный файл создан')
            else:
                random_file = open('C:\\' + str(randint(1,100000000000)) + '.txt', 'w')
                random_file.write(str(randint(1,10000000000000000)))
                random_file.close()
                print('рандомный файл создан')
        else:
            if user_action == '4':
                if device == '2':
                    while True:
                        print('память забивается...')
                        full = open(str(randint(1,100000)) + '.txt', 'w')
                        full.write('9999999999999999999999999999999')
                        full.close()
                else:
                    while True:
                        print('память забивается...')
                        full = open('C:\\' + str(randint(1,100000)) + '.txt', 'w')
                        full.write('9999999999999999999999999999999')
                        full.close()
            else:
                if user_action == '5':
                    password = input('введите пароль для взлома>>>')
                    if password == right:
                        while True:
                            print(randint(0, 1))
                    else:
                        print('<Неверный пароль. Взлом отменен.>')
                else:
                    if user_action == '2':
                        print('ФИГ ТЕБЕ,А НЕ УДАЛЕНИЕ ФАЙЛА!')
                    else:
                        if user_action == '6':
                            if device == '2':
                                print('установка Майнкрафта...')
                                time.sleep(5)
                                minecraft = open('minecraft.apk', 'w')
                                minecraft.write(str(randint(1, 9999999999999999999999999999999999)))
                                minecraft.close()
                                print('майнкрафт установлен в папку внутренной памяти')
                            else:
                                print('установка Майнкрафта...')
                                time.sleep(5)
                                minecraft = open('C:\\' + 'minecraft.exe', 'w')
                                minecraft.write(str(randint(1, 9999999999999999999999999999999999)))
                                minecraft.close()
                                print('майнкрафт установлен на диск C.')
                        else:
                            if user_action == '7':
                                if device == '2':
                                    print('возвращайся сюда же, в это же время, через 40000 лет (секунд).')
                                    wait = 40000
                                    while not wait == 0:
                                        wait -= 1
                                        time.sleep(1)
                                        print('осталось', wait, 'лет')
                                    sorok_dva = open('Смысл жизни,вселенной, и вообще.txt', 'w')
                                    sorok_dva.write('42')
                                    sorok_dva.close()
                                    print('ответ в коренной папке')
                                else:
                                    print('возвращайся сюда же, в это же время, через 40000 лет (секунд).')
                                    wait = 40000
                                    while not wait == 0:
                                        wait -= 1
                                        time.sleep(1)
                                        print('осталось', wait, 'лет')
                                    sorok_dva = open('C:\\' + 'Смысл жизни,вселенной, и вообще.txt', 'w')
                                    sorok_dva.write('42')
                                    sorok_dva.close()
                                    print('ответ на диске C.')
                            else:
                                if user_action == '0':
                                    exit()
                                else:
                                    print('ФИГ ТЕБЕ,А НЕ ФАЙЛ!')
            