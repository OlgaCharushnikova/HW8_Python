from Loggers import find_data, new_data, correction_data, delete_data

def interface():
      print('Для работы с программой выберите нужное действие:')
      print('1 - найти запись\n'
            '2 - создать новую запись\n'
            '3 - редактировать запись\n'
            '4 - удалить запись запись\n'
            '5 - завершение работы\n')
      while True:
            comand  = int(input('Введите цифру, соответствующую команде:'))
            if comand not in (1, 2, 3, 4, 5):
                  print('Такой команды не существует!')
                  print(' ')
                  interface()
            elif comand == 1:
                  find_data()
            elif comand == 2:
                  new_data()
            elif comand == 3:
                  correction_data()
            elif comand == 4:
                  delete_data()      
            elif comand == 5:
                  return  
   
if __name__ == '__main__':
      interface()

# phone_book = ['Иванов', 'Иван', 'Иванович', '9999999999']
# phone_book = ' '.join(phone_book)
# data = open('data.txt', 'w', encoding = 'utf - 8')
# data.writelines(phone_book)
# data.close
