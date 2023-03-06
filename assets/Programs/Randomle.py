import string
import random

# Define the set of characters available on an English keyboard

let = [' '] * 5
st1 = st2 = [' '] * 5

# Generate a random 5-character target word using the keyboard_chars set
target_word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890`~!@#$%^&()-=[]{}\;:,<.>/?+', k=5))
print(f'Target word: {target_word}')

# Initialize the number of failed attempts to 0
num_failures = 0

# Prompt the user for guesses until they guess the target word or reach 6 failed attempts
while True:
    print(f' ___ ___ ___ ___ ___ \n|{st1[0]}{let[0]}{st2[0]}|{st1[1]}{let[1]}{st2[1]}|{st1[2]}{let[2]}{st2[2]}|{st1[3]}{let[3]}{st2[3]}|{st1[4]}{let[4]}{st2[4]}| \n ___ ___ ___ ___ ___ \n')
    let = [' '] * 5
    st1 = st2 = [' '] * 5
    guess = input('Enter your guess: ')

    # Check if the guess is the same length as the target word
    if len(guess) != len(target_word):
        print(f'Your guess must be {len(target_word)} letters long')
        continue

    # Check if the guess matches the target word
    if guess == target_word:
        print(f' ___ ___ ___ ___ ___ \n|{st1[0]}{let[0]}{st2[0]}|{st1[1]}{let[1]}{st2[1]}|{st1[2]}{let[2]}{st2[2]}|{st1[3]}{let[3]}{st2[3]}|{st1[4]}{let[4]}{st2[4]}| \n ___ ___ ___ ___ ___ \n')
        print('')
        print('Oh you MUST have cheated!')
        break

    # Compare the guess to the target word and print the number of matching letters

    for i in range(len(guess)):
      for j in range(len(target_word)):
        if guess[i] == target_word[j] and guess[i] == target_word[i]:
          let[i] = guess[i]
        if guess[i] == target_word[j] and guess[i] != target_word[i]:
          let[i] = guess[i]
          st1[i] = '*'
          st2[i] = '*'


    # Increment the number of failed attempts
    num_failures += 1

    # Check if the user has reached the limit of 6 failed attempts
    if num_failures == 5:
        print(f'You have reached the limit of {num_failures} failed attempts')
        print(f'The word was: {target_word}')
        print('You get nothing')
        print('Good day')
        print('I said good day!')
        break