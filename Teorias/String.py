curso = "Python"

print(curso.center(10, "I"))
print(".".join(curso))
print(curso.lower())
print(curso.upper())
print(curso.split())

curso = "     Python    "


print(curso.lstrip())
print(curso.rstrip())

# o % não é usado mais para concatenar: "Oi %s, sua idade é %d, salario %f" %(aluno, idade, salario )
# format para concatenar: "Oi {}, sua idade é {}, salario {}" .format(aluno, idade, salario )
# f-string :  f"Oi {aluno}, sua idade é {idade}, salario {salario}"

PI = 3.14159

print(f"O valor de pi é {PI:.2f}")