def determine_winner():
    global player1_score
    global player2_score
    global round_num
    global p1_wl
    global p2_wl
    global c_rock
    global c_scissors
    global c_paper
    global score_2
    global p1_
    global p2_
    global round_num
    global keep_going
    global ending
    
    if p1_wl == 3 or p2_wl == 3:
        keep_going = 0
    
    if keep_going == 0 and ending == 0:
        if p1_wl > p2_wl:
            print(p1 + " wins the tournament " + str(p1_wl) + "-" + str(p2_wl) + "!")
            print("Thanks for playing!")
        elif p2_wl > p1_wl:
            print(p2 + " wins the tournament " + str(p2_wl) + "-" + str(p1_wl) + "!")
            print("Thanks for playing!")
        else:
            print("It's a tie. The score was " + str(p1_wl) + "-" + str(p2_wl))
            print("Thanks for playing!")
        ending = 1
    
    if keep_going == 1:
        # Score decider for "rock"
        if p1_ == "rock" or p2_ == "rock":
            if p1_ == "paper" or p2_ == "paper":
                c_rock = 0
            if p1_ == "scissors" or p2_ == "scissors":
                c_rock = 1
        
        # Score decider for "paper"
        if p1_ == "paper" or p2_ == "paper":
            if p1_ == "scissors" or p2_ == "scissors":
                c_paper = 0
            if p1_ == "rock" or p2_ == "rock":
                c_paper = 1
        
        # Score decider for "sicssors"
        if p1_ == "scissors" or p2_ == "scissors":
            if p1_ == "rock" or p2_ == "rock":
                c_scissors = 0
            if p1_ == "paper" or p2_ == "paper":
                c_scissors = 1
        
        if p1_ == p2_:
            print("It's a tie!")
        
        ################################################
        decided = 0
        win1_temp = 0
        win2_temp = 0
        
        if p1_ == "rock" and c_rock == 1:
            p1_wl = p1_wl + 1
            win1_temp = 1
        elif p1_ == "scissors" and c_scissors == 1:
            p1_wl = p1_wl + 1
            win1_temp = 1
        elif p1_ == "paper" and c_paper == 1:
            p1_wl = p1_wl + 1
            win1_temp = 1
        elif p2_ == "rock" and c_rock == 1:
            p2_wl = p2_wl + 1
            win2_temp = 1
        elif p2_ == "scissors" and c_scissors == 1:
            p2_wl = p2_wl + 1
            win2_temp = 1
        elif p2_ == "paper" and c_paper == 1:
            p2_wl = p2_wl + 1
            win2_temp = 1
        elif p1_ == p2_:
            m = 0
        else:
            print("[ERROR DETERMINING SCORE]")
        
        ################################################
        
        if keep_going == 1 and p1_ != p2_:
            if win1_temp > win2_temp:
                print(p1_ + " beats " + p2_ + "! " + p1 + " wins this round.")
                print(str(p1_wl) + "-" + str(p2_wl))
                print(" ")
            if win2_temp > win1_temp:
                print(p2_ + " beats " + p1_ + "! " + p2 + " wins this round.")
                print(str(p1_wl) + "-" + str(p2_wl))
                print(" ")
            c_rock = 0
            c_scissors = 0
            c_paper = 0
            round_num = round_num + 1
    
    
        


def play_round():
    global p1
    global p2
    global p1_
    global p2_
    global p1_wl
    global p2_wl
    global keep_going
    
    if p1_wl == 3 or p2_wl == 3:
        keep_going = 0
    
    if keep_going == 1:
        print("— Round " + str(round_num) + " —")
        p1_ = input(p1 + ", enter your choice (rock/paper/scissors): ")
        p2_ = input(p2 + ", enter your choice (rock/paper/scissors): ")
        print(" ")
    if keep_going == 0:
        ham = 11875


player1_score = 0
player2_score = 0
round_num = 1
p1_wl = 0
p2_wl = 0
c_rock = 0
c_scissors = 0
c_paper = 0
score_2 = 0
p1_ = ""
p2_ = ""
keep_going = 1
ending = 0



def clear():
    c_rock = 0
    c_scissors = 0
    c_paper = 0


print("Welcome to Rock-Paper-Scissors Tournament!")
print(" ")
p1 = input("Player 1, enter your name: ")
p2 = input("Player 2, enter your name: ")
print(" ")
print("Best of 5 rounds. First to 3 wins!")
print(" ")
while ending != 1:
    play_round()
    determine_winner()