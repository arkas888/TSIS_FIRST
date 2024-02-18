from datetime import datetime

# Input two date strings
date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

# Convert date strings to datetime objects
date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

# Calculate the difference in seconds
time_difference = abs((date2 - date1).total_seconds())

# Print the results
print(f"Difference between the two dates in seconds: {time_difference} seconds")


'''Программа принимает две строки даты в формате "YYYY-MM-DD HH:MM:SS" в качестве входных данных.
Она использует метод datetime.strptime для преобразования этих строк в объекты datetime.
Разница между двумя датами вычисляется с использованием оператора -, и метод total_seconds() используется для получения разницы в секундах.
Берется абсолютное значение для обработки случаев, когда вторая дата раньше первой.
Результат выводится, показывая разницу между двумя датами в секундах.'''