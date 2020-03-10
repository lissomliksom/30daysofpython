'''
GOAL:
Do all exercises in "Python Crash Course" by 15.3.2020
This script counts the remaining days and exercises.
'''

from datetime import date

today = date.today()

# Get date in format DD/MM/YYYY
date_current = today.strftime("%d/%m/%Y")
date_end = "15/03/2020"

# Convert first two numbers of dates to integers and calculate remaining days.
days_remaining = int(date_end[:2]) - int(date_current[:2])

# List remaining exercises in all remaining chapters
exercises = {
  'Chapter 6': 0,
  'Chapter 7': 0,
  'Chapter 8': 6,
  'Chapter 9': 16,
  'Chapter 10': 13,
  'Chapter 11': 3,
}

exercises_remaining = 0

# Loop through, count and add up remaining exercises
for exercise in exercises.values():
  exercises_remaining += exercise

# Calculate and print days, exercises and target exercises per day
print(f"Days remaining: {days_remaining}")
print(f"Exercises remaining: {exercises_remaining}")
print(f"Exercises per day: {int(exercises_remaining/days_remaining)}")
