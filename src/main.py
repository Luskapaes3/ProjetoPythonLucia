Zona_Vermelha = 0
Zona_Verde = 0
Zona_Amarela = 0

while (Zona_Vermelha < 2):
    Valor = float(input("Insira o valor em PCU"))
    if Valor > 150:
        Ajuste = Valor + Valor*0.08
    else:
        Ajuste = Valor - Valor*0.04