import dict


def get_key(val):
    for key, value in dict.dictkey.items():
        if val == value:
            return key


def decrypt():
    text = input("Please enter some text to be decrypted: ")
    new_txt = list(text)
    for i in range(0, len(text)):
        if new_txt[i] in dict.dictkey.values():
            new_txt[i] = get_key(new_txt[i])
    print("Text after decryption: "+''.join(new_txt))
