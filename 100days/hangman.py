#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input('Guess a letter: ').lower()


