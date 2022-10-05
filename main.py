from words import words
import random

tries = 5

while tries != 0:
  def generateRandomWord():
    return random.choice(words)

  def generateRandomNum(a, b):
    return random.randint(a, b)

  word = generateRandomWord()
  original = word
  l = len(word)
  for i in range(1):
    try:
      global letter
      index = generateRandomNum(0, l)
      letter = word[index]
      word = word.replace(word[index], '_')
    except Exception as error:
      pass   

  print(word)
  guess = input("Enter the letter with the _ :-")
  if guess == letter:
    print(f"You won! You got it in {tries} tries!")
  else:
    tries -= 1
    print(f"{tries} tries left...Try again.")

print(f'You lost as the hangman was hanged! The word was {word}')