# ------------------------------------------------------------
# imports
# ------------------------------------------------------------
import re

# ------------------------------------------------------------
# functions
# ------------------------------------------------------------
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


# ------------------------------------------------------------
# main
# ------------------------------------------------------------
print("-------- start ---------")

print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))

print("-------- end ---------")