import random, sys, logging

fruitNames = ['mangosteen', 'cranberry', 'grape', 'asparagus', 'rockmelon']

animalWater = ['barnacle', 'barracuda','cuttlefish', 'dolphin', 'dugong',
               'emperor shrimp', 'grouper', 'herring', 'humpback whale', 'mackerel',
               'manta ray', 'narwhal', 'oyster', 'plankton', 'porpoise',
               'pufferfish', 'quillfish', 'sea cucumber', 'seahorse', 'walrus']

animalLand = ['pelican', 'badger', 'camel', 'rhinocerous', 'macaw',
              'black widow', 'tarantula', 'gerbil', 'monkey', 'chincilla',
              'chipmunk', 'penguin', 'chimpanzee', 'kingfisher', 'hippopotamus',
              'platypus', 'emu', 'gecko', 'hawk', 'iguana',
              'gemsbok', 'anteater', 'eagle', 'impala', 'jackal',
              'hyena', 'lemur',' lynx', 'parrot']
# hangmanWord = random.choice(wordChoices)


print('Welcome. Let\'s play hangman! Are you ready?')
Yes = True
while Yes:
    answer = input()
    if answer.lower() in ['no', 'n']:
        print('Thank you and have a nice day!')
        sys.exit()
    elif answer.lower() in ['yes', 'y']:
        Yes = False
    else:
        print('Invalid answer. Are you ready to play?')
        Yes = True

hangmanWord = random.choice(animalLand)
displayList = []
for _ in range(len(hangmanWord)):
    displayList.append("_")


#print('The word is a fruit.\nYou have 10 chances! Please choose your first letter.')
print('The word is an animal on land.\nYou have 10 chances! Please choose your first letter.')
#print('The word is an animal in water.\nYou have 10 chances! Please choose your first letter.')
print(''.join(displayList))


lettersUsed = []
wrongGuesses = 0
guesses = 10
while (guesses != wrongGuesses):
    userChoice = input()
    #for i in range(len(hangmanWord)):
    if userChoice in hangmanWord:
        print(userChoice, 'is in the word!')
        for i in range(len(hangmanWord)):
            if userChoice == hangmanWord[i]:
                displayList[i] = userChoice
                wrongGuesses += 0
                
                if ''.join(displayList) == hangmanWord:
                    print(''.join(displayList))
                    print('Good job! You\'ve guessed the correct word!')
                    sys.exit()
    else:
        print('There is no letter ', userChoice, ' in the word :(')
        print('You have ', str(guesses - wrongGuesses), ' left.')
        # print('You have chosen ', lettersUsed, ' so far.')
        # lettersUsed.append(userChoice)
        wrongGuesses+=1
        if userChoice in lettersUsed:
            print('You have already chosen the letter.')
        else:
            lettersUsed.append(userChoice)
        print('You have chosen ', lettersUsed, ' so far.')


    print(''.join(displayList))

#if guesses == wrongGuesses:
print('You have reached the maximum tries. The word is ' + hangmanWord + '.')
sys.exit()


    









    



