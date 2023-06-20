import random
import time
import tkinter as tk

def LVL_1():
    
    score_LVL_1 = 0 # Displayed at the bottom right hand corner of the screen
    attempts_LVL_1 = 0 # Displayed at the bottom right hand corner just below the score
    level = 1
    
    while True: 
        
        
   
        random_num = random.choice(range(1, 10))

        if random_num < 5:
            print("Less-Then") # Displayed above the input box 
        if random_num > 5:
            print("Greater-Then")
        if random_num == 5:
            print("Equal-To")

        diff = (int(random_num) +- 5)

        print("Difference is " , int(diff)) # displayed above the "less-than" "greater-than" "equal-to"

        guess = input("You: ") 
        attempts_LVL_1 + 1

        diff_guess = (int(random_num) - int(guess))

        if int(guess) == random_num:
            print("Correct") # Displayed if the users guess is correct and should be displayed above the text box 
            score_LVL_1 += 1
            play_again = input("Play Again? yes/no | You:    ") # Should be displayed as a checkable box next to the input line after the user makes a correct guess
        if play_again.lower() == "no":
            print("All Good, Cheers!")
            print("Score: ", score_LVL_1)
            break
        
        if score_LVL_1 == 5:
            level_up = input("Level 2? yes/no")
            if level_up == "yes":
                print()
                print("Level 2 | Guess a Number Between 1 and 20") # should replace the " 1 and 10" range display from level one
                print()
                LVL_2()
                break
            else:
                continue
                
        
        if int(guess) > random_num:
            print("Too high")
            print(int(diff_guess))
        if int(guess) < random_num:
            print("Too Low")
            print(int(diff_guess))
        
    
    
        else:
            if play_again.lower() == "yes":
                print("Sweet!")
                print()
            else:
                print("answer yes/no ") 
                play_again()

    
def LVL_2():
    
    score_LVL_2 = 0
    attempts_LVL_2 = 0
    level = 2
    
    while True:
        random_num2 = random.choice(range(1, 20))
        
        if random_num2 < 10:
            print("Less-Then") # same display possitioning as level one. If you are unsure as to the possitioning and timing for the GUI please ask. 
        if random_num2 >  10:
            print("greater-Then")
        if random_num2 == 10:
            print("Equal-To")
            
        diff = (int(random_num2) +- 10)
        print("Difference is ", diff)
        
        guess = input("You: ")
        
        diff_guess = (int(random_num2) - int(guess))
        
        if int(guess) == random_num2:
            print("Correct! ")
            score_LVL_2 += 1
            play_again = input("Would you like to play again? yes/no | You:  ")
        if play_again.lower() == "no":
            print("All good, Cheers! ")
            print("Score: ",score_LVL_2)
            break
        if int(guess) > random_num2:
            print("Too High ")
            print(diff_guess)
        if int(guess) < random_num2:
            print("Too Low ")
            print(diff_guess)
            
        else:
            if play_again.lower() == "yes":
                print("Sweet")
                print()
            else:
                print("answer yes/no ")
                play_again()


        
        

        
    




   
    
