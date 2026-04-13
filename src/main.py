zona_vermelha = 0
zona_verde = 0
ajuste = 0
leituras_realizadas = 0

while (zona_vermelha < 2):
    valor = float(input("Insira o valor em PCU"))
    leituras_realizadas +=1
    if valor > 150:
        ajuste = valor + valor*0.08
        if ajuste > 250:
            zona_vermelha +=1
        elif 120 < ajuste < 180:
            zona_verde += 1
            zona_vermelha -= 1
        elif 180 < ajuste < 250:
            zona_vermelha -= 1

    else:
        ajuste = valor - valor*0.04
print("Lucas da a bundinha dele")

