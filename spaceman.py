import random 

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') 
    #word = random.choice() 
    secret_word = random.choice(words_list)
    return secret_word

#checks if all the letters of the secret word have been guessed 
def is_word_guessed(secret_word, letters_guessed):
    correctlyGuessed = ' '

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True 


#used to get string correctlyGuessed correct letters guessed, underscores for not yet guessed 
def get_guessed_word(secret_word, letters_guessed):
    correctlyGuessed = ' '

    for letter in secret_word:
        if letter in letters_guessed:
            correctlyGuessed += letter
        else: correctlyGuessed += "_"
    return correctlyGuessed

#stretch, letter already entered, do not deduct life. 
#def check(secret_word, guess):
    #for letter in secret_word:
        #if letter == guess:
            #print(f'ALERT: {guess} has already been attempted. ')
            #print('A life has not been removed. Please proceed cautiously ')
            #return True
    #return False 

#check if the guessed letter is in the secret word 
def is_guess_in_word(guess, secret_word):
    #return guess in secret_word
    if guess in secret_word: 
        #print(f'Correct!')
        return True
    else: 
        #print(f'{guess} is incorrect. ')
        return False 

#main block of code that processes game (huge while loop with if)
def spaceman(secret_word):
    letters_guessed = []
    lives = 7
    print("Welcome, Fellow Earthling! Let's Play Spaceman! ")
    print("\n")
    print("You will start with 7 lives. Keep them by guessing the letters in the secret word correctly. Lose one life for each letter guessed incorrectly. ")
    print("\n")
    running = True
    while running: 
        guess = input('Enter a letter > ')
        if is_guess_in_word(guess, secret_word):
            print(f'Correct! You have {lives} lives left!')
            letters_guessed.append(guess)
            #print(letters_guessed)
        else: 
            lives -= 1
            print(f'{guess} is incorrect. You have {lives} remaining ')
            
        print(get_guessed_word(secret_word, letters_guessed))
        print(f'List of attempted letters: {letters_guessed} ')

        if check(letters_guessed, guess):
            #lives != 1
            #print(f'ALERT: {guess} has already been attempted. Please proceed cautiously ')
        #else: 


        if is_word_guessed(secret_word, letters_guessed):
            print('WINNER, WINNER, CHICKEN DINNER!!!')
            running = False 

        if lives == 0:
            print(f'So close, but so far... GAME OVER! The correct word was {secret_word.upper()}')
            #read secret word as UPPER for easier reading
            running = False
            break
        #letters_guessed.append(guess)
        #print()

#Start game 
secret_word = load_word()
spaceman(secret_word)

"""
CHECK LIST:
✓prog accept USER INPUT for letter guesses
✓provide accurate/update feedback per round: right, display word progress
                                            ✓wrong, lives remaining
✓7 lives total
✓Read duplicate letters in one pass (all 'l', 'e' in challenge)- IS WORD GUESSED 
✓WINNER NOTIFICATION 
✓LOSER  NOTIFICATION IS ALL LIVES DEPLETED
    STRETCH: 
    Play again? yes/no. loop- continue/break?
    ✓Alert user is they have already attempted a letter, without deducting life. 
"""

'''
greeting needs to be outside of while loop, so it doesn't get repeated!!!
"Welcome, space explorer! Let's play Spaceman"
"You will start with 7 lives. Keep them by guessing the letters in the secret word correctly. Guess them wrong, and lose a life each time. "
"Enter a letter > "

user_guess= a
 IF TRUE 
 correct!
display word progress: a _ _ _ _

ELSE FALSE
incorrect ):
SUBTRACT 1 life, display lives remaining.

LOOP until 7 lives depleted or word guessed 
'''