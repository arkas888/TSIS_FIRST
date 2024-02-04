def is_high_imdb_score(movie):
    # Проверяем, если рейтинг IMDB фильма выше 5.5
    return movie["imdb"] > 5.5

# Пример использования функции:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    # ... другие фильмы ...
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

for movie in movies:
    result = is_high_imdb_score(movie)
    print(f"{movie['name']}: IMDB score above 5.5? {result}")


'''1. Определена функция is_high_imdb_score, которая принимает фильм в виде словаря и возвращает True, если его рейтинг IMDB выше 5.5.
2. В теле функции используется выражение movie["imdb"], чтобы получить значение рейтинга IMDB из словаря фильма.
3. Функция возвращает результат сравнения рейтинга IMDB с пороговым значением 5.5.
4. Приведен пример использования функции с небольшим списком фильмов. 
Для каждого фильма выводится информация о том, превышает ли его рейтинг IMDB 5.5.
Таким образом, эта функция просто проверяет, превышает ли рейтинг IMDB фильма заданный порог (в данном случае, 5.5), 
и возвращает соответствующее булево значение.
'''