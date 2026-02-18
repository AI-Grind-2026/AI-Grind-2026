# Day 2 – Patryk's Stat Sheet Beast Mode
# We're using LISTS and LOOPS to flex everything at once

# List = collection of stuff in [] brackets
stats = [
    "Bodyweight: 90kg",
    "Height: 183cm",
    "Bench 1RM: 140kg x2",
    "Pull-up added: +60kg",
    "Gripper: 60kg x20 perfect reps",
    "Reflexes: 170ms average",
    "BMI: ~26.8 – athletic as fuck"
    "Flexibility: can touch toes with ease"
    "Endurance: 5km run in 20 minutes"
    "Sleep: 8 hours/night, no excuses"
]

# Print the whole list automatically with a LOOP
print("=== PATRYK'S FULL BEAST MODE STAT SHEET ===")
print("Generated on Feb 18, 2026 – back from the fever war 💀")

# for loop = "for each thing in the list, do this"
for stat in stats:
    print(f"- {stat}")

# Add your gripper flex again (just for fun)
print("\nHands like steel traps – gripper 60kg x20 🔥")

# Interactive: Let user add a new stat
new_stat = input("\nAdd your proudest new win or stat (or type 'skip'): ")
if new_stat.lower() != 'skip':
    stats.append(new_stat)  # .append adds to the list
    print("\nUpdated stat sheet with your new flex:")
    for stat in stats:
        print(f"- {stat}")
else:
    print("Aight, skipping. Stay hungry tho 😈")

if new_stat == "Bench":
    print("\nLets go my Nigga, hope Grok my g sees that shi!")