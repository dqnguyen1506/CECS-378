#This program essentitally move up every letter in the given string
# by 3 places in the alphabet
s = """F elmb vlr afak'q qoxkpixqb fq yv exka, qexq'p texq zljmrqbop xob clo. Fc vlr afa fq yv 
exka, vlr pelria obal fq ybzrxpb alfkd fq fk yv exka fp fkbccfzfbkq xka qexq'p tev qefp 
qbuq fp pl ilkd. Xipl, qefp xppfdjbkq zxiip clo x pjxii mvqelk moldoxj. Lkb txv lc plisfkd 
qefp fp rpfkd pqofkd.jxhbqoxkp() xka tefib fq fp obzljjbkaba; fq fp klq kbzbppxofiv qeb 
lkiv lmqflk vlr exsb. Elmb vlr exa crk tlohfkd qefp lrq"""

alphabet = ["a","b","c", "d", "e","f","g","h","i","j","k","l","m",
            "n","o", "p", "q","r","s","t","u","v","w","x","y","z"]
new =""
#go through the indexes in the given string
for character in s:
    #check if the index is a letter in the alphabet
    #if it is move up 3 places
    if character.lower() in alphabet:
        index = alphabet.index(character.lower())
        #3 exceptiosn are x, y, and z letters
        #they are moved up and back to the beginning
        #of the alphabet
        if character.lower() == "x":
            character = "A"
        elif character.lower() =="y":
            character = "B"
        elif character.lower() =="z":
            character = "C"
        else:
            character = alphabet[index+3].upper()
            character = character.upper()
    #add the translated character to the new string
    new += character
#print it
print(new)
