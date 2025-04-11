


def choose_word():
    with open("pokemon.txt", "r") as file:
        lineVar = file.readline().strip()
        PokemonList = lineVar.split(",")

    print('there are', len(PokemonList), 'words in the list')
    print("the words to choose from are:")
    print(PokemonList)

    import random
    RandNum = random.randint(0, len(PokemonList) - 1)
    print('number chosen: ', RandNum)

    word = PokemonList[RandNum].strip()
    print('word: ', word)
    print('')
    print('')
    return word


def display_word():
    word = choose_word()
    print(word)
    count = 0

    UnderscoreString = ""
    for i in range(len(word)):
        UnderscoreString += "_"
    print(UnderscoreString)

    GuessedLetters = []
    while UnderscoreString.lower() != word.lower():
        letter = input("Enter a letter: ")
        if len(letter) != 1:
            print("Please enter a single letter")
            continue
        if letter in GuessedLetters or letter.swapcase() in GuessedLetters:
            print("You have already guessed that letter")
            continue
        if letter not in word or letter.swapcase() not in word:
            print("That letter is not in the word")
            GuessedLetters.append(letter)
            count =+ 1
            continue
        if letter in word or letter.swapcase() in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == letter:
                    UnderscoreString = UnderscoreString[:i] + letter + UnderscoreString[i + 1:]
            count =+ 1
            print(UnderscoreString)
            continue
        if UnderscoreString.lower() == word.lower():
            print("You win!")
            print(' it took you ', count, ' guesses')
            break




# choose_word()
display_word()
# playgame()

