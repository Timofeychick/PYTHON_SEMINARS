
def user_choice():   # ГЛАВНОЕ МЕНЮ И ВЫБОР ДЕЙСТВИЯ ДЛЯ ФУНКЦИИ "action()"
    print("1. <Посмотреть телефонную книгу>\n2. <Добавить запись в телефонную книгу вручную> \n3. <Импортировать контакты из другой книги>\n4. <Найти контакт>\n5. <Завершить работу программы>\n")
    point = int(input("Выберите действие: "))
    if (1 <= point <= 5):
        return point
    else:
        print("Неккоректный ввод, повторите")
        
def action(point): # ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ОСУЩЕСТВЛЕНИЯ ДЕЙСТВИЯ
    point = user_choice()
    if (point == 1):
        show_contacts()
    if (point == 2):
        add_new_contacts()
    if (point == 3):
        import_tel_book()
    if (point == 4):
        find_contact()
    if (point == 5):
        print("\n<работа с телефонной книгой завершена>")
        
def show_contacts(): # ФУНКЦИЯ ОТКРЫВАЮЩАЯ ФАЙЛ С КОНТАКТАМИ
    with open("contacts_book.txt", 'r', encoding = 'utf=8') as file:
        text = file.read()
        print(text) 
        file.close()
    print('---------- \n')
    action(user_choice)
    
def add_new_contacts(): # ДОБАВЛЕНИЕ КОНТАКТОВ В ФАЙЛ
        amount = int(input("Сколько контактов вы хотите добавить: "))
        print("\n")
        counter = int(0)
        while counter < amount:
            with open("contacts_book.txt", 'a', encoding = 'utf=8') as file:
                new_name = str(input("Введите ФИО: "))
                new_number = str(input("Введите номер телефона: "))
                file.write(new_name + ' - ' + new_number + '\n' ) 
                file.close()
            counter += 1 
        print('---------- \n')
        action(user_choice)
       
def import_tel_book(): # ИМПОРТ ОДНОГО ФАЙЛА В ДРУГОЙ
    new_contacts = str(input("Введите путь до файла: "))
    open("contacts_book.txt", 'a', encoding = 'utf=8').write(open(new_contacts, "r").read() + '\n')
    print('---------- \n')
    action(user_choice)
    
def find_contact(): # ПОИСК КОНТАКТОВ ПО ЗАПРОСУ ФАМИЛИИ ИЛИ ИМЕНИ ИЛИ ОТЧЕСВТУ
    with open ("contacts_book.txt", 'r+', encoding = 'utf=8') as file:
        contact = str(input("Введите имя / фамилию / отчество для поиска контакта: "))
        print('\n')
        text = file.readlines()
        list_cont = [] # номера линий в которых встречается указанное имя
        line_index = int(0) # индекс линии
        index = int(1)
        
        for line in text: # здесь 'line' - это отдельная строка
            split_line = line.split() # разделяем строку на отдельные слова (строка разбитая на слова)
        
            for one_word in split_line: # здесь элемент (one_word) - это слово в строке
                if one_word == contact:
                    list_cont.append(line_index)
                    print('Контакт найден! Вот все его данные: ')
                    print(f"{index}. {line}\n")
                    index += 1
            line_index += 1  
        if(line_index == 0): print("Контакт не найден")  
        #print(list_cont)
    action(user_choice)
    
def start(): # СТАРТ ПРОГРАММЫ
    print("\n<начало работы с телефонной книгой> \n")
    action(user_choice)


start()

      
