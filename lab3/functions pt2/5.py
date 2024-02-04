def calculate_average_imdb_score_by_category(movie_list, category):
    # Проверка на пустой список
    if not movie_list:
        return None

    # Фильтруем фильмы по заданной категории
    movies_in_category = [movie for movie in movie_list if movie["category"] == category]

    # Проверка на пустой подсписок по заданной категории
    if not movies_in_category:
        return None

    # Вычисляем средний рейтинг IMDB для фильмов в заданной категории
    total_imdb_score = sum(movie["imdb"] for movie in movies_in_category)
    average_imdb_score = total_imdb_score / len(movies_in_category)
    return average_imdb_score

# Пример использования функции:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    # ... другие фильмы ...
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

target_category = "Romance"
average_score_in_category = calculate_average_imdb_score_by_category(movies, target_category)

if average_score_in_category is not None:
    print(f"Средний рейтинг IMDB для категории '{target_category}': {average_score_in_category:.2f}")
else:
    print(f"Фильмов в категории '{target_category}' не найдено или список фильмов пуст.")


'''1. Определена функция calculate_average_imdb_score_by_category, которая принимает список фильмов и название категории, 
затем возвращает средний рейтинг IMDB для фильмов в этой категории.
2. Внутри функции осуществляется проверка на пустой список. Если список пуст, функция возвращает None.
3. Затем фильмы фильтруются по заданной категории, и также осуществляется проверка на пустой подсписок по заданной категории.
Если подсписок пуст, функция также возвращает None.
4. Для вычисления среднего рейтинга IMDB используется сумма рейтингов фильмов в заданной категории и 
деление на количество фильмов в этой категории.
5. Функция возвращает средний рейтинг IMDB для фильмов в заданной категории.
6. Приведен пример использования функции с заданным списком фильмов и категорией. 
Выводится средний рейтинг IMDB для фильмов в заданной категории.
Таким образом, эта функция позволяет вычислить средний рейтинг IMDB для фильмов в заданной категории.
'''