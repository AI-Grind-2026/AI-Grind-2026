import random  

ROASTS = [
    "under 50 kg nga you weak af",
    "YOU ARE A LOSER, YOU ARE A FAILURE, YOU ARE A WASTE OF SPACE, YOU ARE A DISGRACE TO YOUR FAMILY, YOU ARE A DISGRACE TO YOUR COUNTRY, YOU ARE A DISGRACE TO THE HUMAN RACE, YOU ARE A DISGRACE TO THE UNIVERSE, YOU ARE A DISGRACE TO EVERYTHING, YOU ARE A DISGRACE TO NOTHING",  # fixed closing quote
    "so the ai roasted tf out of me {name} and now i have to roast it back with code, this is so sad",
    "you are so bad at coding, you can't even write a simple hello world program"
]

name = input("what is your name? ")
if name == "Patryk":
    print("My dumbass nga creator")
else:
    print("youre not my creator nga")

bench = input("How much is your max bench? (kg) ")
try:
    bench_val = float(bench)
except ValueError:
    print("U think im dumb thats not a number nga")
else:
    if bench_val < 50:
        print("Weak ahh nga bro thinks hes twelve")
    else: 
        print("Dumbass strengh japanese reasearch chemicals loaded mf")

# New: reps part (fixed)
reps_input = input("Aight and how many reps at that weight? ")
try:
    reps = int(reps_input)
except ValueError:
    print("That's not a number nga, try again")
else:
    if reps < 8:
        print("Trash – hit the push-ups instead")
    elif reps <= 12:
        print("Mid – solid, but push for beast next set")
    else:
        print("Beast mode – shoulders crying, Lambo closer 😈")

    
    roast = random.choice(ROASTS)
    if "{name}" in roast:
        roast = roast.format(name=name)
    print("Here's your roast:", roast)