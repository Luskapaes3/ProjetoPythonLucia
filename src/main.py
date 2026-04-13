redZone = 0
greenZone = 0
yellowZone = 0

while (yellowZone < 2):
    value = float(input("Insira o valor em PCU"))
    if value > 150:
        adjust = Valor + Valor*0.08
    else:
        adjust = Valor - Valor*0.04