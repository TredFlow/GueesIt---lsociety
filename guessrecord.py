import os
from art import tprint
def record_check():
    file_name = 'record.txt'
    if  not os.path.exists(file_name ):
        with open ('record.txt', 'w') as f:
          f.write(str(100))
        return(100)
    with open(file_name, 'r') as f:
        content = f.read().strip()
        return int(content) if content else 100
    
def record_mod(new_record):
    with open ('record.txt', 'w') as f:
       f.write(str(new_record))

def record_guess(attempts, current_record):
    attempts = int(attempts)
    current_record = int(current_record)
    if attempts == current_record:
        print('You can always be thinner. Look Better. - P.Bateman')
        tprint('LOOK BETTER')
    elif attempts < current_record:
        print(f'Cool, Your new record is {current_record - attempts} attempts better. ')
        record_mod(attempts)
    elif attempts > current_record:
        print(f'Bro, you were better last time. Your best was {current_record}.')
        
