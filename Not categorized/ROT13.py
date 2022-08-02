#use dictionary
def rot13(msg):
    encored_msg = ""
    code_table = {
        "a" : "n",
        "b" : "o",
        "c" : "p",
        "d" : "q",
        "e" : "r",
        "f" : "s",
        "g" : "t",
        "h" : "u",
        "i" : "v",
        "j" : "w",
        "k" : "x",
        "l" : "y",
        "m" : "z",
        "n" : "a",
        "o" : "b",
        "p" : "c",
        "q" : "d",
        "r" : "e",
        "s" : "f",
        "t" : "g",
        "u" : "h",
        "v" : "i",
        "w" : "j",
        "x" : "j",
        "y" : "k",
        "z" : "l"
    }
    for letter in msg:
        if letter.lower() in code_table.keys():
            #check if upper, change the letter add to result string
            #else, keep
            if letter.isupper():
                encored_msg += code_table.get(letter.lower()).upper()
            else:
                encored_msg += code_table.get(letter)
        #if not a letter, stay unchange
        else:
            encored_msg += letter

    return encored_msg

print(rot13("abcDd!"))

#the function above is having no uppercase check