# Create a fence cost calculator
# Author: Miguel Agustin
# Date: 22 May 2026

def num_check(question):
    error = "Please enter a number more than zero\n"
    
    while True:
        try:

            # ask user for number
            response = float(input(question))

            # checks if input is more than zero and is a number
            if response > 0:
                return(response)
            else:
                print(error)

        except ValueError:
                print(error)

print()
print("Welcome to the fence cost calculator.\n")

loop = ""
while loop == "":
    
    # asks to input values for width, length and cost / m of fence
    width = num_check("Width: " )
    print(width)

    print()

    length = num_check("Length: ")
    print(length)

    print()

    cost = num_check("Cost / m: ")
    print(cost)

    # calculation of fence cost
    fence_cost = 2 * (length+width) * cost
    
    # output
    print(f"The total cost of your fence is ${fence_cost}")
    
    # asks if user wishes to make another calculation
    loop = input("Press <enter> if you wish to make another calculation or any key to quit.")
    print()

print("Thank you for using the Fence Cost calculator.")
