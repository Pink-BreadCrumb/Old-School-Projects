import random
import time

def roll_die():
    return random.randint(1, 6)

def cpu_turn():
    return random.randint(1, 2)

turn_number = 1
temp_score = 0
p1_totalscore = 0
p2_totalscore = 0
user_choice = ""
player_turn = 1

###############################################

def run_round():
    global turn_number
    global temp_score
    global p1_totalscore
    global p2_totalscore
    global user_choice
    global player_turn
    global turn_over
    valid_move = False
    turn_over = False
    
    if user_choice != "roll":
        print("Turn " + str(turn_number))
        if player_turn == 1:
            print("Your current score is: " + str(p1_totalscore))
        if player_turn == 2:
            print("Your current score is: " + str(p2_totalscore))
    print("This round you have: " + str(temp_score))
    
    while valid_move == False:
        if player_turn == 1:
            user_choice = input("Would you like to roll or bank? ")
        if player_turn == 2:
            if cpu_turn() == 1:
                user_choice = "roll"
            if cpu_turn() == 2:
                user_choice = "bank"

            print("Would you like to roll or bank? " + user_choice)
            time.sleep(1.5)
        
        if user_choice != "roll" and user_choice != "bank":
            print("Invalid choice entered, please try again.")
            print(" ")
        
        if user_choice == "roll":
            valid_move = True
            die = roll_die()
            if die == 1:
                print("You rolled a 1! Points are reset!")
                temp_score = 0
                turn_number = turn_number + 1
                turn_over = True
                user_choice = ""
            if die > 1:
                print("You rolled a " + str(die) + ".")
                temp_score = temp_score + die
            print(" ")

        if user_choice == "bank":
            valid_move = True
            if player_turn == 1:
                p1_totalscore = p1_totalscore + temp_score
            if player_turn == 2:
                p2_totalscore = p2_totalscore + temp_score
            temp_score = 0
            turn_number = turn_number + 1
            turn_over = True
            print(" ")


while p1_totalscore < 100 and p2_totalscore < 100:
    run_round()
    if turn_over == True:
        if player_turn == 1:
            player_turn = 2
        elif player_turn == 2:
            player_turn = 1

print(" ")
print("-----------------------")
print(" ")
if p2_totalscore >= 100:
    print("Player 2 won the game after " + str(turn_number) + " turns!")
if p1_totalscore >= 100:
    print("Player 1 won the game after " + str(turn_number) + " turns!")