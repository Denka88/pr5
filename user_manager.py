import sys

def menu(action):
    match action:
        case "1":
            print("hi")



while True:
    print("------Меню------")
    print("1. Показать всех пользователей")
    print("2. Добавить нового пользователя")
    print("3. Найти пользователя по имени")
    print("4. Удалить пользователя по ID")
    print("5. Изменить статус пользователя")
    print("6. Сохранить изменения в файл")
    print("7. Выйти из программы")
    selected_action = input("Выберите действие: ")
    print("\n")

    if selected_action == "0":
        sys.exit(0)
    else:
        menu(selected_action)