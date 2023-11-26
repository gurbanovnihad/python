#!/usr/bin/python3

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12 or 15? ")
person_count = input("how many people to split the bill? ")

total_bill_tip = int(total_bill) + int(total_bill) * int(tip_percent)/100

pay_per_person = round(total_bill_tip / int(person_count), 2)

print("Each person should pay: ${}".format(pay_per_person))

