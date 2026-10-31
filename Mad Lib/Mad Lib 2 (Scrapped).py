#Manual varibles
global money
money = 0
global wallet
wallet = 15

global money_wall
money_wall = 0

global desk
desk = 0

global calen
calen = 0

global looking
looking = 0

global charging
charging = 0

global side_table
side_table = 0



#wipes screen (somewhat) at user input
def newline():
    print(" ")
    input("--> ")
    print("\n" * 100)

def clear():
    print("\n" * 100)

################################################################################
print("Developer's note, this story is not in it's fullest state yet. There is still much to squeze out of this concept but I am only working on a draft as of right now. The real story will span over many in-game days (around 3 or 4) where a similer, but more extended, plot will play-out. The draft also has dumb refrences that need to be removed so the story will fit an actual naritive.")
print(" ")
print("On a side note, something that is not obvious, but the 'time of day' choice will decide how the plot will play out and it will change MANY parts of the story. I recomend doing the routes in order. (Morning, Afternoon, Evening, and then Night)")
print(" ")
print("Okay! This was made way after the two previous notes, but I need to mention this! The main character's canonical name is 'Cody'. Also, so far, the nighttime draft has the most detail out of all of them. I do not want to redo the other drafts, insted I am opting to make the full story.")
print("(Progress dialouge by clicking ENTER when you see the text below this line.)")
newline()
print("As my final goodbye to this 'MadLib', I would like to state this as my final note:")
print("First off, I will be scrapping the 'Afternoon' and the 'Evening' routes in order to favor more time to the true story.")
print("This story has advanced into something so large. I am so happy that the idea came to me.")
print("So, please, look into the full story if you get the chance. Please and thank you.")
newline()



print("I might just remove the Deltarune refrence below here. It's anoying in a actual story stand-point...")
newline()

print("It seems")
print("that we meet")
print("again...")
newline()

print("Yet though a new interface.")
print("You return.")
newline()

print("Are you here to see.")
print("Something new?")
newline()

print("In this world,")
print("your choices will matter more than")
print("you expect.")
newline()

print("Choose wisly.")
newline()

noun = input("Enter it's name: ")
while noun == "Lake" or noun == "lake":
    clear()
    print("???: ...")
    print(" ")
    input("???: Enter... a name:")
    clear()
adj = input("Give it an adjective, their defining property: ")
verb = input("Their verb (avoid sufixes, please): ")
store = input("Insert the name of a shopping location: ")
timeofday = input("Select a time ([CASE SENSITIVE!] Morning or Night: ")

while timeofday != "Morning" and timeofday != "Afternoon" and timeofday != "Evening" and timeofday != "Night":
    print("\n" * 100)
    print("It seems,")
    print("you have encountered")
    print("an error.")
    newline()
    print("Please ensure")
    print("that you spelt")
    print("everything correctly.")
    print(" ")
    print("Capitalization matters.")
    print(" ")
    timeofday = input("Morning or Night: ")
    print("\n" * 100)
                
creature = "Dog" #input("Select a pet to visit " + noun + ": ")
cre_name = "Susie" #input("Lend your creature of choice a name: ")
food = "Sushi" #input("Pick an store item: ")
quantity = int(5) #int(input("Decide on a quantity: "))
price = float(15.75) #float(input("Choose your price (a decimal, no symbols, 1.00 - 19.99): "))


nd = noun + ": "


print("\n" * 100)
print("Excellent.")
print("Truly excellent.")
newline()
print("Thank you for your time,")
print("for your creation.")
newline()
print("Go fourth into")
print("this world,")
print(noun + ".")
newline()
print("(Due to restrictions (Of my knowledge) within python, I will use 'Name:' to indicate dialouge.)")
print("(Example:    " + nd + "Hello!!!)")
newline()



#################################################

if timeofday == "Morning":
    print("The sound of my alarm pulls me from my sleep. The sun is rising, slowly cutting though the gaps in my curtians.")
    print("It's 7am, though it is the weekend, I decied to get up sooner than later.")
    print("I go about my morning routine. Getting a shower, fixing my hair, brushing my teeth- I'm out of toothpaste... and of couse there's no extra...")
    newline()
    print("After a little bit, I find myself in the center of my lone apartment again. I need to go to " + store + " today and get some necessities, along with buying " + food + ".")
    newline()
    print(nd + "... alright, what now?")
    newline()
    exit = 0
    

if timeofday == "Afternoon":
    print("The sound of my alarm blares into my ears, startling me awake.")
    print("My phone's screen catches my atention, 3pm")
    print("I ended up getting up later than I wanted...")
    print("I slowly stumble out of bed and get ready for the half of the day I have to get through.")
    newline()
    print("After a little bit, I find myself in the center of my lone room again. I need to go to " + store + " today and buy some " + food + ".")
    newline()
    print(nd + "... what next?")
    newline()
    exit = 0

if timeofday == "Evening":
    print("The sound of my alarm startles me awake.")
    print("The screen of my phone shines into my face, along with the sun's light from my window.")
    print(" ")
    print("5pm")
    newline()
    print("I ended up getting up later than I expected, it's the weekend so it's not a big issue...")
    print(" ")
    print("I slowly stumble out of bed and get ready for the half of the day I have to get through.")
    newline()
    print("After a little bit, I find myself in the center of my lone room again. I need to go to " + store + " today and buy some " + food + ".")
    newline()
    print(nd + "... what next?")
    newline()
    exit = 0

if timeofday == "Night":
    print("Where... am I?")
    print("I'm standing in a dark void, an area deprived of light, though I can make out the shape of my own body.")
    print("... And one of another's")
    print("They stand before me, a very familiar shape.")
    newline()
    print("It looks... like a person... a person that I know...")
    newline()
    print("They reach one hand out slightly, palm of their hand facing up.")
    newline()
    print("It's getting hard to stand. As a feeling simmiler to fear overcomes me, my body gets weak.")
    newline()
    print("I reach out my hand and attempt to lightly grab it, partily restraining myself out of worry.")
    newline()
    print("They use both hands to flip mine over and make me close my it.")
    newline()
    print("Dropping their hand down I open my own... it's... a faint light...?")
    newline()
    print("The light of this item masks it's true form, I have no way to know what it really is.")
    newline()
    print("The person speaks to me, a voice I've yearned to hear one last time...")
    print("???: Don't... forget...")
    newline()
    print("In an instant, I'm ripped back to reality.")
    newline()
    print("Curled up in the blankets of my bed, tears run down my face.")
    print(nd + "A... A dream...")
    print(nd + "It was just... a dream...")
    newline()
    print("I notice something in my hand... it's... a key?")
    print("Did it somehow come from my dream?")
    print("That faint light... is it important?")
    newline()
    
    print("My senses and thoughts return as I realize where I am and who I am.")
    print("It's 9pm, the sun is already down.")
    newline()
    print("I've been... strugling with some issues for a while...")
    newline()
    print("I haven't found a real reason to... keep going like this...")
    print("But I do (unfortunately) have to go to " + store + " today...")
    newline()
    print("I force myself out of bed and get ready for the half of the day I have to get through.")
    newline()
    print("After a little bit, I find myself in the center of my lone room again. I need to go to " + store + " today and buy some " + food + ".")
    newline()
    print(nd + "...")
    exit = 0


while exit == 0:
    clear()
    print("1. Inspect the desk drawers")
    print("2. Check your calender")
    print("3. Look around the room")
    print("4. Check the laptop on the desk")
    print("5. Check the bedside table")
    print("6. leave the apartment (Go to " + store + ")")
    print(" ")
    room_move = int(input("--> Make a number choice: "))
    clear()
    
    if room_move == 1:
        if desk == 0:
            clear()
            print("I decied to walk over and check my drawers on the side of my desk... I found $5.")
            money = int(money) + int(5)
            print("I now have an extra $" + str(money) + " in my pockets. (Not counting my wallet)")
            newline()
        if desk == 1:
            clear()
            print("Haven't I... already checked this?")
            newline()
        desk = 1

    if room_move == 2:
        if calen == 0:
            clear()
            print("The calender hangs as a lone wall decoration near my desk. It reads, 'October 2nd, 20XX'.")
            print(nd + "I guess Halloween is soon. I really enjoy that holiday... how did I forget...?")
            if timeofday == "Night":
                print(" ")
                print(nd + "There's no point in trick-or-treating this year, it's not like I have anyone to go with...")
                print(nd + "Except him... he always loved Halloween...")
                print("Suttle tears fill my eyes.")
                newline()
            else:
                print("I stand there in silence... stuck in a trance...")
                newline()
        if calen == 1:
            print("I feel the need to look at the calender again...")
            newline()
            print("I can't bring myself to do it...")
            newline()
            if timeofday != "Night":
                print("I clench my fist as I feel like I'm going to cry...")
                print("I just want to forget about that night... but I can't...")
                newline()
        calen = 1
            
    if room_move == 3:
        if looking == 0:
            clear()
            print("I pan my eyes around my apartment's bedroom, but there's still little to nothing.")
            print("I've never been big on decorations. There's no point.")
            newline()
        if looking == 1:
            clear()
            print("There's no reason to keep doing that. I have things I need to do.")
            newline()
        looking = 1

    
    if room_move == 4:
        if charging == 1:
            print("The laptop is sitting on the desk, plugged in.")
            print("It might be done charging by tonight.")
        if charging == 2:
            print("The laptop is sitting on the desk, plugged in.")
            print("I don't think it will be charged anytime soon.")
        if charging == 3:
            print("The laptop is sitting on the desk, plugged in.")
            print("There's no reason to wait on it...")
            
        if charging == 0:
            if timeofday == "Morning" or timeofday == "Afternoon":
                print("I notice my laptop, sitting alone on my desk... The batery is around 70% gone, I guess I left it on last night.")
                print("I turn off the device and plug it in.")
                charging = 1
            if timeofday == "Evening":
                print("I notice my laptop, alone on my desk... The screen is lit up, showing a 2% battery warning. I guess I left it on last night.")
                print("I try to turn off the device, but it dies before I can. I shut the lid of the laptop and plug it's charger in.")
                charging = 2
            if timeofday == "Night":
                print("The laptop is alone on my desk, I notice that it's dead but the lid is still open. I guess that I forgot to turn it off yesterday...")
                print("I choose to plug it in, even though there's no reason to, I still feel like I should.")
                charging = 3
        newline()
    
    if room_move == 5:
        if side_table == 1:
            clear()
            print("There's nothing else there.")
            newline()

        if side_table == 0:
            clear()
            if timeofday == "Morning" or timeofday == "Afternoon":
                print("I look over at my bedside table, it's fairly empty. But there's a photograph on the surface... before getting the chance to see it, I flip it over so nobody can.")
            if timeofday == "Evening":
                print("Looking over at my bedside table, my eyes are caught on something... a photograph... it's... me and him... before-... before he-...")
                print("I muster up my little strength I have and slip the photograph into my pocket.")
                photograph = 1
            if timeofday == "Night":
                print("I notice something on my bedside table. It's... a photo...")
                print("I thought I hid this...")
                print(nd + "This was before he... before...")
                if calen == 1:
                    print("I colapse on my bed, starting to cry more than earlier...")
                if calen != 1:
                    print("I slowly sit on the bed, hands shaky... memories of that night rushing back...")
                    print("It was unbarable...")
                newline()
                print("I try my best to speak between sobs,")
                print(nd + "W-Why... Why him?!")
                print(nd + "I-I-I wish I could've... done something... anything!!!")
                newline()
                print("... I don't know how long I've been crying for, but it's been over an hour.")
                print("I stumble out of bed, calmed down a decent ammount, and I choose to head to " + store + " before it closes for the night.")
                print("Before I leave though, I slip the photo into my pocket.")
                photograph = 1
                exit = 1
            newline()
            side_table = 1
    
    if room_move == 6:
        print("(Are you ready to leave, " + noun + "?)")
        print("(You won't come back here again, choose wisly.)")
        exitchoice = 0
        print(" ")
        exitchoice = input("--> (Y/N)?: ")
        if exitchoice == "Y" or exitchoice == "y":
            exit = 1
            clear()
        else:
            exit = 0
    
if exit == 1:
    if timeofday == "Morning":
        # print("Route overview: " + noun + " goes to " + food + " to buy a few items from their shopping list and " + food + ". They encounter their old high school friend Kyle on the way and end up going to the store with them. The store is out in a small quiet area of town, " + noun + " chooses to go to that random area because it's where their childhood friend's grave is. The mention of the dead friend is only shown in the story during the 'Evening' and 'Night' time sections. The route ends with a sense of being incomplete so you will be convinced to try the other routes (time slots).")
        print("(This is the very first draft of the morning route, I am not really proud of it. The Evening and Night routes will be far more detailed than this route.)")
        print("(DRAFT)")
        print(" ")
        print("Leaving my apartment, I walk down the busy paths of the city and make my way to the subway. (I've never been good with crowds...)")
        newline()
        print("After getting though a storm of people on their way to work, I manage to get to the subway and board the train to the other side of town.")
        print("The train is fairly empty since I'm going to a small area away from town. It's always much quieter at their stores.")
        newline()
        print("As I start to zone out and ponder on some stuff that happened the other day, I hear a very familiar voice.")
        print("???: " + noun + "...?")
        print(" ")
        print("Hearing my name strikes me back to reality.")
        newline()
        print("I realize who it is.")
        print(nd + "... Kyle?")
        print("The person sits directly accross from me in confusion.")
        newline()
        print("Kyle: It is you!")
        print("Kyle rushes over drops himself onto the open seat next to me and gives me a playful punch on the sholder.")
        print("Kyle: I haven't seen you since, what, highschool? It's been like, 3 years!")
        print(" ")
        print("He's still WAY too energetic.")
        newline()
        print("(I'm too lazy to give him a discription is the draft. He has an energetic personality, do what you will with that.)")
        newline()
        print("In anxity and confusion, I speak up.")
        print(nd + "O-Oh! I guess it has been that long.")
        print(" ")
        print("Kyle: I know that you moved away near the very end of high school, but how come you ghosted everyone? If I'm right, you and Lake both stopped-")
        print("I cut him off at the mention of that name.")
        print(nd + "STOP!")
        newline()
        print("Kyle looks shocked at my sudden reaction.")
        print(" ")
        print("Kyle: Uhmm, okay...? Bad break-up I suppose?")
        print("He lets out a small chuckle.")
        print("The two of us were really close back than, people thought we were dating. It's stupid... luckily Kyle doesn't know the truth...")
        newline()
        print("We talk about random things relating to our lives since I seperated from the group as the train moves on it's tracks.")
        print("Kyle: Wait, how come you never tried calling us when you left, " + noun + "?")
        print(nd + "Kyle, you changed your phone number. I accidentally called a pizza place when I tried to contact you.")
        print("Kyle: Ohhhhhh... I forgot that I did.")
        print("Of course he did...")
        newline()
        print("As we get closer to the station, Kyle speaks up.")
        print("")
        print("Kyle: Where are you going to?")
        print(nd + "Oh, I'm just going to " + store + ".")
        print("Kyle: Damn, you're going really far out just for that place?")
        print(nd + "I have my reasons.")
        newline()
        print("Kyle: Oh! I just remembered! I was also going to go to " + store + "! I was going to do it later this evening, but this gives us a chance to hang out and catch-up some more!")
        print(nd + "Uhm, I guess so!")
        print(" ")
        print("Kyle: I came out to this area for some other things, but I can delay them for now! I'll be in the area all day anyways!")
        newline()
        print("The train comes to a stop as me and Kyle step out, around 5 people (including us) exit for this area. The station has very few people as well.")
        print("I wasn't lying when I said that it was quiet here.")
        print("Kyle: To be honest, I can't remember where " + store + " is, so I'll just follow you.")
        print(nd + "I thought you said that you used to live here though? And this place is fairly close to where our high school was.")
        print("Kyle: Well, I never really paid enough attention when driving around here. And I never drove in this area often.")
        newline()
        print("We make our way to the store, which is only a five minuite walk from where we are, while making small talk along the way")
        print("Kyle: ... You know, you were always known for being " + adj + " in high school.")
        print(nd + "W-What? Where's that coming from?")
        print("Kyle: It's just something I kept hearing, don't get mad at me!")
        print(nd + "... whatever.")
        newline()
        print("After all that travel, we arive at " + store + ".")
        print("Kyle is still folowing behind me.")
        print("Kyle: This place is a lot different than I remember.")
        print(nd + "It's been like this for a long time, I guess that you're not here often?")
        print("Kyle: I've gone to other " + store + "s, but I haven't been to this one in a while.")
        newline()
        print("Entering the store, the large isles streach before us. I pull out my rather small shoppping list and grab a cart, Kyle does the same.")
        print("Kyle catches a glance at my rather small list,")
        print("Kyle: I assumed you would've had more to buy if you came this far out?")
        print(nd + "Well... there's other reasons I came out here...")
        print("Kyle: What reasons?")
        print("I stay silent.")
        print("Kyle: Uhmmm... okay?")
        newline()
        print("We keep walking, as I grab my items that I need, I also notice that Kyle is grabbing his things")
        print("I've never been one for coversation, so I wait for Kyle to start one.")
        print("Kyle: So... how have you been recently...?")
        print(nd + "Hmm?")
        print("Kyle: I just noticed that you... don't seem well. It's like, you're hiding something.")
        print("Kyle: I get if you don't want to talk about it. But I'm here if you need...")
        print("I stand there, partily across the empty store asile, not facing him")
        print(nd + "...")
        print("Kyle: Is this about Lake-")
        print(nd + "No.")
        newline()
        print("I cut him off instantly, before he can finish talking.")
        print("It's only making my issues more aparent.")
        print("Kyle: Okay, I get it. Sorry for prying.")
        print("Great... he knows now. He's going to figure it out and blame me too... just like everyone else-")
        print("Kyle: " + noun + ". You're spacing out. Let's keep moving.")
        print(nd + "Y-Yah... okay...")
        newline()
        print("We finish our trip though the store. I find the " + food + " that I was going to buy, my toothpaste, and other stuff.")
        print("I'm not sure what Kyle bought, he bought a lot but it somehow fit in the small paper store bags.")
        print(" ")
        print("The cashier's voice snaps me back to reality,")
        print("-- Will that be all?")
        print(nd + "Y-Yes!")
        print("Kyle gives me a conserned glance.")
        newline()
        print("As we walk out the store, Kyle speaks up.")
        print("Kyle: Well, I guess I'll see you later?")
        print("Kyle: Oh wait! I still need your phone number!")
        print(nd + "Yah, I almost forgot...")
        print("Me and him pull out our phones so we can exchange numbers")
        newline()
        print("Kyle turns around and walks off, opposite of where I need to go.")
        newline()
        print("Looking off in the distance near the store, I see a graveyard.")
        print("Spaced out for a moment, thoughts that I can't comprehend cross me.")
        newline()
        print("I snap back to reality.")
        print("Turning the other way, I head back to the train station, the moment just now becoming nothing but a memory...")
        newline()
        print("(Aren't you forgetting something?)")
        
        
        
    if timeofday == "Afternoon":
        print("(Developer's note: I do not give a crap about this route of the game, it will get the LEAST attention in this draft.)")
        print(" ")
        print("This route is a slightly altered version of the 'Morning' route, the overview for that route is as follows:")
        print("Route overview: " + noun + " goes to " + food + " to buy a few items from their shopping list and " + food + ". They encounter their old highs school friend Kyle on the way and end up going to the store with them. The store is out in a small quiet area of town, " + noun + " chooses to go to that random area because it's where their childhood friend's grave is. The mention of the dead friend is only shown in the story during the 'Evening' and 'Night' time sections. The route ends with a sense of being incomplete so you will be convinced to try the other routes (time slots).")
        print(" ")
        print("THIS ROUTE IS NOT FINISHED, PLEASE RESTART THE PROGRAM AND USE THE 'MORNING' TIME OPTION")
        #Slightly altered "Morning" story
    
    
    
    if timeofday == "Evening":
        print("(DRAFT)")
        print(" ")
        print("Route overview: This is similer to the morning route yet has many changes. " + noun + " will go to the store, encounter Kyle, talk with him, part ways, and then buy flowers for Lake (dead friend) and visit his grave, the route ends with him walking from the grave.")
        print(" ")
        print("THIS ROUTE IS NOT FINISHED, PLEASE RESTART THE PROGRAM AND USE THE 'MORNING' TIME OPTION")
        #Evening story, moving on ending
    
    
    
    if timeofday == "Night":
        print("(DRAFT)")
        print(" ")
        print("I put my coat on and exit the door of my apartment, the cold autumn winds cutting though me.")
        print("The streets are quiet and empty, as you would expect at night, even if this is a large city.")
        newline()
        print("With the street lamps and city lights being the only thing to light my path, I make my way to the underground subway.")
        newline()
        print("Though this is how it always is, it is still a shocker when I notice that there are very few people around this late at night.")
        print("Pulling my train-pass from the warm pockets of my jacket, I scan it and continue to the train.")
        newline()
        print("Due to the common lack of people in this place, I'll be heading to a town that's decently far from the city. I'm shocked there's even a train route there in the first place.")
        newline()
        print("Finaly sat-down on the train, I breathe a sigh of relief as I put my headphones in my ears.")
        print("That relief unfortunately doesn't last long, as a familiar voice rings out to me...")
        newline()
        print("???: There's no way...")
        newline()
        print("The familiar looking voice forces me to meet with the person sitting on the opposite side of the train, slightly at an angle from me.")
        newline()
        print("I take the assumption that they're talking to someone nearby, so I look to my left and right... only to be met by empty seats...")
        newline()
        print("???: Holy crap... " + noun + "?!")
        newline()
        print("Parts of memories flood though my mind as I attempt to recall the name of who I'm seeing...")
        print(nd + "Wait... Elizabeth?")
        print("The person gives me an annoyed expression")
        print("Elizabeth?: " + noun + ", I've told you SO MANY times and you still can't say my name properly...?")
        print("She let's out a small chuckle as she moves to sit next to me.")
        newline()
        print("Elizabeth: I go by 'Liz', remember?")
        print(nd + "O-Oh, yah... I just... I have a bad memory, that's all!")
        print("Embarrassment takes me over as I start to recall more of our past.")
        newline()
        print("Liz: I would've never expected to see you here! It's been ages! Where did you go??")
        print(nd + "...")
        print("Liz: If I remember right, you left right around the end of high school...?")
        print(nd + "U-Uhmm... yah...")
        newline()
        print("Liz flashes a confused expression, most likely noticing the tension in my voice.")
        print("Liz: Are you alright? You seem... tense...")
        print(nd + "...")
        newline()
        print("Liz: If you think I'm mad about you leaving, you know that I'm not, right?")
        print(nd + "I'd be shocked if it was true...")
        print("Liz: " + noun + "... you don't have to be so hard on yourself...")
        print("Liz: I'm sure that you had a reason to leave that horible place. I did.")
        newline()
        print("Her words catch my attention, 'I did'.")
        newline()
        print("Did... something happen to her too?")
        newline()
        print("Liz: Think of it this way: you were the first one to leave, but not the only one.")
        print("Liz: Oh right, it would've been bad for you to be there anyways. Kyle started a fire during the graduation ceremony.")
        print("She lets out a small laugh... I don't get how something so extreme could be funny!")
        print(nd + "A... fire?!")
        newline()
        print("The mention of a fire had caused me to overlook something major... that name...")
        print("'Kyle'...")
        print("It sounds... familiar. Yet, I don't know that name...")
        newline()
        print("I franticly look through my mind, trying to find that name... 'Kyle'...")
        newline()
        print("And, as I should've guessed, Liz catches my expression; reading my thoughts instantly.")
        print("Liz: There is no way... no way you forgot who Kyle was...")
        newline()
        print("I jump at the sudden reading of my thoughts being announced.")
        print(nd + "...!")
        print("No words leave my mouth, just a small reaction to the comment made.")
        newline()
        print("Liz looks at me, her face adorned by a confused expresion.")
        print("Liz: Uhhhh... here, I'll show you a photo!")
        newline()
        print("She pulls her phone from her pockets, after failing to enter the pin a few times, she pulls up a photo of... me??")
        print("The photo seems to be cropped, it has me, this 'Kyle' person, and a few others from a group. Their faces are out of frame.")
        newline()
        print("Before any words can carry between the two of us, the train comes to a slow.")
        newline()
        print("Liz: Oh, the train's stopping. I hadn't realized we were almost here.")
        newline()
        print(nd + "Same.")
        newline()
        print("I stand up and stretch a little. It could be because of the exausting social interaction, but it feels like I was on that train much long than 20 minutes.")
        newline()
        print("I look to my side and realize that Liz is walking up ahead already. She looks back at me,")
        print("Liz: Hurry up, idiot! They'll leave you on the train!")
        newline()
        print("I realize that I've been standing there and blankly staring at Liz.")
        newline()
        print(nd + "Oh! Sorry! Coming!")
        print("I quickly try to catch up to Liz, almost bumping into a stranger in the process.")
        newline()
        print("After I catch up to them we continue on our way to " + store + ".")
        newline()
        print("Liz: ...")
        print(nd + "...")
        newline()
        print("The scilence felt odd, but comforting.")
        newline()
        print("(Developer's note: In favor of working on the full relese of this story, I will be rushing the ending of this 'MadLib' version. The morning route contains more story then the night route, but the night route is more canonical to the full story. Read as you so choose.)")
        newline()
        print("Eventualy we make it to the store, not much of note other than small talk between me and Liz.")
        newline()
        print("Once we exit the store, Liz mentions something.")
        newline()
        print("Liz: Oh right, I haven't gotten your contact info.")
        newline()
        print("They pull their phone out their pocket once more.")
        newline()
        print(nd + "I almost forgot.")
        newline()
        print("I pull my phone out of my cold jacket pocket, the fall wind draining the heat from the tiny block of metal in my hand")
        newline()
        print("(We exchange information.)")
        newline()
        print("Liz: Well... I guess we'll be in touch?")
        newline()
        print(nd + "I hope so.")
        newline()
        print("Liz: Just... don't vanish on me again, okay?")
        newline()
        print(nd + "Don't worry, I won't.")
        newline()
        print("Liz, standing infront of me, slowly turns around giving me one final glance as they walk off the other way into the cold fall night.")
        newline()
        print("I turn my head to the side, a noise catching my ear.")
        newline()
        print("My eyes set on a cematary nearby.")
        newline()
        print("(Aren't you forgetting something?)")