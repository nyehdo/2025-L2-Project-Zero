# functions go here
def int_check(question):
    """checks user enter an integer"""

    error = "Ooops - please enter an integer more than zero."

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == "xxx":
            return response

        try:
            # change the response to an integer and check that it's more than zero
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here


# loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = input("Name: ")  # replace with call to not blank function

    # ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")

