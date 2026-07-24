#My project
bank_vault = 15000
while True:
    credit=int(input("Enter your credit sum:"))
    if credit == 0:
        print("You have left, Goodbye")
        break
    if credit < 1000:
        print("Error: You can't take less than 1000")
        continue
    if credit < 0:
        print("Error: Sum cannot be negative")
        continue
    if credit <= 5000:
        input("Why do you take credit?:")
        print("Status: Approved, welcome to bank")
        print("If you want to leave, write on credit sum: 0")
        bank_vault = bank_vault = credit
        print(f"There is:" ,{bank_vault} "in cash box")
        
        if bank_vault <= 0:
            print("Bank is closed, money ran out of")
            break
    else:
        print("Status: Denied! Too much risk for the bank!")
        print("If you want to leave, write on credit sum: 0")