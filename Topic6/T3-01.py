# ------------------------------------------------------------
# imports
# ------------------------------------------------------------
import random
import re

# ------------------------------------------------------------
# config
# ------------------------------------------------------------
rules = {
    "do you think (.*)": [
        'yes, I think so', 'well, I do think {0}', 'yup, why not'
    ],
    "do you remember (.*)": [
        'yes, I remember {0}', 'I still remember {0}', 'yes, you remind me of that'
    ],
    "I want (.*)": [
        'I know you want {0}', 'yes, no problem'
    ]
}


# ------------------------------------------------------------
# functions
# ------------------------------------------------------------
# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None

    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)

            if '{0}' in response:
                phrase = match.group(1)

            # it's good to break here, otherwise it will continue to match other rules
            break

    # Return the response and phrase
    return response.format(phrase)


# ------------------------------------------------------------
# main
# ------------------------------------------------------------
print("-------- start ---------")

# Test match_rule
print(match_rule(rules, "do you remember your last birthday"))
print(match_rule(rules, "I want to eat an apple"))

print("-------- end ---------")