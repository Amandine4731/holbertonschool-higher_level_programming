#!/usr/bin/python3
def uppercase(str):

    # parcours toute la string
    for i in range(len(str)):
        asci = ord(str[i])

        # verifie si il s'agit d'une lower
        if (asci >= 97) and (asci <= 123):
            # converti en upper
            asci = asci - 32

        # imprime tous les caractères, les upper, et les lower convertis
        print("{}".format(chr(asci)), end="")
    print("")
