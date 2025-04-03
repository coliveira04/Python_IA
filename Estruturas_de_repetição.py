# ESTRUTURAS DE REPETIÇÃO

# Comando for - usado quando se sabe o número exato de vezes que um bloco de código deve ser executado

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()

    #Função Range - usada para produzir uma sequência de números inteiros a partir de um início inclusivo até um fim exclusivo
    #Range é um intervalo numérico
        # recebe três argumentos: stop (obrigatório); start e step (opcionais)

numero = int(input("Insira um número inteiro: "))
for numero in range(0, 51, 5):
    print(numero, end=" ")

