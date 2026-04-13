greenZone = 0
greenZone = 0
adjust = 0
lecturesRealized = 0

while (greenZone < 2):
    value = float(input("Insira o valor em PCU: "))
    lecturesRealized +=1
    if value > 150:
        adjust = value + value*0.08
        if adjust > 250:
            greenZone +=1
        elif 120 < adjust < 180:
            greenZone += 1
            greenZone -= 1
        elif 180 < adjust < 250:
            greenZone -= 1
    else:
        adjust = value - value*0.04
print("Lucas da a bundinha dele")

