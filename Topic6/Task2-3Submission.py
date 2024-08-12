import random

# Task 2-3 
questions = ["I dont' know", "You tell me"]
statement = ["Wow interesting!", "Can you tell me more?"]

def respond(message):
    # Check for a question mark
    if message.find("?") != -1:
        # Return a random question
        return print(random.choice(questions))
    # Return a random statement
    return print(random.choice(statement))


# Send messages ending in a question mark
respond("what's today's weather?")
respond("what's today's weather?")

# Send messages which don't end with a question mark
respond("I love building chatbots")
respond("I love building chatbots")

