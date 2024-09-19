import random
#print a welcome message for our player
print("******Welcome to my word guess game*****\nHint: African country names.\n")
print()
#the user is asked to enter the name first
name = input("What is your name? ")
print(f"Good Luck! {name.upper()}")
# lets store the variable words in a list called words
words = ['kenya', 'nigeria','southafrica', 'egypt', 'ghana', 'uganda','morocco', 'rwanda',]
# function will choose one random word from this list of words
while True:
  word = random.choice(words)
  print("Guess the character ")
  print("\n")
  guesses = ""
  # any number of turns can be used here
  turns = 12
  # use loop to determine number of guesses
  while turns > 0:
    failed = 0
    #all the character from the input word taking one at a time
    for character in word:
      # comparing that character with character in guesses
      if character in guesses:
        print(character.upper(), end=" ")
      else:
        print("_", end=" ")
        # for every fail 1 will be added in failure
        failed += 1
    if failed == 0:
      # this print the correct word
      print(f"\nThe word is: {word.upper()}\nYou win")
      
      # user will win the game if failure is 0 and 'you win'
      print()
      break
    print()
    guess = input("Guess a character: ").lower()
    print("\n")
    if guess in guesses:
      print("You have already guessed that character.")
    if len(guess) !=1:
      print("Please enter a single character.")
      continue
    guesses += guess
      # check input with the character will be stored in guesses
      # check input with the character in word
    if guess.lower() not in word.lower():
      turns -=1
        # if character does not match the word then 'wrong' will be given as output
      print("Wrong")
        # this will print the number of turns left for the user
      print(f"You have, {turns},more guesses")
  
      if turns == 0:
        print("You loose")
  again = input("Play again? Y/N: ").upper()
  if again == "Y":
    continue
  else:
    print("Thank you for playing our game. Bye!")
    break