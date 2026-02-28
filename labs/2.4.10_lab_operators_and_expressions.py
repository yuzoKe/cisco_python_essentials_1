"""
2.4.10 LAB - Operators and expressions

Scenario
Take a look at the code in the editor: it reads a float value, puts it into a variable named x,
and prints the value of a variable named y. Your task is to complete the code in order 
to evaluate the following expression:

3x^3 - 2x^2 + 3x - 1

The result should be assigned to y.

Remember that classical algebraic notation likes to omit the multiplication operator ‒ you need to use it explicitly.
Note how we change data type to make sure that x is of type float.

Keep your code clean and readable, and test it using the data we've provided, each time assigning it to
the x variable (by hardcoding it). Don't be discouraged by any initial failures. Be persistent and inquisitive.

"""
# Sample Input
# x = 0; y = -1.0
# x = 1; y = 3.0
# x= -1; y = -9.0
# ---
# Provided code
# x =  # Hardcode your test data here.
# x = float(x)
# Write your code here.
# print("y =", y)
# ---

x = 0
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

x = 1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

x = -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)
