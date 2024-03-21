"""Escreva um programa que irá solicitar a quantidade de pessoas de uma residência e a quantidade de minutos em média que as pessoas se demoram no banho. Sabendo que o chuveiro é de 2400 W, o programa deverá calcular e exibir o consumo da energia elétrica, em quilowatt-hora no final do mês (30 dias) e o valor em reais gasto, dado que o valor do KWh é de R$ 0,40. """

QunatidadePessoas = int(input("Digite a quandide de pessoas que moram na Residencia: "))
print(f"Valor de Residentes foi de: {QunatidadePessoas}")

MediaBanho = int(input("Digite a Media de Banho dos Residentes: "))
print(f"Media Digitada e de: {MediaBanho}")

Chuveiro = (2400 * MediaBanho) / 1000
print(f"o gasto no medio de quilowatt-hora e de: {Chuveiro}")

gastoPorPessoa = Chuveiro / 5
print(f"tendo uma media de {gastoPorPessoa}Watts por pessoa")

GastoWattsMes = Chuveiro * 30
GastoMensal = GastoWattsMes * 0.40

print(f"Tendo um Gasto Por mes de {GastoWattsMes}Kwh")
print(f"E o Valor a ser Pago por Kmw no mes e de: {GastoMensal}")