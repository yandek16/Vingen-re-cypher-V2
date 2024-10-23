alphabet = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
    'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
    ' ': 26, 
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
    'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
    'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 
    '0': 27, '1': 28, '2': 29, '3': 30, '4': 31, '5': 32, 
    '6': 33, '7': 34, '8': 35, '9': 36
}


inverse_alphabet = {v: k for k, v in alphabet.items()}


message_chiffre = input("Entrez un message chiffré: ")
lettresmess = list(message_chiffre)
print(lettresmess)

Key = input("Entrez la clé de déchiffrage: ")
lettreskey = list(Key)
print(lettreskey)


message_dechiffre = []

for i in range(len(lettresmess)):
    lettremess = lettresmess[i]
    
    if lettremess in alphabet:
        valeur_message = alphabet[lettremess]
        
        lettre_clef = lettreskey[i % len(lettreskey)]
        valeur_clef = alphabet[lettre_clef]
        
        
        valeur_dechiffree = (valeur_message - valeur_clef) % 27
        lettre_dechiffree = inverse_alphabet[valeur_dechiffree]
        
        message_dechiffre.append(lettre_dechiffree)
    else:
        message_dechiffre.append(lettremess)

message_dechiffre_final = ''.join(message_dechiffre)
print("Message déchiffré:", message_dechiffre_final)
