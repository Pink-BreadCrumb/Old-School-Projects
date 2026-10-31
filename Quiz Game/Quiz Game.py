score = 0

print("Multiple-Choice Quiz Game:")

print("Does the number 1 equal 1?")
print("a) Yes")
print("b) No")
print("c) Sometimes")
print(" ")
answer1 = input("-->")
print(" ")
if answer1 == "a":
    print("Correct... for very obvious reasons.")
elif answer1 == "b":
    print("... that's incorrect. Better yet, how did you get that wrong???")
elif answer1 == "c":
    print("Incorrect... what do you mean 'sometimes'???")
if answer1 == "a":
    score = score + 1
print(" ")
print("Who owns Microsoft?")
print("a) Bill Gates")
print("b) Steve Jobs")
print("c) @grok answer this for me")
print(" ")
answer2 = input("-->")
print(" ")
if answer2 == "a":
    print("Correct.")
elif answer2 == "b":
    print("Incorrect.")
elif answer2 == "c":
    print("@grok: 'Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975.'")
if answer2 == "a" or answer2 == "c":
    score = score + 1
print(" ")
print("How many bananas are the leathal amount for a human?")
print("a) 50 million bananas")
print("b) 5 bananas")
print("c) 4765 bananas")
print(" ")
answer3 = input("-->")
print(" ")
if answer3 == "a":
    print("Correct.")
elif answer3 == "b":
    print("... incorrect.")
elif answer3 == "c":
    print("Incorrect")
if answer3 == "a":
    score = score + 1


print(" ")
print("You got " + str(score) + "/3 correct.")
if score == 0:
    print("... you did that on purpose.")
if score == 1:
    print("You've got... room for improvment.")
elif score == 2:
    print("You almost got them all.")
elif score == 3:
    print("Congrats! You got them all right!")
if score < 0:
    print("... how did you even get that score!? You aren't meant to!")