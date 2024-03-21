"""Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km/h acima de 80 km/h."""

VelCarro = float(input("Qual a velocidade do seu carro: "))
print(f"A velocidade do carro e de: {VelCarro}")

Multa = 80

VerfMulta = 80 <= VelCarro
print(f"Voce tomou multa?: {VerfMulta}")

PagaMulta = (VelCarro % 80) * 5 
print(f"Valor da Multa e de: R${PagaMulta}")