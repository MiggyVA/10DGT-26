# Create a Area/Perimeter calculator
# Author: Miguel Agustin
# Date: 21 May 2026

def num_check(question):
    error = "Please input a number that is more than zero\n"
    while True:
        try:
            # ask user for a number
            response = float(input(question))

            # check if number is more than zero
            if response > 0:
                return(response)
            else:
                print(error)
            
        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":
    # main code
    width = num_check("width: ")
    print(width)

    print()

    height = num_check("height: ")
    print(height)

    # calculations for perimeter and area
    area = height * width
    perimeter = 2 * (height + width)

    # output calculations
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # ask user if they wish to continue
    keep_going = input("Press <enter> or to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator.")

