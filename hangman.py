
from hangman_life import game_name
import random

# All the words to be guessed consist of six Letters
guess_list = ['Almond', 'Banana', 'Blewits', 'Brazil', 'Carrot', 'Casaba', 'Cashew', 'Celery', 'Cherry', 'Chives',
              'Chocho', 'Citron', 'Citrus', 'Cob nut', 'Cooker', 'Daikon', 'Damson', 'Endive', 'Fennel', 'Garlic', 'Girkin',
              'Greens', 'Kiwano', 'Lentil', 'Lichee', 'Lychee', 'Marrow', 'Medlar', 'Nettle', 'Orange', 'Oyster', 'Papaya',
              'Pawpaw', 'Peanut', 'Pepper', 'Pignut', 'Pippin', 'Potato', 'Quince', 'Radish', 'Raisin', 'Rocket', 'Russet', 'Squash', 'Tomato', 'Turnip', 'Wakame', 'Walnut']

# Chosse Random Name From guess_list
guess_word = random.choice(guess_list).lower()
word_letters = len(guess_word)

game_over = False
tries = 6
print(game_name)
print(f'The word You Guessed is : {guess_word}')

result = []

for _ in range(word_letters):
    result +='_'

while not game_over:
    user_guessing = input('Guess a Letter: ')

    if user_guessing in result:
        print(f'The letter you have guessed is: {user_guessing}')

    for position in range(word_letters):
        letter = guess_word[position]
        if letter == user_guessing:
            result[position] = letter

    if user_guessing not in guess_word:
        print(f'You guessed {user_guessing}, This letter not in the word, you lose a try')
        tries-=1

        if tries == 0:
            game_over = True
            print(f'Game Over, You lose the game, try again later')
    print(f'{" ".join(result)}')

    if '_' not in result:
        game_over=True
        print('You Are a Winner, Congratulations')

    from hangman_life import lives
    print(lives[tries])