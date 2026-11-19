# lab2_variables.py
# Types de base, inspection avec type(), réaffectation et mutabilité

# --- 1. Les quatre types de base ---
entier = 42              # int
flottant = 3.14          # float
texte = "Python"         # str
vrai_ou_faux = True      # bool

print(entier, "→", type(entier))
print(flottant, "→", type(flottant))
print(texte, "→", type(texte))
print(vrai_ou_faux, "→", type(vrai_ou_faux))

# bool hérite de int : True vaut 1 et False vaut 0
print("True + True =", True + True)

# --- 2. Réaffectation d'une variable ---
nombre = 10              # nombre référence un int
print("\nnombre =", nombre, "| id =", id(nombre))

nombre = 10 + 5          # le nom pointe désormais vers un autre int (15)
print("nombre =", nombre, "| id =", id(nombre))

# Opérateur d'affectation augmentée
total = 0
total += 5               # équivaut à total = total + 5
print("total =", total)

# --- 3. Objet mutable : la référence ne change pas ---
liste = [1, 2, 3]
print("\nliste =", liste, "| id =", id(liste))
liste.append(4)          # l'objet est modifié, pas la référence
print("liste =", liste, "| id =", id(liste))

# --- 4. Conversions et vérification de type ---
print()
print(float("7.5"), type(float("7.5")))
print(bool("False"), "(toute chaîne non vide vaut True)")
print(str(1234), type(str(1234)))
print(int(3.99), "(int tronque vers 0)")
print(round(3.99), "(round arrondit)")

print(isinstance(entier, int))      # True
print(isinstance(texte, int))       # False

# --- 5. Annotation de type (PEP 484) ---
age: int = 25
print("\nage =", age)
