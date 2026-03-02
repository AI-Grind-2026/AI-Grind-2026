# Day 3 – Patryk's Reusable Beast Functions (upgraded with AI help)
# Functions = code you can call again and again like a tool

def print_beast_stats():
    """Prints your full tank stats automatically"""
    print("=== PATRYK BEAST MODE STATS v3 ===")
    print("90kg Polish tank | 183cm | High T since 15")
    print("Bench 140kg x2 | Pull-ups +60kg | Gripper 60kg x20")
    print("Reflexes 170ms | Survived 39° fever TWICE 💀")
    print("Back grinding Feb 23 – Lambo fund loading 😈\n")

def calculate_bmi(weight_kg, height_cm):
    """Calculates BMI – reusable for anyone"""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    print(f"Your BMI: {bmi:.2f}")
    if bmi < 25:
        print("Athletic zone – keep eating clean")
    elif bmi < 30:
        print("Tank mode – solid")
    else:
        print("Cut a little if you want, still a beast")
    return bmi

def add_new_win(win_description):
    """Adds a new win to your mental list (future database vibe)"""
    print(f"NEW WIN UNLOCKED: {win_description}")
    print("Logged in the grind book 🔥\n")
    return win_description

def survived_fever(days):
    """Simulates surviving a fever for a certain number of days"""
    print(f"Survived {days} days of fever like a true beast! 💀")
    if days >= 10:
        print("DOUBLE DIGIT WARRIOR – opps got SMOKED twice 😤🔥")
    elif days >= 5:
        print("Round 2 survivor – body said NOT TODAY 💪")
    else:
        print("Quick recovery – still a tank")
    return days


def roast_day(day):
    """Prints a day-specific roast based on the weekday string."""
    roasts = {
        'monday': "Mondays... you woke up the wrong side of the mass.",
        'tuesday': "Tuesday? Same as Monday but you still didn't lift.",
        'wednesday': "Hump day! More like slump day for your gains.",
        'thursday': "It's almost Friday and you're still online, what a shock.",
        'friday': "Friday night and you're coding? You need a life, bro.",
        'saturday': "Weekend? Your excuse for skipping cardio again.",
        'sunday': "Sunday scaries but you should be prepping not panicking.",
    }
    roast = roasts.get(day.lower())
    if roast:
        print(roast)
    else:
        print("That's not a weekday, try again next time—at least pick a real one.")
    return roast

# === MAIN EXECUTION – run everything here ===

# Roast based on the current weekday
while True:
    today = input("What day is it today? ").strip()
    if not today:
        print("Come on, type a day of the week, bro.")
        continue
    roast = roast_day(today)
    if roast:
        break
    # if roast was None, loop again

print_beast_stats()

my_bmi = calculate_bmi(90, 183)

# Interactive fever survivor
while True:
    fever_input = input("How many days did you survive the fever this time? (number only, or 'skip'): ")
    if fever_input.lower() == 'skip':
        print("Aight, skipping fever log. Still a survivor tho 😈")
        break
    try:
        days = int(fever_input)
        survived_fever(days=days)
        break
    except ValueError:
        print("Bro, enter a NUMBER or 'skip' – try again 💀")

# Interactive win logger
new_win = input("\nEnter today's win (e.g. 'Coded Day 3 upgraded' or 'Gym after fever'): ")
if new_win.strip():
    add_new_win(new_win)
else:
    print("No new win logged? Get after it tomorrow, tank 😈")