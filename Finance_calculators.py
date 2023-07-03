import math 

print ("MENU:  ")
print ("investment - calculates the amount of interest you'll earn on your investment")
print("bond - calculate the amount you'll have to pay on a home loan")

customer_choice = input ("Enter either 'investement' or 'bond' from the menu above: ")

# to check for the lower or upper case sensitivity
customer_choice = customer_choice.lower()

#to check is the customer's choice entry is valid 
while customer_choice not in ['investment', 'bond']:
    print ("invalid input. Please enter either 'investment' or 'bond': ")
    customer_choice = input("Enter either 'investement' or 'bond' from the menu above: ")
    customer_choice = customer_choice.lower()
    
if customer_choice == 'investment':
 # ask customer input
    #but i want to make sure that valid entries are given hence I am adding a validation check that i learnt on Youtube
    while True:
        try:
            deposit = float(input("Enter the amount of money you are depositing: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for deposit: ")

    while True:
        try:
            interest_rate = float(input("Enter the interest rate (as a percentage): ")) /100
            break
        except ValueError:
            print("Invalid Entry. Please enter a number for interest rate. ")

    while True:
        try:
            years = int(input("Enter the number of years you plan on investing: "))
            break
        except ValueError:
            print("Invalid entry. Please enter a number for number of years.")

    interest = input("Do you want simple or compound interest? ").lower()
        
     #to calculate the interest and print
    if interest == "simple":
        total_amount = deposit * (1 + interest_rate * years)
        print(f"The total amount after {years} years with simple interest is: {total_amount}")

    #if compound is selected
    elif interest == "compound":
        total_amount = deposit * math.pow((1 + interest_rate), years)
        print(f"The total amount after {years} years with compound interest is: {total_amount}")

    #if an invalid selection is made 
    else:
        print("Invalid input. Please enter either 'simple' or 'compound' for the interest type.")

#but where the choice made is bond, the following is the code
elif customer_choice == "bond":
     #ask customer to input but I also want to make sure only valid entries are allowed
    while True:
         try:
            present_value = float(input ("Enter the present value of your house: "))
            break
         except ValueError:
            input("Invalid entry. Please enter a number for present value of house.")
    while True:
        try:
            bond_interest_rate = float(input("Enter the interest rate: ")) /100 /12
            break
        except ValueError:
            print("Invalid entry. Please enter a number for bond interest rate.")

    #I could have coded months to factor in those customers who would want to pay for example 10 and a half months but decided against it, to make is simple
    while True:
        try:
            number_months = int(input("Enter number of months you want to repay the bond: "))
            break
        except ValueError:
            print("Invalid entry. Please enter a number for a whole number of months. ")

    #to calculate the monthly payment and print
    monthly_repayment = (bond_interest_rate * present_value)/(1 - (1 + bond_interest_rate)**(-number_months))
    print(f"The amount £{round(monthly_repayment,2)} will have to be paid each month for {number_months} months")
