"""
2.6.11 LAB - Operators and Expressions 2

Scenario
- Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number
of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59).
The result has to be printed to the console.

- For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

- Don't worry about any imperfections in your code.
it's okay if it accepts an invalid time.
the most important thing is that the code produces valid results for valid input data.

- Test your code carefully. Hint: using the % operator may be the key to success.

TEST DATA
Sample Input1: 12h 17m 59s
Expected output1: 13:16

Sample Input2: 23h 58m 642s
Expected output2: 10:40

Sample Input3: 0h 1m 2939s
Expected output3: 1:0

----------------------------------------
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
----------------------------------------

"""
# ----------------------------------------
# My First try
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# mtotal = hour*60 + mins + dura
# mremainder = mtotal % 60
# print(round(mtotal / 60), mremainder, sep=":")
# ----------------------------------------

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura  # find a total of all minutes
hour = hour + mins // 60  # find a number of hours hidden in minutes and update the hour
mins = mins % 60  # correct minutes to fall in the (0..59) range
hour = hour % 24  # correct hours to fall in the (0..23) range
print(hour, mins, sep=":")

# At first, I was confused about why 13 % 24 equals 13 and not 10.
# I was thinking in terms of regular division, where 13/24 is about 0.5,
# and expected a remainder of something like 10 (e.g., 130 - 120 = 10).
# But the modulus operator (%) gives the *remainder* after division.
# Since 24 doesn't fit even once into 13, the remainder is just 13 itself.
# This helped me understand how % keeps values within a cycle, like 0–23 hours.
