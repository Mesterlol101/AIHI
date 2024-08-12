from time import sleep

def response(message):
    return "I can hear you! You said: {}".format(message)

def send_message(message):
    # Call response to get response
    print("User: {}".format(message))
    sleep(1)
    print("Bot: {}".format(response(message)))

send_message("E")