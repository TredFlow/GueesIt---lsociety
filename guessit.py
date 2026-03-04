import random
import time
from modguess import slow_print, messages, tprint
from guessrecord import record_check, record_guess
best_score = record_check()
num = random.randint(1, 100)
attempts = 0
slow_print('Welcome to the game!')
time.sleep(1)
tprint('GUESS IT')
time.sleep(2)
slow_print(f"Current record to beat: {best_score} attempts")
time.sleep(1)
while True:
    guess = input('Enter a number between 1 and 100:')
    attempts += 1
    if not guess.isdigit(): 
        print("Enter the NUMBERS, bro")
        continue
    i = int(guess)
    if i < 1 or i > 100: 
        slow_print('The number must be between 1 and 100!')
        continue
    if i == num:
        messages(attempts)
        break
    elif i < num:
        slow_print('The number is higher!')
    elif i > num:
        slow_print('The number is less!')

record_guess(attempts, best_score)
Exit = input('Press Enter to exit...')








