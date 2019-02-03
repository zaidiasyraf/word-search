import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesnt exist. Please double check it"
        else:
            return "We didnt understand your query"
    else:
        return "The word doesn't exist. Please double check!"

word = input("Enter the word : ")

output = meaning(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
