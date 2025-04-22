import random 
wordList = ["About",	'Alert',	'Argue',	'Beach',
'Above', 'Alike',	'Arise',	'Began',
'Abuse',	'Alive',	'Array',	'Begin']

selectedWord = ''
correctLetters = 0
tries = 0

# Selects random word from the wordList.
def selectWord():
  randomNum = random.randint(0, len(wordList) - 1)
  selectedWord = wordList[randomNum]
  selectedWord = selectedWord.lower()
  return selectedWord

# This function takes in what was guessed and for each letter checks it against each letter of the actual word.
def guessCheck(guessedWord) -> list:
  wordResultList = []
  lettersChecked = 0
  while lettersChecked != 5: 
    if guessedWord[lettersChecked] in selectedWord and guessedWord[lettersChecked] == selectedWord[lettersChecked]:
      wordResultList.append('✔')
    elif guessedWord[lettersChecked] in selectedWord:
      wordResultList.append('-')
    else:
      wordResultList.append('X')
    lettersChecked += 1
  wordResult = wordResultList[0:5]
  return wordResult


print('Welcome to bootWord, your favorite Wordle knockoff. \nOur pool of words is ' + str(len(wordList)) + ' words long. \nYou will have five tries to guess the word.\nPress ENTER to continue.')
input()
selectedWord = selectWord()

#This loop is the main game loop. It will run until the game ends.
while correctLetters != 5 and tries != 5:
  guess = ''
  print('Guess a five letter word.')
  guess = input()
  guess = str(guess)
  guess = guess.lower()
  if len(guess) != 5:
    print('Please type a five letter word.')
    continue
  else:
    print(guessCheck(guess))
    correctLetters = guessCheck(guess).count('✔')
    tries += 1

if correctLetters == 5:
  print('Congrats! You won bootWord!')
elif tries == 5 and correctLetters != 5:
  print('Out of guesses. Maybe next time.')
    
