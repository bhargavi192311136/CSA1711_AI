# Python program to remove punctuations from a given string

import string

# Input string from user
text = input("Enter a string: ")

# Create a translation table that removes punctuation
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation
no_punct = text.translate(translator)

print("\nString without punctuation:")
print(no_punct)
