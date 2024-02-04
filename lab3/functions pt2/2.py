def filter_high_imdb_movies(movie_list):
    # Фильтруем фильмы с рейтингом IMDB выше 5.5
    high_imdb_movies = [movie for movie in movie_list if movie["imdb"] > 5.5]
    return high_imdb_movies

# Пример использования функции:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    # ... другие фильмы ...
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

high_imdb_movies = filter_high_imdb_movies(movies)
print("Фильмы с рейтингом IMDB выше 5.5:")
for movie in high_imdb_movies:
    print(f"{movie['name']} - IMDB: {movie['imdb']}, Category: {movie['category']}")

'''1. Определена функция filter_high_imdb_movies, которая принимает список фильмов и возвращает подсписок фильмов с рейтингом IMDB выше 5.5.
2. В теле функции используется списковое включение для фильтрации фильмов. Создается новый список high_imdb_movies, 
включающий только те фильмы, у которых рейтинг IMDB больше 5.5.
3. Функция возвращает подсписок high_imdb_movies.
4. Приведен пример использования функции с заданным списком фильмов. Выводится информация о фильмах с рейтингом IMDB выше 5.5.
Таким образом, эта функция фильтрует список фильмов, оставляя только те, у которых рейтинг IMDB превышает 5.5, и возвращает новый список.
'''