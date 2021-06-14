import dict


def encrypt():
    text = input("Please enter some text to be encrypted: ")
    new_txt = list(text)
    for i in range(0, len(text)):
        if new_txt[i] in dict.dictkey.keys():
            new_txt[i] = dict.dictkey[text[i]]
    print("Text after encryption: "+''.join(new_txt))
