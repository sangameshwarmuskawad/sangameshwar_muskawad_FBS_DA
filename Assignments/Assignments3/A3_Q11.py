# take input
ticket_price = int(input("Enter ticket price per person: "))

total_amount = 0

# check condition
for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    
    if(age > 12):
        amount = ticket_price * 0.7
    elif(age > 59):
        amount = ticket_price * 0.5
    else:
        amount = ticket_price
    
    total_amount += amount

print("Total ticket amount for all 5 people:", total_amount)    
