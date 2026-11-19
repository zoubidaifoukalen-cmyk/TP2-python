# calc.py : mini-calculatrice

print("=== Mini-calculatrice ===")

try:
    a = float(input("Premier nombre : "))
    b = float(input("Deuxième nombre : "))
except ValueError:
    print("Saisie invalide, merci d'entrer des nombres.")
    raise SystemExit(1)

print("Opérations : +  -  *  /")
op = input("Choisis une opération : ").strip()

if op == "+":
    resultat = a + b
elif op == "-":
    resultat = a - b
elif op == "*":
    resultat = a * b
elif op == "/":
    if b == 0:
        print("Erreur : division par zéro impossible.")
        raise SystemExit(1)
    resultat = a / b
else:
    print("Erreur : opérateur invalide.")
    raise SystemExit(1)

print(f"{a} {op} {b} = {resultat}")
