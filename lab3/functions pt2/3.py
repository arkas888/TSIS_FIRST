def filter_movies_by_category(movie_list, category):
    # Фильтруем фильмы по заданной категории
    movies_in_category = [movie for movie in movie_list if movie["category"] == category]
    return movies_in_category

# Пример использования функции:
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    # ... другие фильмы ...
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

target_category = "Romance"
movies_in_target_category = filter_movies_by_category(movies, target_category)
print(f"Фильмы в категории '{target_category}':")
for movie in movies_in_target_category:
    print(f"{movie['name']} - IMDB: {movie['imdb']}, Category: {movie['category']}")


'''1. Определена функция filter_movies_by_category, которая принимает список фильмов и название категории, затем возвращает подсписок фильмов, принадлежащих заданной категории.
2. В теле функции используется списковое включение для фильтрации фильмов. Создается новый список movies_in_category, включающий только те фильмы, у которых категория совпадает с заданной.
3. Функция возвращает подсписок movies_in_category.
4. Приведен пример использования функции с заданным списком фильмов и категорией. Выводится информация о фильмах в заданной категории.
Таким образом, эта функция позволяет фильтровать список фильмов и возвращать только те, которые принадлежат заданной категории.'''