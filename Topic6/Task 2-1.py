# task 2-1
# Define variables
name = "Greg"
weather = "cloudy"


# Define a dictionary with the questions and answers
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "I am sorry, please repeat"
}


# Define the respond function
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message

print(respond("what's today's weather?"))