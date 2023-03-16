# CARRON Thibault

# Question 1

def codage(message, d):
    chaine=""
    if (d >=0 & d<=25):
        for i in range (0, len(message)):
            if(ord(message[i]) + d > 122):
                ascii=chr(ord(message[i]) + 26 - d)
                chaine = chaine + ascii
            else:
                ascii=chr(ord(message[i]) + d % 26)
                chaine=chaine+ascii
        print(chaine);
    else:
        return "La clé de chiffrement est trop grande"

# Traduction de chaques lettre en caractere ascii, j'additionne le d
codage("tew wm jegmpi uyi gipe pi gsheki hi giwev", 4)

# Question 2
def freq_lettres(messagecode):
    chiffre=""
    for i in range (0, len(messagecode)):
        chiffre=ord(messagecode[i]) - 97
        return chiffre

## print(freq_lettres("bbbb"))

def calcul_auto_decal(messagecode):
    base="e"
    for i in range(0, len(messagecode)):
        return