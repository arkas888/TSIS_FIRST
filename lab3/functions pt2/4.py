def calculate_average_imdb_score(movie_list):
    # Проверка на пустой список
    if not movie_list:
        return None

    # Вычисляем средний рейтинг IMDB
    total_imdb_score = sum(movie["imdb"] for movie in movie_list)
    average_imdb_score = total_imdb_score / len(movie_list)
    return average_imdb_score

# Пример использования функции:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    # ... другие фильмы ...
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

average_score = calculate_average_imdb_score(movies)

if average_score is not None:
    print(f"Средний рейтинг IMDB для списка фильмов: {average_score:.2f}")
else:
    print("Список фильмов пуст.")


'''1. Определена функция calculate_average_imdb_score, которая принимает список фильмов и возвращает средний рейтинг IMDB.
2. Внутри функции осуществляется проверка на пустой список. Если список пуст, функция возвращает None.
3. Для вычисления среднего рейтинга IMDB используется сумма рейтингов всех фильмов и деление на количество фильмов.
4. Функция возвращает средний рейтинг IMDB.
5. Приведен пример использования функции с заданным списком фильмов. Выводится средний рейтинг IMDB для списка фильмов.
Таким образом, эта функция позволяет вычислить средний рейтинг IMDB для заданного списка фильмов.'''