"""
3.1.6 LAB - Variables - Questions and answers

Scenario
Using one of the comparison operators in Python, write a simple two-line program that takes 
the parameter n as input, which is an integer, and prints False if n is less than 100,
and True if n is greater than or equal to 100.

Don't create any if blocks (we're going to talk about them very soon).
Test your code using the data we've provided for you.

TEST DATA
Sample Input: 55
Expected output1: False

Sample Input: 99
Expected output2: False

Sample Input: 100
Expected output3: True

Sample Input: 101
Expected output3: True

Sample Input: -5
Expected output3: False

Sample Input: +123
Expected output3: True
"""
n = int(input("Enter a number: "))
print(n >= 100)
