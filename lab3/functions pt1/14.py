# main_program.py

# Importing functions from the tasks
from task1 import grams_to_ounces
from task2 import fahrenheit_to_centigrade
from task3 import solve
from task4 import filter_prime
from task5 import print_permutations
from task6 import reverse_sentence
from task7 import has_33
from task8 import spy_game
from task9 import sphere_volume
from task10 import unique_elements
from task11 import is_palindrome
from task12 import histogram
from task13 import guess_the_number

def main():
    # Example usage of the imported functions

    # Task 1: Grams to Ounces
    grams_value = 500
    ounces_value = grams_to_ounces(grams_value)
    print(f"{grams_value} grams is equal to {ounces_value:.2f} ounces.")

    # Task 2: Fahrenheit to Centigrade
    fahrenheit_temp = 75
    centigrade_temp = fahrenheit_to_centigrade(fahrenheit_temp)
    print(f"{fahrenheit_temp} Fahrenheit is equal to {centigrade_temp:.2f} Centigrade.")

    # Task 3: Solve
    heads = 35
    legs = 94
    solution = solve(heads, legs)
    print("Number of Chickens and Rabbits:", solution)

    # Task 4: Filter Prime Numbers
    numbers = [2, 3, 5, 8, 13, 15, 17, 20]
    prime_numbers = filter_prime(numbers)
    print("Prime Numbers:", prime_numbers)

    # Task 5: Print Permutations
    input_string = "abc"
    permutations = print_permutations(input_string)
    print(f"Permutations of '{input_string}': {permutations}")

    # Task 6: Reverse Sentence
    input_sentence = "Hello, World!"
    reversed_sentence = reverse_sentence(input_sentence)
    print(f"Reversed sentence: {reversed_sentence}")

    # Task 7: Has 33
    sequence1 = [1, 3, 3]
    sequence2 = [1, 3, 1, 3]
    sequence3 = [3, 1, 3]

    print("Has 33 in sequence1:", has_33(sequence1))
    print("Has 33 in sequence2:", has_33(sequence2))
    print("Has 33 in sequence3:", has_33(sequence3))

    # Task 8: Spy Game
    spy_game_result = spy_game([1, 3, 0, 0, 7, 5])
    print("Spy Game Result:", spy_game_result)

    # Task 9: Sphere Volume
    sphere_radius = 4
    sphere_volume_result = sphere_volume(sphere_radius)
    print(f"Volume of a sphere with radius {sphere_radius}:", sphere_volume_result)

    # Task 10: Unique Elements
    original_list = [1, 2, 3, 1, 2, 4, 5]
    unique_list = unique_elements(original_list)
    print("Original List:", original_list)
    print("List with Unique Elements:", unique_list)

    # Task 11: Is Palindrome
    word = "madam"
    palindrome_result = is_palindrome(word)
    print(f"{word} is a palindrome: {palindrome_result}")

    # Task 12: Histogram
    histogram([4, 9, 7])

    # Task 13: Guess the Number
    guess_the_number()

if __name__ == "__main__":
    main()
    
    '''Эта программа демонстрирует использование различных функций из предоставленных задач в новой программе.'''