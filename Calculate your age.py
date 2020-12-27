# This script is for calculate you age in all time units
age = int(input('Type your age===>').strip())

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("You lived for: " )
print(f"{months} Monthes.")
print(f"{weeks} Weeks.")
print(f"{days} Days.")
print(f"{hours} Hours.")
print(f"{minutes} Minutes.")
print(f"{seconds} Seconds.")
