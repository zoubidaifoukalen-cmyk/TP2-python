# lab2_conversion_input.py
# input() renvoie toujours une chaîne : il faut convertir

age_str = input("Quel âge as-tu ? ")
print("Tu as saisi :", age_str, "→", type(age_str))

# Version fiabilisée avec try/except
try:
    age = int(age_str)
    print("Après conversion :", age, "→", type(age))
    print(f"Dans 5 ans tu auras {age + 5} ans.")
except ValueError:
    print("Saisie invalide, merci d'entrer un entier.")
