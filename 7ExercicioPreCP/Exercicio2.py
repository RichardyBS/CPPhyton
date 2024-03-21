"""Escreva um programa que solicite a altura e peso e calcule o IMC. """

Altura = float(input("Digite Sua Altura em Metros: "))
print(f"Altura é de {Altura}")

Peso = float(input("Digite seu Peso em kg: "))
print(f"Peso é de {Peso}")

IMC = Peso / (Altura * Altura)
print(f"Seu Índice de Massa Corporal é de: {IMC: ,.2f}")