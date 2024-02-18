import json

# Загрузка данных из файла JSON
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Форматированный вывод
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Итерация по данным и вывод информации
for entry in data:
    dn = entry.get('attributes', {}).get('dn', '')
    description = entry.get('attributes', {}).get('descr', '')
    speed = entry.get('attributes', {}).get('speed', 'inherit')
    mtu = entry.get('attributes', {}).get('mtu', '')

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
    
'''Мы начинаем с открытия файла sample-data.json и загрузки его содержимого в переменную data с использованием модуля json.
Затем мы форматируем вывод, создавая таблицу с заголовками столбцов.
Используя цикл for, мы проходим по данным и извлекаем необходимую информацию (DN, Description, Speed, MTU) из каждой записи.
Далее, мы выводим отформатированную строку для каждой записи данных, соответствующую столбцам таблицы.
Программа выводит информацию о состоянии интерфейсов в формате, подобном указанному в упражнении.'''