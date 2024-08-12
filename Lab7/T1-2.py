# ------------------------------------------------------------
# imports
# ------------------------------------------------------------
import re

# ------------------------------------------------------------
# config
# ------------------------------------------------------------
# Define a dictionary of patterns
patterns = {}

# intents dictionary
keywords = {
    "greet": ["hello", "hi", "hey"],
    "goodbye": ["bye", "farewell"],
    "thankyou": ["thank", "thx"],
}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile("|".join(keys))

# ------------------------------------------------------------
# functions
# ------------------------------------------------------------
# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None

    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message
        if re.search(pattern,message):
            matched_intent = intent

    return matched_intent


# ------------------------------------------------------------
# main
# ------------------------------------------------------------
# print the discovered intent
print(match_intent("hello!"))
print(match_intent("bye byeee"))
print(match_intent("thanks very much!"))
print(match_intent("wow"))