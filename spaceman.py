import random 

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split('') 
    #word = random.choice() 
    secret_word = random.choice(words_list)
    return secret_word

def get_guessed_word(secret_word, letters_guessed):

def is_guess_in_word(user_guess, secret_word):

def spaceman(secret_word):
    letters_guessed = []
    lives = 7

#Start game 
secret_word = load_word()
spaceman(secret_word)

"""
CHECK LIST:
prog accept USER INPUT for letter guesses
provide accurate/update feedback per round: right, display word progress
                                            wrong, lives remaining
✓7 lives total
Read duplicate letters in one pass (all 'l', 'e' in challenge)
WINNER NOTIFICATION 
LOSER  NOTIFICATION IS ALL LIVES DEPLETED
    STRETCH: 
    Play again? yes/no. loop- continue/break?
    Alert user is they have already attempted a letter, without deducting life. 
"""

'''
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