#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator! ")
input_bill = (input("What was the total bill? ")) #type in currency format
actual_bill = float(input_bill.replace('$', '')) #removes the dollar sign to convert to float
indv_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

indv_bill = (actual_bill/total_people) 
tip = (indv_tip/100) + 1
bill_with_tip = indv_bill * tip
print(f"Each person should pay: ${bill_with_tip:.2f}")

      