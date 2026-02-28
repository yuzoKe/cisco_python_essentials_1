"""
3.2.9 LAB - Essentials of the while loop
Scenario
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. 
The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
Note: the height is measured by the number of fully completed layers – if the builders
don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
Test your code using the data we've provided.

TEST DATA
Sample Input: 6
Expected output1: The height of the pyramid: 3

Sample Input: 20
Expected output1: The height of the pyramid: 5

Sample Input: 1000
Expected output1: The height of the pyramid: 44

Sample Input: 2
Expected output1: The height of the pyramid: 1

Code Given:
blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

print("The height of the pyramid:", height)

"""

blocks = int(input("Enter the number of blocks: "))

height = blocks/2

print("The height of the pyramid:", height)
