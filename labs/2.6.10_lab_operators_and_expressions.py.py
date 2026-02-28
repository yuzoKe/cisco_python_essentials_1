"""
2.6.10 LAB - Operators and expressions

Scenario
Your task is to complete the code in order to evaluate the following expression:

    1
  ---------
        1
  x + -------
          1
      x + -----
            1
        x + -
            x

The result should be assigned to y. Be careful ‒ watch the operators and keep their priorities in mind. 
Don't hesitate to use as many parentheses as you need.
You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.

TEST DATA
Sample Input1 : 1
Expected output1: y = 0.6000000000000001

Sample Input2 : 10
Expected output2: y = 0.09901951266867294

Sample Input3 : 100
Expected output3: y = 0.009999000199950014

Sample Input4 : -5
Expected output4: y = -0.19258202567760344

----------------------------------------
x = float(input("Enter value for x: "))

# Write your code here.

print("y =", y)
----------------------------------------



"""
x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print("y =", y)
