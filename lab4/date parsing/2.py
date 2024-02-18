from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Calculate yesterday and tomorrow
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))


'''Программа использует модуль datetime для работы с датами и временем.
Получает текущую дату и время с использованием функции datetime.now().
Затем вычисляет вчерашнюю и завтрашнюю дату, вычитая и добавляя один день к текущей дате с помощью timedelta(days=1), соответственно.
Результаты выводятся отформатированно, отображая вчерашнюю, текущую и завтрашнюю даты.'''