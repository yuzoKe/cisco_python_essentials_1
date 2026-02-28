"""
2.6.9 LAB - Simple input and output

Scenario

- Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
- The results have to be printed to the console.
- You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.
- Test your code ‒ does it produce the results you expect?
- We won't show you any test data ‒ that would be too simple.

The code:
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))

# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here

print("\nThat's all, folks!")

"""
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))

print("The addition of", a, "and", b, "results", a + b)
print("The multiplication of", a, "and", b, "results", a * b)
print("The division of", a, "and", b, "results", a / b)
print("The subtraction of", a, "and", b, "results", a + b)

print("\nThat's all, folks!")
