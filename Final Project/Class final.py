# --- API Imports ---
import shutil
import time



global questions
questions = []

global answers
answers = []

global check
check = []

global score
score = []



def clear():
    print("\n" * 100)

def print_(text):
    terminal_width = shutil.get_terminal_size().columns
    print(text.center(terminal_width))

def main_menu():
    clear()
    print_("Quiz Maker!")
    print("")
    print_("- - 1||Start your Quiz  --  --  --  Create a Quiz||2 - -")
    print_("--- 3||Run Demo Quiz||3 ---")
    print("")
    print("---------------")
    
    user_input = "BLANK"
    while user_input == "BLANK":
        try:
            user_input = int(input("Choose an option based on the numbers above: "))
        except ValueError:
            user_input = "BLANK"
            print("An invalid option has been entered. Please try again.")
        if type(user_input) == "<class 'int'>":
            if user_input > 3 and user_input < 1:
                user_input = "BLANK"
            
    if user_input == 1:
        if not questions:
            print("Your quiz has no values. Please enter the quiz maker before choosing this option.")
            time.sleep(2)
            main_menu()
        else:
            run_quiz()
    if user_input == 2:
        quiz_maker()
    if user_input == 3:
        demo()

def quiz_maker():
    print("Starting the quiz maker will clear your current quiz.")
    print("Are you sure you want to proceed?")
    if input("Y/N: ") == "Y":
        global questions
        global answers
        global check
        global score
        global exit_choice
        exit_choice = ""
        questions = []
        answers = []
        check = []
        score = []
        global quiz_name
        quiz_name = input("Please enter your quiz name:")
        
        while exit_choice != "Y":
            clear()
            print("Please select an option below --")
            print(quiz_name)
            print("")
            print("1) Add a question/answer")
            print("2) Remove a question/answer")
            print("3) Finish editing")
            print("--------------------------------")
            quiz_maker2(input("Selection: "))
        main_menu()

def quiz_maker2(temp_choice):
    global exit_choice
    
    if temp_choice == "1":
        clear()
        for i in range(9999):
            try:
                if questions[i] == "(Placeholder for 'no value')":
                    pass
                else:
                    continue
            except IndexError:
                pass
            
            current_edit = i+1
            questions.append(input("Enter the name for question " + str(current_edit) + ": "))
            clear()
            print("Question " + str(current_edit) + ": " + questions[i])
            print("")
            for k in range(4):
                answers.append(input("Enter the answer option: "))
            print("-----------------------------")
            for j in range(4):
                temp = input("Is answer " + str(j+1) + " correct? Y/N: ")
                if temp == "Y":
                    temp = True
                else:
                    temp = False
                check.append(temp)

            clear()
            print("Would you like to continue adding questions?")
            ending_choice = input("Y/N: ")
            if ending_choice == "Y":
                pass
            else:
                print("Now exiting...")
                time.sleep(2)
                clear()
                break
            
    if temp_choice == "2":
        clear()
        if len(questions) == 0:
            print("You have no questions or answers to remove. Please select to add them before entering this menu.")
            time.sleep(2)
        else:
            for i in range(len(questions)):
                print(str(i+1) + ") " + questions[i])
                something = len(questions) + 1
                print(str(something) + ") Cancel removal")
                
            while True:
                try:
                    alter_input = int(input("Please select the question that you wish to remove: "))
                    clear()
                    if alter_input > 0 and alter_input < len(questions) or alter_input == something:
                        temp_check = 1
                    if alter_input != something:
                        print('You have selected the question "' + questions[alter_input-1])
                        temp_check = 1
                    else:
                        print("Now exiting...")
                        time.sleep(2)
                        clear()
                        temp_check = 2
                        break
                except IndexError:
                    print("You have entered an invalid option. Please try again.")
                if temp_check == 1:
                    break
            if temp_check != 2:
                clear()
                if input("You wish to remove question " + questions[alter_input-1] + "?" + "\n" +  "(Y/N): ") == "Y":
                    clear()
                    print("Removing question...")
                    time.sleep(2)
                    questions.pop(alter_input-1)
                    for j in range(4):
                        answers.pop(0 + (4*(alter_input-1)))
                    for k in range(4):
                        check.pop(0 + (4*(alter_input-1)))

    if temp_choice == "3":
            print("You wish to exit the quiz maker?" + "\n" + "You will not be able to return.")
            exit_choice = input("Y/N: ")
            if exit_choice == "Y":
                print("Now exiting...")
                time.sleep(2)
                clear()
            else:
                exit_choice = ""


def question_load(questions, answers, imported):
    global current
    for i in range(len(questions)):
        clear()
        current = imported
        round_number = imported+1
        print_("- - - - || Question - " + str(round_number) + " || - - - -")
        print_(questions[current])
        print("")
        print_("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        for z in range(4):
            print_(str(z+1) + ") " + answers[0+z+(4*current)])
            print_("- - - - -")
        print("")
        print("")

        

def take_answer():
    global user_answer
    while True:
        user_answer = int(input("Enter your answer based off the numbers next to them: "))
        if user_answer > 4 or user_answer < 0:
            print("An invalid option has been entered. Please try again.")
        else:
            break
    
    return user_answer
    

def demo():
    global questions
    global answers
    global check
    temp_1 = None
    temp_2 = None
    temp_3 = None

    if not questions:
        questions = ["What's 1+2?", "What's the capital of France?"]
        answers = ["3", "5", "2", "4", "Paris", "Africa", "California", "Hawiai"]
        check = [True, False, False, False, True, False, False, False]
    else:
        temp_1 = questions
        temp_2 = answers
        temp_3 = check
    
    run_quiz()
    if temp_1 == None:
        pass
    else:
        questions = temp_1
        answers = temp_2
        check = temp_3


def run_quiz():
    score = 0

    for i in range(len(questions)):
        question_load(questions, answers, i)
        temp_number = take_answer()
        temp_number = (temp_number-1) + (4*i)
        if check[temp_number] == True:
            print("")
            print("Correct!")
            time.sleep(2)
            score = score + 1
        else:
            print("")
            correct = ""
            for u in range(4):
                temp_temp = u + (4*i)
                if check[temp_temp] == True:
                    correct = correct + str(i+1) + " "
            print("Incorrect..." + "\n" + "The correct answer was " + correct)
            time.sleep(2)
        print("")
    print("----------------------------------------------------")
    print("Good job! Your score was " + str(score) + "/" + str(len(questions)) + "!")
    print("----------------------------------------------------")
    time.sleep(4)
    

main_menu()