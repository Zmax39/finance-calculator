import math

# Greeting message
print("This is a financial calculator with 2 different options!\n")

# Input from user will get them to select an option
user_option = str(input("Please choose an Option from the list below.\n\n Investment\t- To calculate the amount of interest you'll earn on your investment\nBond\t- To calculate the amount you'll have to repay on a home loan\n\nPlease now input your Option: "))

# if statement that will decide what to do next when investment is inputted (.lower() is used to accept any variation of the capitilisation of 'investment')
if user_option.lower() == "investment":
    deposit_amount = float(input("\n""Please Enter the amount of money you will be depositing in £: "))
    interest_rate = float(input("Please enter your interest rate as a %: "))
    years_of_investing = float(input("Please enter the number of years you plan to invest for: "))
    interest_option = str(input("Please input your interest option - 'Simple' or 'Compound': "))
# if/elif/else statements used to run code depending on the interest option selected
    if interest_option.lower() == "simple":
        total_simple_amount = deposit_amount * (1+(interest_rate/100)*years_of_investing)
        print("\n"f"The amount of money you will get back is £{total_simple_amount}.")
    elif interest_option.lower() == "compound":
        total_compound_amount = deposit_amount * math.pow((1+(interest_rate/100)), years_of_investing)
        print("\n"f"The amount of money you will get back is £{round(total_compound_amount, 2)}.")
    else:
        print("Error, Please Select from the valid options!")
# elif statement to run the code if bond is inputted
elif user_option.lower() == "bond":
    house_value = float(input("\n" "Please enter the value of your house in £: "))
    interest_rate = float(input("Please enter your current interest rate as a %: "))
    bond_repayment = float(input("Please enter how many months you plan on taking to repay the bond: "))
    rate = interest_rate / 100 / 12
    total_bond_payment = house_value * (rate * (1 + rate) ** bond_repayment) / ((1 + rate) ** bond_repayment - 1)
    print("\n" f"The total amount you will pay monthly on the bond is £{round(total_bond_payment, 2)}!")
else:
    print("Error, Please Select Either 'Investment' or 'Bond'!")