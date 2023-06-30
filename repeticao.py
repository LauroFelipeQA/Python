texto = "Lauro ASD easd egassdfsdf"
VOGAIS = "AEIOU"

for n in texto:
    if n.upper() in VOGAIS:
        print(n.upper(), end="-")
