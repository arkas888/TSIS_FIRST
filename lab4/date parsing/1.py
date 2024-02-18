from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days
new_date = current_date - timedelta(days=5)

# Print the results
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("New Date (after subtracting five days):", new_date.strftime("%Y-%m-%d"))


'''Программа использует модуль datetime для работы с датами и временем.
Получает текущую дату и время с использованием функции datetime.now().
Затем вычитает пять дней из текущей даты с помощью timedelta(days=5).
Результаты выводятся отформатированно, отображая как текущую дату, так и новую дату после вычитания пяти дней.'''