from datetime import datetime

# Get the current date and time with microseconds
current_datetime = datetime.now()

# Drop microseconds
rounded_datetime = current_datetime.replace(microsecond=0)

# Print the results
print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", rounded_datetime)

'''Программа использует модуль datetime для работы с датами и временем.
Получает текущую дату и время с микросекундами с помощью функции datetime.now().
Затем создает новую дату и время, убирая микросекунды с использованием метода replace и установки microsecond в 0.
Оригинальная и измененная даты и времени выводятся, чтобы показать разницу.'''