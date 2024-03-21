"""Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos	 exercícios (ME) que fazem parte da avaliação. Calcular a média de aproveitamento (MA), usando a fórmula: 

MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7 """

RM = input("Digite o numero de RM")

Nota1 = float(input("Digite Sua Nota Banco de Dados"))
print(f"A nota digitada foi de: {Nota1}")

Nota2 = float(input("Digite Sua Nota FrontEnd"))
print(f"A nota digitada foi de: {Nota2}")

Nota3 = float(input("Digite Sua Nota Python"))
print(f"A nota digitada foi de: {Nota3}")

ME = float(input("Digite a Media dos Exercicios: "))

MA = (Nota1 + Nota2 * 2 + Nota3 * 3 + ME) / 7

print(f"A média de aproveitamento do aluno, {RM}, é:, {MA}")