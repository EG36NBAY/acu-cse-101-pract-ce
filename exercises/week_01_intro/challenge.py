# ==============================================================================
# ACU CSE 101: Week 01 Graded Challenge - The Way of the Program & Variables
# Think Python: Chapters 1 & 2
#
# GRADED INDEPENDENT CHALLENGE:
# Complete the 5 challenges below on your own.
# Run tests with the 'Run Tests' button or pytest to verify your solutions!
# ==============================================================================

import random
import math
import math  # noqa: F401

# ------------------------------------------------------------------------------
# Challenge 1: Travel Currency Converter
# A student is traveling abroad and exchanging Euros (EUR) to US Dollars (USD).
# The exchange desk charges a 2% transaction fee on the gross USD amount.
#
# Task:
# 1. Prompt user for:
#    - Amount in EUR (float): float(input("Enter amount in EUR: "))
#    - Exchange rate (float): float(input("Enter exchange rate (EUR to USD): "))
# 2. Calculate:
#    - gross_usd = euros * rate
#    - fee = gross_usd * 0.02
#    - net_usd = gross_usd - fee
# 3. Print the amounts formatted to 2 decimal places:
#    print(f"Gross USD: ${gross_usd:.2f}")
#    print(f"Fee: ${fee:.2f}")
#    print(f"Net USD: ${net_usd:.2f}")
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 1 below:
amount_eur = float(input("Enter amount in EUR:"))
exchange_rate = float(input("Enter exchange rate(EUR to USD)\n"))
gross_usd = amount_eur * exchange_rate
fee = gross_usd * 0.02
net_usd = gross_usd - fee
# i wondered why we used the dolar sign first at the first look tbh i got it later
print(f"Gross USD: ${gross_usd:.2f}")
print(f"Fee: ${fee:.2f}")
print(f"Net USD: ${net_usd:.2f}")
# ------------------------------------------------------------------------------
# Challenge 2: Pizza Party Slices & Leftovers
# You are hosting a computer science pizza party!
# Slices must be distributed evenly among all students, and any leftover
# slices go to the hard-working TAs.
#
# Task:
# 1. Prompt user for:
#    - Number of students (int): int(input("Enter number of students: "))
#    - Number of pizzas (int): int(input("Enter number of pizzas: "))
#    - Slices per pizza (int): int(input("Enter slices per pizza: "))
# 2. Calculate:
#    - total_slices = pizzas * slices_per_pizza
#    - slices_per_student = total_slices // students  (integer division)
#    - leftover_slices = total_slices % students      (remainder / modulo)
# 3. Print the results:
#    print(f"Total slices: {total_slices}")
#    print(f"Slices per student: {slices_per_student}")
#    print(f"Leftover slices: {leftover_slices}")
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 2 below:
Amount_Student = int(input("Enter number of students: "))
Number_pizza = int(input("Enter number of pizzas: "))
Slice_per_pizza = int(input("Enter slices per pizza:\n "))
Spp = Slice_per_pizza
total_slice = Number_pizza*Spp
sps = total_slice // Amount_Student
leftover_slices = total_slice % Amount_Student
print(f"Total slices: {total_slice}")
print(f"Slices per student: {sps}")
print(f"Leftover slices: {leftover_slices}")
# ------------------------------------------------------------------------------
# Challenge 3: Sphere Geometry (Volume & Surface Area)
# Think Python Exercise 2.2:
# The volume of a sphere with radius r is (4/3) * pi * r^3,
# and its surface area is 4 * pi * r^2.
#
# Task:
# 1. Prompt user for:
#    - Radius of the sphere (float): float(input("Enter sphere radius: "))
# 2. Calculate volume and surface area using math.pi and the ** operator.
# 3. Print the results formatted to 2 decimal places:
#    print(f"Sphere Volume: {volume:.2f}")
#    print(f"Sphere Surface Area: {surface_area:.2f}")
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 3 below:
# first time using import math for pi
radius = float(input("Enter sphere radius: \n"))
volume = (4 / 3) * math.pi * (radius ** 3)
surface_area = 4 * math.pi * (radius ** 2)
print(f"Sphere Volume: {volume:.2f}")
print(f"Sphere Surface Area: {surface_area:.2f}")
# ------------------------------------------------------------------------------
# Challenge 4: 3-Cup Shell Game (Cyclic Variable Rotation)
# In class we swapped 2 variables (a, b = b, a).
# Now let's perform a 3-cup cyclic rotation in a single multiple assignment!
# Cup A receives Cup C's item, Cup B receives Cup A's item, and Cup C receives Cup B's item.
#
# Task:
# 1. Prompt user for:
#    - Item in Cup A: input("Enter item in Cup A: ").strip()
#    - Item in Cup B: input("Enter item in Cup B: ").strip()
#    - Item in Cup C: input("Enter item in Cup C: ").strip()
# 2. Perform the circular rotation in ONE assignment statement:
#    cup_a, cup_b, cup_c = cup_c, cup_a, cup_b
# 3. Print the rotated cups separated by ' -> ' using sep:
#    print(cup_a, cup_b, cup_c, sep=" -> ")
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 4 below:
cup_a = input("Enter item in Cup A: ").strip()
cup_b = input("Enter item in Cup B: ").strip()
cup_c = input("Enter item in Cup C: ").strip()
cups = [cup_a, cup_b, cup_c]
random.shuffle(cups)
print(*cups, sep=" =>")
# ------------------------------------------------------------------------------
# Challenge 5: Digital Event Badge Generator
# Generate a formatted conference badge for attendees using string methods
# (.strip, .title, .upper), string repetition (*), and character count (len).
#
# Task:
# 1. Prompt user for:
#    - Attendee full name (str): input("Enter attendee name: ").strip()
#    - Department (str): input("Enter department: ").strip()
#    - Role (str): input("Enter role: ").strip()
# 2. Transform the text:
#    - Format name in title case: name.title()
#    - Format department in uppercase: dept.upper()
#    - Format role in title case: role.title()
# 3. Print the badge decorated with a 32-character border of '#' characters:
#    border = "#" * 32
#    print(border)
#    print(f"NAME: {name}")
#    print(f"DEPT: {dept}")
#    print(f"ROLE: {role}")
#    print(f"NAME LENGTH: {len(name)}")
#    print(border)
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 5 below:

full_name = input("Enter attendee name: ").strip().title()
department = input("Enter department: ").strip().upper()
role = input("Enter role: ").strip().title()

border = ("#" * 32 + "\n") * 2
print(border, end="")
print(f"NAME: {full_name}")
print(f"DEPT: {department}")
print(f"ROLE: {role}")
print(f"NAME LENGTH: {len(full_name)}")
print(border, end="")

# i gotta work on those basic imports tbh.
