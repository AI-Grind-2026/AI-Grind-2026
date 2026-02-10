# Yo Patryk, Day 1 beast mode
name = "Patryk"
weight = 90
height_cm = 183

print(f"Yo {name}, {weight}kg Polish tank at {height_cm}cm – ready to stack AI bread 😈")

# Quick calc: BMI rough
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
print(f"Your BMI: {bmi:.2f} – athletic as fuck")

# Interactive shit
custom_name = input("Enter your street name, homie: ")
print(f"Aight {custom_name}, let's get rich with Python today!")

# Add your boxing stats flex
bench_1rm = 140
pullup_added = 60
reflexes_ms = 170

print(f"Bench beast: {bench_1rm}kg for 2 reps")
print(f"Pull-up with +{pullup_added}kg – grip like a vice")
print(f"Reflexes {reflexes_ms}ms average – faster than most pros")

# Quick conditional (first taste of brain logic)
if reflexes_ms < 200:
    print("Reflex god tier – boxing ring gonna fear you")
else:
    print("Still solid, but train that shit harder")

# Let user input their own stat for fun
custom_stat = input("Enter your proudest lift or reflex time: ")
print(f"Damn, {custom_stat} – that's fire, homie. Keep stacking wins")

# Your own addition – gripper flex
gripper_reps = 20
print(f"Gripper 60kg for {gripper_reps} perfect reps – hands like steel traps")