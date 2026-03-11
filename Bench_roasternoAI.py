import random

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

import random
ROASTS = ["under 50 kg nga you weak af",
          "YOU ARE A LOSER, YOU ARE A FAILURE, YOU ARE A WASTE OF SPACE, YOU ARE A DISGRACE TO YOUR FAMILY, YOU ARE A DISGRACE TO YOUR COUNTRY, YOU ARE A DISGRACE TO THE HUMAN RACE, YOU ARE A DISGRACE TO THE UNIVERSE, YOU ARE A DISGRACE TO EVERYTHING, YOU ARE A DISGRACE TO NOTHING",
          "so the ai roasted tf out of me {name} and now i have to roast it back with code, this is so sad",
            "you are so bad at coding, you can't even write a simple hello world program"
          ]
ROASTSS = ["Lmao so what u think ill believe ur natty","Japanese reasearch chemicals pumped mfker","so your pretty strong huh? you must be a steroid user","ermm what the flip"]
name = input("what is your name?")
if name == "Patryk":
    print("My dumbass nga creator")
else: print("youre not my creator nga")

bench = input("How much is your max bench?(kg)")
try:
    bench_val = float(bench)
except ValueError:
    print(RED + "U think im dumb thats not a number nga" + RESET)
else:
    if bench_val <50:
        print(random.choice(ROASTS))
    else: 
        print(random.choice(ROASTSS))
Reps = input("Aight and how many reps?")
if int(Reps) >2:
    print("Aigt so cardio type shi?")
else:
    print("yeah aight zero cardio dumbass nig-")
if int(Reps) >2:
    print("aha aha so either youre strong or a fatass anyways im going to jerk off-") 
else:
    print("Yeah zero cardio wannabe strongman")
if input("") == "wait":
    print("Nah fuck off... twin 🙏")
else:
    print("🖕")



        

        
    




