#Hangman project to do 1: Choose a random from the word list and assighn it to the variable called choosen_world.Then print it
import random
from Hangman_words import word
from hangman_art import stages
word_list=["aardwark","baboon","canel"]
#Create a variable called"lives" to keep track of the how many lives user left 
#set lives equal to 6
lives=6
choosen_word=random.choice(word)
# print(choosen_word)
word_lenghth=len(choosen_word)
placeholder=""
for letter in choosen_word:
    placeholder+="_"
print(placeholder)
#Ask a user to guess a letter and assighn their answer variable called guess.make guess lowercase.
#Use a while loop to ask a user to guess again
game_over=False
corrected_letters=[]
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT***********************************")
    guess=input("letter to guess: ").lower()
    print(guess)
#If user has entered a letter that they have already guessed, print the letter is already guessed
#Use a while loop to ask a user to guesagain 
#Create a display that puts the guess letter in the right position and _ in remaining position
    display=""
#modify for loop so you need to keep prrvious coorect letters 
    for letter in choosen_word:
        if letter==guess:
            display+=letter
            corrected_letters.append(guess)
        elif letter in corrected_letters:
            display+=letter
        else:
            display+="_"
    print(display)
#If guess is not a letter in choosen_word,then reduce lives by 1.
    if guess in corrected_letters:
        print(f"You have guessed a letter {guess}")
    if guess not in choosen_word:
        lives-=1
        print(f"You guessed {guess},thats not in word. You lose a life")
        if lives==0:
            game_over=True
            print(f"************************* IT WAS {choosen_word}.YOU LOSE******************************")
#If lives go down to 0 then the game should stop and it should print "You lose"
    if "_" not in display:
        game_over=True
        print("******************************YOU WIN********************************************************")
#Print the ASCII art from stages
#that corresponds to the current number of lives the user has remainmg
    print(stages[lives])