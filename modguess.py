import sys
import time
from art import tprint
from languess import Translations
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    print()
def messages(attempts, lang):
    if attempts == 1:
            slow_print(Translations [lang]['attempts_1'].format(attempts))
    elif attempts <= 7:
        slow_print(Translations [lang]['attempts_7'].format(attempts))
    elif attempts <= 10:
            slow_print(Translations [lang]['attempts_10'].format(attempts))
    elif attempts >= 11:
            slow_print(Translations [lang]['troll_start']) 
            time.sleep(1)
            slow_print(Translations [lang]['hood_troll']) 
            time.sleep(1)
            slow_print(Translations [lang]['shame'].format(attempts))
            time.sleep(1)
            slow_print(Translations [lang]['calling'])
            time.sleep(1)
            tprint('BEEP')
            time.sleep(1)
            slow_print(Translations [lang]['mom_answer'])
            time.sleep(1)
            tprint('HAHAHAHA')
            time.sleep(1)
            tprint('DONT CRY')

