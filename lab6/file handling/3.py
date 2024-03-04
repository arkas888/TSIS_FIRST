import os

def analyze_path(path):
    # Проверяем существование пути
    if os.path.exists(path):
        print(f"Путь '{path}' существует.")

        # Получаем имя файла из пути
        filename = os.path.basename(path)
        print(f"Имя файла: {filename}")

        # Получаем директорию из пути
        directory = os.path.dirname(path)
        print(f"Директория: {directory}")
    else:
        print(f"Путь '{path}' не существует.")

def main():
    specified_path = input("Введите путь для анализа: ")
    analyze_path(specified_path)

if __name__ == "__main__":
    main()
    
'''Импортируем модуль os для работы с операционной системой.

Создаем функцию analyze_path(path), которая принимает путь и анализирует его.

Проверяем существование пути с использованием os.path.exists().

Если путь существует, используем os.path.basename() для получения имени файла из пути и os.path.dirname() для получения директории.

Функция выводит соответствующие сообщения, включая имя файла и директорию.

В функции main() запрашиваем у пользователя ввод пути для анализа.

Если программа запускается как основная, вызываем main().'''