import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)


place_holder = ''

for position in range(len(chosen_word)):
    place_holder += '_'
print("Word to guess : "+place_holder)

game_over = False

correct_letters = []

while not game_over:
    print(f"*****************{lives}/6 LIVES LEFT**************************")
    guess = input("guess a word : ").lower()

    if guess in correct_letters:
        print(f"You've already guessed a letter {guess}")

    display = ''

    for letters in chosen_word:
        if letters == guess:
            display += letters
            correct_letters.append(letters)
        elif letters in correct_letters:
            display += letters
        else:
            display += '_'



    print("Word to guess: " +display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("**********************You Lost A Game.***************************")

    if '_' not in display:
        game_over = True
        print('**************************You Won A Game.****************************')

    print(stages[lives])
