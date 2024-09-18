message = input(">>> ")

emoji_mapping = {
    ":)": "😊",
    ":D": "😁",
    ":|": "😐",
    ":o": "😮",
    ":p": "😋",
    ":v": "😦",
    ">-<": "😣"   
}

words = message.split(" ")

output = ""
for w in words:
    output = output + emoji_mapping.get(w, w) + " "
   
   
print(f"\n {output}")
    