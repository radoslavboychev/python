import random

#Game of hangman 1.0
#Author - rboychev

name = input("Enter your name: ")
print("Good luck", name)

# these are the words that will be included in the game
wordBank = ["welcome", "hangman", "game", "player", "python"]

word = random.choice(wordBank)

print("\Let's begin. Guess the letters!")

guesses = ""

turns = 10

while turns > 0:
    failed = 0  # count when the player fails
    for char in word:
        if char in guesses:
            print(chr, end="")
        else:
            print("_", end="")
            # for every  failure increment ++
            failed += 1
    if failed == 0:
        print("\n \r You Win!")
        print("\n Your word is: ",word)
        break
    
    guess = input("\n \n Guess the character: ")
    guesses += guess;
    if guess not in word:
        turns -= 1
        #if the character isn't in the word, output "wrong"
        print("Wrong")
        print("\nYou have", + turns," more attempts")
        if turns == 0:
            print("\n\nYou lose, the word was:",word )
