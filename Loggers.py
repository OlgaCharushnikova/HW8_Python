def find_data():
    surname = input('Введите фамилию: ')
    data = open('data.txt', 'r', encoding = 'utf - 8')
    for line in data:
        if surname in line:
            print(line)
    data.close


def new_data():
    surname = input('Введите фамилию:')
    name = input('Введите имя:')
    patronymic = input('Введите отчество:')
    phone_number = input('Введите номер телефона:')
    data = open('data.txt', 'a', encoding = 'utf - 8')
    data.write('\n')
    data.write(f'{surname} {name} {patronymic} {phone_number}')
    data.close
    print('Запись добавлена.')

def correction_data():
    replace_number = input('Для изменения данных нажмите: \n'
                                '1 - для изменения фамилии\n'
                                '2 - для изменения имени\n'
                                '3 - для изменения отчества\n'
                                '4 - для изменения номера телефона\n')
    if replace_number == '1':
        surname = input('Введите фамилию для корректировки данных: ')
        data = open('data.txt', 'r+', encoding = 'utf - 8')
        list_data = data.read()
        list_data = list_data.split()
        if surname in list_data:
            index = list_data.index(surname)
            new_surname = input('Введите новое имя: ')
            list_data[index] = new_surname
        data = open('data.txt', 'w', encoding = 'utf - 8')
        new_list_data = []
        i = 0
        j = 0
        while i < len(list_data):
            for j in range(4):
                surname = list_data[i]
                new_list_data.append(surname)
                new_list_data.append(' ')
                j += 1
                i += 1
            new_list_data.append('\n')
        data.writelines(new_list_data)
        data.close    

    if replace_number == '2':
        name = input('Введите имя для корректировки данных: ')
        data = open('data.txt', 'r+', encoding = 'utf - 8')
        list_data = data.read()
        list_data = list_data.split()
        if name in list_data:
            index = list_data.index(name)
            new_name = input('Введите новое имя: ')
            list_data[index] = new_name
        data = open('data.txt', 'w', encoding = 'utf - 8')
        new_list_data = []
        i = 0
        j = 0
        while i < len(list_data):
            for j in range(4):
                name = list_data[i]
                new_list_data.append(name)
                new_list_data.append(' ')
                j += 1
                i += 1
            new_list_data.append('\n')
        data.writelines(new_list_data)
        data.close 

    if replace_number == '3':
        patronymic = input('Введите отчество для корректировки данных: ')
        data = open('data.txt', 'r+', encoding = 'utf - 8')
        list_data = data.read()
        list_data = list_data.split()
        if patronymic in list_data:
            index = list_data.index(patronymic)
            new_patronymic = input('Введите новое отчество: ')
            list_data[index] = new_patronymic
        data = open('data.txt', 'w', encoding = 'utf - 8')
        new_list_data = []
        i = 0
        j = 0
        while i < len(list_data):
            for j in range(4):
                patronymic = list_data[i]
                new_list_data.append(patronymic)
                new_list_data.append(' ')
                j += 1
                i += 1
            new_list_data.append('\n')
        data.writelines(new_list_data)
        data.close  

    if replace_number == '4':
        phone_number = input('Введите номер телефона корректировки данных: ')
        data = open('data.txt', 'r+', encoding = 'utf - 8')
        list_data = data.read()
        list_data = list_data.split()
        if phone_number in list_data:
            index = list_data.index(phone_number)
            new_phone_number = input('Введите новый номер телефона: ')
            list_data[index] = new_phone_number
        data = open('data.txt', 'w', encoding = 'utf - 8')
        new_list_data = []
        i = 0
        j = 0
        while i < len(list_data):
            for j in range(4):
                phone_number = list_data[i]
                new_list_data.append(phone_number)
                new_list_data.append(' ')
                j += 1
                i += 1
            new_list_data.append('\n')
        data.writelines(new_list_data)
        data.close 
    print('Запись отредактирована.')


def delete_data():
    surname = input('Введите фамилию: ')
    data = open('data.txt', 'r', encoding = 'utf - 8')
    list_phon_numbers = []
    for line in data:
        if surname not in line:
            l = str(line)
            list_phon_numbers.append(l)
    data = open('data.txt', 'w', encoding = 'utf - 8')
    data.writelines(list_phon_numbers)
    data.close
    print('Запись удалена.')




