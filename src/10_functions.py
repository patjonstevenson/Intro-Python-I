# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    return num % 2 == 0

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def print_even_or_odd(num):
    if is_even(num):
        print("Even!")
    else:
        print("Odd")

print_even_or_odd(num)
