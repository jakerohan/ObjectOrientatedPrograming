word_list = ['']
word = ''
guesses = ['a', 'e', 'i', 'o', 'u']
underscores = ''

with open('second attempt/pokemon.txt', 'r') as file:           #working directory is one folder up, not sure why
        pokemon = file.read()
        word_list = pokemon.strip().split(', ')                 #removes spaces and commas from text file

def choose_word():
    import random
    global word
    
    rand_number = random.randint(0, len(word_list)-1)           #generates random number in the range of the length of the string
    word = word_list[rand_number]

def display_word():
    global guesses
    global underscores
    underscores = ''

    #   print(word)
    for letter in word:
        if letter.lower() in guesses:                           # trying to make the game non-reliant on upper or lower case
            underscores += letter                               # checks guesses list, if a letter in guesses is in the word, then the letter is displayed
        else:                                                   
            underscores += '_'                                  #if not in guesses, print '_'
    print(underscores)

def play_game():
    choose_word()
    display_word()

    global guesses
    turns_count = 0

    while underscores != word:
        guess = input('please guess a letter: ')
        print('')
        
        if guess.lower() in word or guess.upper() in word:      # trying to make the game non-reliant on upper or lower case
            print('good guess')
        else:
            print('bad luck, try again')
            
        turns_count += 1

        guesses.append(guess)
        display_word()
        print('')
        

    print('it took you ', turns_count, ' to guess')


play_game()
