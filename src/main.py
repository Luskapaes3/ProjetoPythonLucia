redZone = 0
greenZone = 0
adjust = 0
lecturesRealized = 0

while (redZone < 2):

    value = int(input("Insira o valor em PCU: "))
    lecturesRealized +=1

    if value > 150:
        adjust = value + value*0.08

        if adjust > 250:
            redZone +=1
        elif 180 < adjust:
            redZone = 0
        else:
            greenZone += 1
            redZone = 0

    else:
        adjust = value - value*0.04

        if 120 > adjust:
            greenZone += 1
            redZone = 0
print("Lucas da a bundinha dele")

