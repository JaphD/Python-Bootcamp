# Problem 1: Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print(f"Error: Item in the list is not a number.")

print()

# Problem 2: Handle teh exception thrown by the code below using try and except blocks. Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    x / y
except ZeroDivisionError as e:
    print(f"Error: {e}.")
finally:
    print("All Done.")

print()


# Problem 3: Write a function that asks for an integer and prints the square of it. Use a while loop with a try,
# except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            result = int(input("Please enter an integer: "))
            result_squared = result ** 2
        except TypeError:
            print(f"An error occurred! Please try again!")
            continue
        except ValueError:
            print(f"An error occurred! Please try again!")
            continue
        else:
            print(f"Thank you, your number squared is: {result_squared}.")
            break


ask()
