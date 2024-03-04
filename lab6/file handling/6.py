import os

def create_text_files():
    # Получаем список букв от A до Z
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Перебираем буквы и создаем файлы
    for letter in alphabet:
        file_name = f"{letter}.txt"
        try:
            # Полный путь к файлу
            full_path = os.path.join(os.getcwd(), file_name)

            # Создаем и открываем файл для записи ('w' - режим записи)
            with open(full_path, 'w') as file:
                file.write(f"Привет, это файл {file_name}!")
            print(f"Файл '{file_name}' успешно создан по пути: {full_path}")
        except Exception as e:
            print(f"Произошла ошибка при создании файла {file_name}: {e}")

def main():
    create_text_files()

if __name__ == "__main__":
    main()
    
'''import os: Импортируем модуль os, который предоставляет функции для работы с операционной системой.

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': Создаем строку, представляющую алфавит в верхнем регистре.

for letter in alphabet:: Запускаем цикл for, чтобы перебирать каждую букву в алфавите.

file_name = f"{letter}.txt": Создаем имя файла, добавляя текущую букву к расширению ".txt".

full_path = os.path.join(os.getcwd(), file_name): Создаем полный путь к файлу, используя текущую рабочую директорию и имя файла.

with open(full_path, 'w') as file:: Открываем файл для записи с использованием контекстного менеджера, 
чтобы гарантировать корректное закрытие файла.

file.write(f"Привет, это файл {file_name}!"): Записываем в файл приветственное сообщение, включающее имя файла.

print(f"Файл '{file_name}' успешно создан по пути: {full_path}"): Выводим сообщение о успешном создании файла, включая его имя и полный путь.

except Exception as e:: Если происходит ошибка при создании файла, выводим сообщение об ошибке.

def main(): и if __name__ == "__main__":: Определяем функцию main(), которая вызывает create_text_files(). 
Это обеспечивает выполнение программы только при ее запуске напрямую, а не при импорте в другой скрипт.'''