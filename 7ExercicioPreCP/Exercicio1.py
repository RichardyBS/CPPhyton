"""Escreva um programa que pergunte a temperatura em celsius e converta para Kelvin. """

TempCelsius = int(input("Digite qual a Temperatura Celsius: "))
print(f"temperatura digitada foi de: {TempCelsius}°C")

Kelvin = TempCelsius + 273,15
print(f"A conversão da Temperatura de Celsius para Kelvin é de: {Kelvin}")