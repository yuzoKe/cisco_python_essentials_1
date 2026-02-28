"""
2.4.7 LAB - Variables

Scenario
Here is a short story:

Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples.
They were all very happy and lived for a long time. End of story.

Your task is to:

- create the variables: john, mary, and adam;
- assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
- having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
- now create a new variable named total_apples equal to the addition of the three previous variables.
- print the value stored in total_apples to the console;
- experiment with your code: create new variables, assign different values to them, and perform various arithmetic
operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on 
one line, e.g., "Total number of apples:" and total_apples.

"""

john = int(3)
mary = int(5)
adam = int(6)

print(john, mary, adam, sep=",")

total_apples = john + mary + adam
print(total_apples)

eduardo = int(10)
carolina = int(3)
pedro = int(2)

print("At the start, Carolina had 3 apples, Pedro 2 apples and Eduardo 10.\n"
      "Carolina took one apple from Pedro.\n""Eduardo seeing that Pedro only had one left, gave 3 apples to him.\n")
