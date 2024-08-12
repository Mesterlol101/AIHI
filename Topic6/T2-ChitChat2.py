# ------------------------------------------------------------
# imports
# ------------------------------------------------------------
import random

# ------------------------------------------------------------
# config
# ------------------------------------------------------------
name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
    "what's your name?": [
        "my name is {0}".format(name),
        "they call me {0}".format(name),
        "I go by {0}".format(name)
    ],
    "what's today's weather?": [
        "the weather is {0}".format(weather),
        "it's {0} today".format(weather)
    ],
    "default": [
        "default message"
    ]
}

# ------------------------------------------------------------
# functions
# ------------------------------------------------------------


def respond(message):
    # check if the message is in the responses array
    if message in responses:
        # return a random matching message
        bot_message = random.choice(responses[message])
    else:
        # return the default message
        bot_message = random.choice(responses["default"])

    return bot_message


# ------------------------------------------------------------
# main
# ------------------------------------------------------------
print("-------- start ---------")

# print(respond("what's today's weather?"))
print(respond("what's your name?"))
# print(respond("who are you?"))


print("-------- end ---------")