# join - joins a list of strings with another string as a separator.

# replace - replaces one substring in a string with another.

# startswith and endswith - determine if there is a substring at the start and end of a string, respectively.

# lower and upper – changes the case of a string

# split -the opposite of join, turns a string with a certain separator into a list.
# Here they are in action:


print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"
