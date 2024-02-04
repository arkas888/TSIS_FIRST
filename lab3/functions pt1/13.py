import random

def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()
    
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        player_guess = int(input())
        guesses_taken += 1

        if player_guess < secret_number:
            print("Your guess is too low.")
        elif player_guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {guesses_taken} guesses!")
            break

# Run the game
guess_the_number()


'''Ниже представлена простая программа на Python для игры "Угадай число":

1. Импортирован модуль random для генерации случайных чисел.
2. Определена функция guess_the_number без параметров.
3. Запросено у пользователя имя и сохранено в переменной player_name.
4. Выведено приветствие с использованием имени игрока и загадано случайное число от 1 до 20.
5. В цикле while игроку предлагается угадать число.
6. После каждой попытки выводится подсказка, слишком низкое или слишком высокое число.
7. Если угадано правильное число, программа завершает цикл и поздравляет игрока.

Пример использования программы:
Введите имя: KBTU
Пример вывода:
Добро пожаловать, KBTU! Я загадал число от 1 до 20.
Угадайте число.
12
Ваша догадка слишком низкая.
Угадайте число.
16
Ваша догадка слишком низкая.
Угадайте число.
19
Отличная работа, KBTU! Вы угадали мое число за 3 попытки!
Эта программа создает случайное число от 1 до 20 и предлагает игроку угадать его, 
предоставляя подсказки о том, слишком низкое или слишком высокое введенное число. Программа завершается, когда игрок угадывает число.
'''