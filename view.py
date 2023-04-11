import text_fields as txt

def main_menu() -> int:
    print(''' Главное меню:
    1. Открыть
    2. Сохранить
    3. Показать все
    4. Создать
    5. Найти
    6. Изменить
    7. Удалить
    8. Выход''')

    choice = ''

    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Введите число от 1 до 9')
    
def show_contacts(book : list[dict], message : str):
    if book:
        for n, contact in enumerate(book,1):
            print(f'{n}.{contact.get("name"):<20}'
                    f'{contact.get("phone"):<20}'
                    f'{contact.get("comment"):<20}')
    else:
        print(message)

def print_info(message:str):
    print('\n' + '-'*len(message))
    print(message)
    print('-'*len(message) + '\n')

def new_contact() -> dict:
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    return {'name':name,
            'phone':phone,
            'comment': comment}

def confirm(message: str) -> bool:
    answer = input(message + ' (y/n)?')
    if answer.lower() == 'y':
        return True
    else:
        return False