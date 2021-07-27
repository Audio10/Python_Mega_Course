import json
# To get the close matches with a word
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    matches = get_close_matches(word, data.keys())
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(matches) > 0:
        response = input(f"Did you mean {matches[0]} instead? Enter Y if yes, or N if no:")
        response = response.upper()
        if response == "Y":
            return data[matches[0]]
        elif response == "N":
            return "The word doesn't exist. PLease double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. PLease double check it."


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)