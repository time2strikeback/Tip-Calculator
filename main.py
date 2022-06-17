print("Welcome to the Tip Calculator")
bill= float(input("what was the total bill? Rs "))
tip = int(input("How much tip Would you like to give? 10 , 12 , 15? "))
people = int(input("How Many People to split the bill ? "))
tip_percentage = tip / 100
total_tip= bill * tip_percentage
total_amount = bill+total_tip
final_amount= round(total_amount/people,2)
print(f"Everyone should pay Rs {final_amount} Each")
