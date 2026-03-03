import sys
import time
from art import tprint

def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    print()
def messages(attempts):
    if attempts == 1:
            slow_print(f'WTF! Are you Einstein? Even I can`t guess in {attempts} attempts.')
    elif attempts <= 7:
            slow_print(f'Bravo boss! {attempts} attempts, a worthy result.')
    elif attempts <= 10:
            slow_print(f'More or less, {attempts} attempts, but still congratulations!')
    elif attempts >= 11:
            slow_print('Hey, dude! When did you get your IQ tested?') 
            time.sleep(1)
            slow_print('This is a cool neighborhood, get lost!') 
            time.sleep(1)
            slow_print(f'{attempts} attempts, shame!')
            time.sleep(1)
            slow_print("We're calling your mom!")
            time.sleep(1)
            tprint('BEEP')
            time.sleep(1)
            slow_print("Your mom: Are you serious? I'll give him up right now.")
            time.sleep(1)
            tprint('HAHAHAHA')
            time.sleep(1)
            tprint('DONT CRY')
