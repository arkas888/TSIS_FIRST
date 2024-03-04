import os

def list_directories(path):
    # Получаем список каталогов в указанном пути
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):
    # Получаем список файлов в указанном пути
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all_contents(path):
    # Получаем список всех каталогов и файлов в указанном пути
    all_contents = os.listdir(path)
    return all_contents

def main():
    specified_path = input("Введите путь к директории: ")

    if os.path.exists(specified_path):
        print("\nСписок каталогов:")
        print(list_directories(specified_path))

        print("\nСписок файлов:")
        print(list_files(specified_path))

        print("\nСписок всех каталогов и файлов:")
        print(list_all_contents(specified_path))
    else:
        print("Указанный путь не существует.")

if __name__ == "__main__":
    main()
    
'''Импортируем модуль os для работы с операционной системой.

Создаем три функции:

list_directories(path): возвращает список каталогов в указанном пути.
list_files(path): возвращает список файлов в указанном пути.
list_all_contents(path): возвращает список всех каталогов и файлов в указанном пути.
В функции main() запрашиваем у пользователя ввод пути к директории.

Проверяем, существует ли указанный путь (os.path.exists(specified_path)).

Если путь существует, выводим три списка:

Список каталогов.
Список файлов.
Список всех каталогов и файлов.
Если путь не существует, выводим сообщение об ошибке.

Если программа запускается как основная, вызываем main().'''