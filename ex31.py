print("""You are in the dark room with two doors.
Which one you will go to - 1 or 2 ?""")

door = input(">")

if door == "1":
    print("In this room giant bear eating cheese 'Friends'.")
    print("Your moves?")
    print("1. Take cheese.")
    print("2. Scream to bear's ear.")

    bear = input("> ")

    if bear == "1":
        print("Bear eats your face off. Good job!")
    elif bear == "2":
        print("Bear eats your leg off. Good job!")
    else:
        print(f"Fine, this move {bear} was only right move")
        print("Bear ran away.")

elif door == "2":
    print("You look into the endless abyss of Cthulhu's eyes. Your moves?")
    print("1. Tell Ctulhu about of some Syberia story.")
    print("2. Touch yellow clotherspins")
    print("3. Try wistle the melody 'Black raven'")

    ctulhu = input("> ")

    if ctulhu == "1" or ctulhu == "2":
        print("You was keep your life because Ctulhu turned into the jelly")
        print("It's amazing!")
    else:
        print("Ctulhu embraced you and you fell into the dark pool")
        print("It's amazing!")

else:
    print("Insanity embraced you and take off your face. Good job!")
