from random import randint

array_character = ["Выход", "Камень", "Ножницы", "Бумага"]


# Ввод игроком одного "персонажа" игры; проверка на число.
def enter_character():
    print("Введите соотетствующую цифру. Для выхода из программы введите 0.")
    while 1:
        try:
            choice_player = int(input("\t1. Камень\n\t2. Ножницы\n\t3. Бумага\nВведите цифру: "))
            if choice_player in (range(0, 4)):
                return choice_player
            else:
                print("Цифра должна быть от 1 до 3.\nПопробуйте еще раз. Для выхода из программы введите 0.")
        except ValueError:
            print("Неправильный ввод! Введите цифру еще раз (от 1 до 3). Для выхода из программы введите 0.")


# Создание рандомного "персонажа" игры компьютером.
def create_pc_character():
    choice_pc = randint(1, 3)
    return choice_pc


# Заметка: посмотреть про словари (вместо условий)
def game():
    while 1:
        choice_player = array_character[enter_character()]
        choice_pc = array_character[create_pc_character()]
        if choice_player == choice_pc:
            result = "Ничья.\n"
        elif ((choice_player == "Камень") and (choice_pc == "Ножницы")) or ((choice_player == "Ножницы") and (choice_pc == "Бумага")) or ((choice_player == "Бумага") and (choice_pc == "Камень")):
            result = "Вы выиграли!\n"
        elif choice_player == "Выход":
            exit()
        else:
            result = "Вы проиграли.\n"
        print("Вы выбрали: ", choice_player)
        print("Компьютер выбрал: ", choice_pc)
        print(result)


game()
