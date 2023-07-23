"""
The string lower() is an in-built method in Python language. 
It converts all uppercase letters in a string into lowercase 
and then returns the string. Whereas casefold() method is an 
advanced version of lower() method, it converts the uppercase 
letter to lowercase including some special characters which are 
not specified in the ASCII table for example ‘ß’ which is a German 
letter and its lowercase letter is ‘ss’.
"""

string1 = "ß"

print("Original string")
print(string1)

print("Convert using casefold()")

string2 = string1.casefold()

print(string2)

print("Convert using lower()")

string3 = string1.lower()

print(string3)
