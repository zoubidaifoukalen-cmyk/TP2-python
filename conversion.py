# conversion.py : conversion de températures

print("=== Conversion de températures ===")
print("1. Celsius → Fahrenheit et Kelvin")
print("2. Fahrenheit → Celsius et Kelvin")
choix = input("Ton choix (1 ou 2) : ").strip()

try:
    if choix == "1":
        c = float(input("Température en °C : "))
        f = c * 9 / 5 + 32
        k = c + 273.15
    elif choix == "2":
        f = float(input("Température en °F : "))
        c = (f - 32) * 5 / 9
        k = c + 273.15
    else:
        print("Choix invalide.")
        raise SystemExit(1)
except ValueError:
    print("Saisie invalide, merci d'entrer un nombre.")
    raise SystemExit(1)

print(f"{c:.2f}°C = {f:.2f}°F = {k:.2f}K")
