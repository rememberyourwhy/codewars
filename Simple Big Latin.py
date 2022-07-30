"""

 what to do
 think
 ok, always work with a word
 seperate each word and work with each

 follow what they demand us to do

 just read through the word and add requirements to it later

"""
import string

def change(word):
    alb = string.ascii_lowercase
    for i in word:
        if i.lower() not in alb + " ":
            return word
    word = word.replace(" ", "")
    return word[1:] + word[0] + "ay"

def main(text):
    j = 0
    new_string = ""
    word = ""
    for i in range(len(text)):
        if (text[i] == " ") or (i == len(text) - 1):
            word = text[j : i + 1]
            new_string += change(word)
            if i != len(text) - 1:
                j = i + 1
                new_string += " "
    return new_string

print(main("piggy so what !"))
