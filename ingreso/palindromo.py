#PALINDROMO

palabra = input("Palabra o frase: ").lower()
palabra_junta = palabra.replace(" ", "")
palabra_comparada = ""
comparador = 0

for letra in palabra_junta:
    palabra_comparada = palabra_comparada + palabra_junta[comparador - 1]
    comparador = comparador - 1

if palabra_comparada == palabra_junta:
    resultado = "es palindromo"
else:
    resultado = "no es palindromo"

print(f"'{palabra}' {resultado}") 
