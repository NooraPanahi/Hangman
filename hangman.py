import random
from pyfiglet import Figlet
def wordFrame(word):
    chars = []
    for i in range(length):
        if i in found:
            chars.append(found[i])
        else:
            chars.append("-")
    print(chars)

def findChar(c):
    result = False
    for i in range(length):
        if word[i] == c:
            found[i] = c
            result = True
    return result

def message(txt):
    figlet.setFont(font="slant")
    print(figlet.renderText(txt))
     

def main(chance):
    while chance>0 and len(found.keys()) != length :
        wordFrame(word)
        c = input("enter a letter: ")
        finded = findChar(c)
        if not finded :
            chance -= 1
            print(f"you have {chance} more chances!")
    if chance >0 :
        wordFrame(word)
        message("you won!")
    else:
        message("game over!")

figlet = Figlet()
words = ["sky","flower","door","milk","ice cream","coffee","chocolate", "water","mobile","tv","table","chair",]
found = {}
word = random.choice(words)
length = len(word)
main(length)