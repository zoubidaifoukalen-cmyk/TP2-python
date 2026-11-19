# texte.py : analyse de texte utilisateur

original = input("Entre un mot ou une phrase : ")

print("Longueur       :", len(original))
print("Majuscules     :", original.upper())
print("Minuscules     :", original.lower())
print("Inversé        :", original[::-1])

# Bonus : palindrome (on ignore la casse et les espaces)
nettoye = original.lower().replace(" ", "")
if nettoye == nettoye[::-1]:
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")

# Les chaînes sont immuables : upper() crée une nouvelle chaîne,
# l'original reste intact pour comparaison.
print("Original intact :", original)
