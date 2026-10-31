import random

def roll_die():
    return random.randint(1, 6)

turn_number = 1
temp_score = 0
p1_totalscore = 0
p2_totalscore = 0
user_choice = ""

###############################################

def run_round():
    global turn_number
    global temp_score
    global p1_totalscore
    global p2_totalscore
    global user_choice
    valid_move = False
    
    if user_choice != "roll":
        print("Turn " + str(turn_number))
        print("Your current score is: " + str(p1_totalscore))
    print("This round you have: " + str(temp_score))
    
    while valid_move == False:
        user_choice = input("Would you like to roll or bank? ")
        
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
                user_choice = ""
            if die > 1:
                print("You rolled a " + str(die) + ".")
                temp_score = temp_score + die
            print(" ")

        if user_choice == "bank":
            valid_move = True
            p1_totalscore = p1_totalscore + temp_score
            temp_score = 0
            turn_number = turn_number + 1


while p1_totalscore < 100 and p2_totalscore < 100:
    run_round()

print(" ")
print("-----------------------")
print(" ")
print("You won the game after " + str(turn_number) + " turns!")