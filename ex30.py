people = 15
cars = 15
trucks = 30


if cars > people:
    print("Ride in the car")
elif cars < people:
    print("Don't ride in the car")
else:
    print("We can't choose")

if trucks > cars:
    print("So many trucks")
elif trucks < cars:
    print("Maybe ride in the truck?")
else:
    print("We still can't choose")

if people > trucks:
    print("Ok, let's ride in the truck")
else:
    print("Fine, let's stay at home")
