from sys import exit

def start():
    print "I'm sorry to tell you that you were chosen by death."
    print "Do you choose death or change your fate? "
    print "Now make your present."

    next = raw_input("> ")

    if next == "change my fata" or "change":
        alive_room()
    elif next == "death" or "dead":
        death_room()
    else:
        dead("You chose wrong, you died.")

def alive_room():
    print "Pretty good. You chose to live. Now you're alive here."
    print "People live to make a lot of sacrifices, are you ready?"
    print "yes? or no?"

    next = raw_input("> ")
    if next == "yes":
        life_room()
    elif next == "no":
        dead("You coward, you're dead.")
    else:
        dead("You chose wrong, you died.")

def life_room():
    print "You are brave. Now you're life here."
    print "Now please choose whether to discard the material life you have."
    print "yes? or no?"

    next = raw_input("> ")
    if next == "yes":
        healthy_room()
    elif next == "no":
        dead("You coward, you're dead.")
    else:
        dead("You chose wrong, you died.")

def healthy_room():
    print "Good job. Now you're healthy here."
    print "You have no substance now, and are you willing to lose your health in order to live?"
    print "yes? or no?"

    next = raw_input("> ")
    if next == "yes":
        family_room()
    elif next == "no":
        dead("You coward, you're dead.")
    else:
        dead("You chose wrong, you died.")

def family_room():
    print "You are brave.But you're very weak now."
    print "Now you're family here."
    print "Now, would you like to desert your family for the sake of your life?"
    print "Please tell me your answer,yes or no?"

    next = raw_input("> ")
    if next == "yes":
        print "You survived, but you lost your life, your health, and your family."
        exit(0)
    elif next == "no":
        dead("So you're willing to give up everything for your family, I admire you, but you're still dead.")
    else:
        dead("You chose wrong, you died.")

def dead(why):
    print why
    exit(0)

def death_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        alive_room()
    elif next == "no":
        death1_room()
    else:
        dead("You chose wrong, you died.")

def death1_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        alive_room()
    elif next == "no":
        death2_room()
    else:
        dead("You chose wrong, you died.")

def death2_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        alive_room()
    elif next == "no":
        death3_room()
    else:
        dead("You chose wrong, you died.")

def death3_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        alive_room()
    elif next == "no":
        death4_room()
    else:
        dead("You chose wrong, you died.")

def death4_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        alive_room()
    elif next == "no":
        death5_room()
    else:
        dead("You chose wrong, you died.")

def death5_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        alive_room()
    elif next == "no":
        death6_room()
    else:
        dead("You chose wrong, you died.")

def death6_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        alive_room()
    elif next == "no":
        death7_room()
    else:
        dead("You chose wrong, you died.")

def death7_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        alive_room()
    elif next == "no":
        death8_room()
    else:
        dead("You chose wrong, you died.")

def death8_room():
    print "There is a death here."
    print "Actually, I don't want to embarrass a person who wants to die."
    print "So would you like to live now? yes or no?"

    next = raw_input("> ")

    if next == "yes":
        print "A close call!"
        print "Good job, you win!"
        exit(0)
    elif next == "no":
        dead("I can't stand you, go to hell!")
    else:
        dead("You chose wrong, you died.")

start()
