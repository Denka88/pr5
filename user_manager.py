import json
import os

import sys


if not os.path.exists('users.json'):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump([], f, indent=4)
    print("Файл создан")

with open('users.json', 'r', encoding='utf-8') as f:
    users = json.load(f)



def show_all_users():
    if users is None:
        print("Список пользователей пуст")
    else:
        for user in users:
            print(f"|ID: {user['id']:<4}| {user['name']:<25}| {user['email']:<25}| {user['city']:<15}| {user['status']:<10}|")

def add_new_user():
    while True:
        name = input("Введите имя пользователя: ")
        if name is None:
            print("Неверное имя пользователя!")
            continue
        break
    while True:
        email = input("Введите email адрес пользователя: ")
        if email is None:
            print("Неверный email адрес!")
            continue
        if email in users:
            print("Email адрес занят другим пользователем!")
            continue
        if not email.find('@') != -1:
            print("Не обнаружено \"@\"")
            continue
        break
    while True:
        city = input("Введите город пользователя: ")
        if city is None:
            print("Неверный город")
            continue
        break
    while True:
        input_status = input("Выберите статус(active/inactive)(1/0): ")
        status = "active"
        if input_status == '1':
            status = "active"
        elif input_status == '0':
            status = "inactive"
        else:
            print("Выберите число 1 или 0!")
            continue
        break
    users.append({"id": len(users)+1, "name": name, "email": email, "city": city, "status": status})

def find_user_by_name():
    name = input("Введите имя для поиска: ")
    found_users = []
    for user in users:
        if name.lower() in user["name"].lower():
            found_users.append(user)

    if len(found_users) > 0:
        print("Найдены совпадения")
        print("-" * 20)
        for user in found_users:
            print(f"|ID: {user['id']:<4}| {user['name']:<25}| {user['email']:<25}| {user['city']:<15}| {user['status']:<10}|")
    else:
        print("Совпадения не найдены")

def delete_user_by_id():
    show_all_users()
    while True:
        try:
            id_for_delete = int(input("Введите ID для удаления: "))
        except ValueError:
            print("Это не число!")
        else:
            break

    if id_for_delete <= len(users):
        agreement = input("Подтвердить удаление(y/n): ")
        if agreement == 'y':
            deleted = users.pop(id_for_delete-1)
            print(f"Пользователь {deleted['name']} удален")
        else:
            print("Удаление отменено")
    else:
        print("ID нет в списке")

def change_status():
    show_all_users()
    id_for_change = int(input("Введите ID для смены статуса: "))

    changed = False
    for user in users:
        if id_for_change == user['id']:
            changed = True
            if user['status'] == "active":
                user['status'] = "inactive"
                print(f"|ID: {user['id']:<4}| {user['name']:<25}| {user['email']:<25}| {user['city']:<15}| {user['status']:<10}|")
            else:
                user['status'] = "active"
                print(f"|ID: {user['id']:<4}| {user['name']:<25}| {user['email']:<25}| {user['city']:<15}| {user['status']:<10}|")

            break
    if not changed:
        print("ID нет в списке")

def save_changes():
    users_new = json.dumps(users, indent=4, ensure_ascii=False)
    with open('users.json', 'w', encoding='utf-8') as f:
        f.write(users_new)
    print("Данные сохранены")

def menu(action):
    match action:
        case "1":
            show_all_users()
        case "2":
            add_new_user()
        case "3":
            find_user_by_name()
        case "4":
            delete_user_by_id()
        case "5":
            change_status()
        case "6":
            save_changes()


while True:
    print("\n------Меню------")
    print("1. Показать всех пользователей")
    print("2. Добавить нового пользователя")
    print("3. Найти пользователя по имени")
    print("4. Удалить пользователя по ID")
    print("5. Изменить статус пользователя")
    print("6. Сохранить изменения в файл")
    print("7. Выйти из программы")
    selected_action = input("Выберите действие: ")
    print("\n")

    if selected_action == "7":
        save_changes()
        sys.exit(0)
    else:
        menu(selected_action)