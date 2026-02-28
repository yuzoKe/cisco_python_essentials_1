"""
2.1.13 LAB - Formatting the output

Scenario
We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments.
Feel free to modify any part of the code, but there is one condition - learn from your mistakes and draw your own conclusions.

Try to:
1. Minimize the number of print() function invocations by inserting the \n sequence into the strings;

2. Make the arrow twice as large (but keep the proportions)

3. Duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick:
"string" * 2 will produce "stringstring" (we'll tell you more about it soon)

4. Remove any of the quotes, and look carefully at Python's response;
pay attention to where Python sees an error - is this the place where the error really exists?

5. Do the same with some of the parentheses;

6. Change any of the print words into something else, differing only in case (e.g., Print) - what happens now?

7. Replace some of the quotes with apostrophes; watch what happens carefully.
"""

print("0. Original version:")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# ==========================
# Result for 1
# ==========================
print("1. With fewer 'print()' invocations:")
print("     *\n", "   * *\n", "  *   *\n", " *     *\n",
      "***   ***\n", "  *   *\n", "  *   *\n", "  *****")

# ==========================
# Result for 2
# ==========================
print("2. Bigger:")
print("       *\n", "    *   *\n", "   *     *\n", "  *       *\n", " *         *\n",
      "***       ***\n", "  *       *\n", "  *       *\n", "  *********")

# ==========================
# Result for 3: duplicate the arrows
# ==========================
print("3. Double:")
print("    *"+"         *")
print("   * *"+"       * *")
print("  *   *"+"     *   *")
print(" *     *"+"   *     *")
print("***   ***"+" ***   ***")
print("  *   *"+"     *   *")
print("  *   *"+"     *   *")
print("  *****"+"     *****")
# I tried using the "string" * 2, it didn't work.
# So I adjusted the number of spaces to make the second arrow simetrical.


# ==========================
# Result for 4: proposital error
# ==========================

# print("    *"+"         *")
# print("   * *"+"       * *")
# print("  *   *"+"     *   *")
# print(" *     *"+"   *     *")
# print("***   ***"+" ***   ***")
# print("  *   *"+"     *   *")
# print("  *   *"+"     *   *")
# print("  *****"+"     *****)

# the error points at the first ", but clearly its because its not closed.
# SyntaxError: unterminated string literal (detected at line 62)
# print("  *****"+"     *****)
#                 ^

# ==========================
# Result for 5: removing parentheses
# ==========================

# print"Hello"
# NameError: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# ==========================
# Result for 6: changing print to Print
# ==========================

# Print("Hello")
# NameError: name 'Print' is not defined

# ==========================
# Result for 7: replacing quotes with apostrophes
# ==========================
print('Hello')        # works fine
print("It's me")      # works fine
# print('It's me')    # SyntaxError: unterminated string literal
print('It\'s me')     # works fine

# My perspective:
# Single and double quotes are equivalent in Python, both define strings.
# Problems occur when the chosen quote character conflicts with the text inside.
# Example: 'It's me' fails, because the apostrophe in "It's" ends the string early.
# Solutions: use double quotes around it, or escape the apostrophe with \.
