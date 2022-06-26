
# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
print("Space removed: ", iban)

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    print("Character swapped: ", iban)
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            print(ch, "character is : ", ord(ch))
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    print("IBAN in integer: ", iban)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

#GB72 HBZU 7006 7212 1253 00
#FR76 30003 03620 00020216907 50
#DE02100100100157517108