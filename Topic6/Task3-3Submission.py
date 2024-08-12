import random
import re
from time import sleep

# Define match_rule()
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
    return response, phrase

def replace_pronouns(message):
    message = message.lower()

    if "me" in message:
        message = re.sub("me", "you", message)
        return message

    if "my" in message:
        message = re.sub("my", "your", message)
        return message

    if "your" in message:
        message = re.sub("your", "my", message)
        return message

    if "you" in message:
        message = re.sub("you", "me", message)
        return message

    return message

def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase) 
        # Include the phrase in the response
        response = response.format(phrase)
    return response



def send_message(message):
    # Print user_message
    print("User: {}".format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print bot's response.
    print("Bot: {}".format(response))

# Send Messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")