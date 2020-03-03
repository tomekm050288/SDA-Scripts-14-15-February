# def CaesarCipher(word):
#     password = ""
#     for i in word:
#         if i >= "a" and i <= "w":
#             # funkcja ord() zamienia literę na odpowiadającą cyfra według ASCII
#             # funkcja chr() zamienia cyfrę na odpowiednią literę w ASCII
#             password += chr(ord(i) + 3).upper()
#         elif i == 'y':
#             password += 'A'
#         elif i =='z':
#             password += 'B'
#         else:
#             password += i
#     return password
#
# word_to_code = input("Enter the word from the encoding of the Caesar cipher: ")
# print(CaesarCipher(word_to_code))

#####################################################




# def CaesarCipher(word,shift):
#     password = ""
#     for i in word:
#         if i.isalpha():
#             # funkcja ord() zamienia literę na odpowiadającą cyfra według ASCII
#             # funkcja chr() zamienia cyfrę na odpowiednią literę w ASCII
#             password += chr(ord(i) + shift).upper()
#         elif i == 'y':
#             password += 'A'
#         elif i =='z':
#             password += 'B'
#         else:
#             password += i
#     return password
#
# word_to_code = input("Enter the word from the encoding of the Caesar cipher: ")
# shift = int(input("Enter shift: "))
# print(CaesarCipher(word_to_code,shift))



def caesar(plainText, shift):
    cipherText = ""
    for ch in plainText:
        #sprawdzamy czy ch jest itera alfabetu
        if ch.isalpha():
            # jeśli tak to do zmiennej stayinAlphabet dodajemy ord(ch) i dodajemy shift
            stayInAlphabet = ord(ch) + shift
            # sprawdzamy czy ord(ch)+shift wykracza poza ord(z)
            if stayInAlphabet > ord('z'):
                #jesli tak to zmiejszamy o 26 znaków - wracamy do pocżatku alfabetu
                stayInAlphabet -= 26
        # konwertujemy na stringa
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    print("Your ciphertext is: ", cipherText)
    return cipherText

print(caesar("tuwxyz",3))