import random 

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') 
    #word = random.choice() 
    secret_word = random.choice(words_list)
    return secret_word

#checks if all the letters of the secret word have been guessed, multiples
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True 

#get string correctlyGuessed letters, underscores for not yet guessed 
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
            #return True
    #return False 

#check if the guessed letter is in the secret word, print correpsonding statement, correct/incorrect
def is_guess_in_word(guess, secret_word):
    #return guess in secret_word
    if guess in secret_word: 
        #print(f'Correct!')
        return True
    else: 
        #print(f'{guess} is incorrect. ')
        return False 

#main, processes game (huge while loop with if)
#specify lives and load empty string
def spaceman(secret_word):
    letters_guessed = []
    lives = 7
    print("Welcome, Fellow Earthling! Let's Play Spaceman! ")
    print("\n")
    print("You will start with 7 lives. Keep them by guessing the letters in the secret word correctly. Lose one life for each letter guessed incorrectly. ")
    print("\n")
    running = True
    while running: 
        print(secret_word)
        guess = input('Enter a letter > ')
        if is_guess_in_word(guess, secret_word):
            print(f'Correct! ')
            letters_guessed.append(guess)
            print(f'List of attempted letters: {letters_guessed} ')
        else: 
            lives -= 1
            print(f'{guess} is incorrect. You have {lives} remaining ')
            letters_guessed.append(guess)
            print(f'List of attempted letters: {letters_guessed} ')
        print(get_guessed_word(secret_word, letters_guessed))
        #print(f'List of attempted letters: {letters_guessed} ')
        if is_word_guessed(secret_word, letters_guessed):
            print('WINNER, WINNER, CHICKEN DINNER!!!')
        if lives == 0:
            print(f'So close, but so far... GAME OVER! The correct word was {secret_word.upper()}')
            #read secret word as UPPER for easier reading
            running = False
            break
#Start game 
secret_word = load_word()
spaceman(secret_word)


#if check(letters_guessed, guess):
                #print(f'ALERT: {guess} has already been attempted. ')
                #lives += 1 

                #letters_guessed.append(guess)
        #play again loop
        #play_again = print("Would you like to play again? (yes/no) > ")
        #if play_again == 'yes':
            #print("Let's play again!")
        #else: 
            #print('Thanks for playing!')