redZone = 0
greenZone = 0
adjust = 0
lecturesRealized = 0
smallestLecture = 0
total = 0
conclude = 0

while (conclude != 2):

    value = int(input("Insira o valor em PCU: "))
    lecturesRealized +=1
    if value > 150:
        adjust = value + value*0.08
        total = total + adjust

        if adjust > 250:
            redZone +=1
#script pra brecar o codigo agora ao vivo se pegar duas vezes seguidas
            if redZone >= 2:
                print("----- SISTEMA TRAVADO ------") 
                break
        elif 180 < adjust:
            redZone = 0
        else:
            greenZone += 1
            redZone = 0

    else:
        adjust = value - value*0.04
        total = total + adjust

        if 120 > adjust:
            greenZone += 1
            redZone = 0
#script bolado pra salvar o menor valor lido 
    if smallestLecture == 0:
        smallestLecture = adjust
#o if coloca o primeiro valor lido como essa variavel nova, que vai ser comparada com o resto
    elif smallestLecture > adjust:
        smallestLecture = adjust
#se a variavel smallest for maior que o novo valor lido, o valor lido eh armazenado como o novo smallestLecture

#sistema pra concluir ou continuar inserindo dados
    print("----- Digite 1 para continuar a leitura -----") 
    print("----- Digite 2 para concluir a leitura -----")
    conclude = int(input(""))        

if conclude == 2:
    print("----- SISTEMA CONCLUIDO ------")

#script ja com print pra deixar o lucas de xerequinha calculando a media total das leituras realizadas
print(f"A media de todas as leituras realizadas ajustadas foi de {total/lecturesRealized:1.2f} UPCs")
print(f"A menor leitura ajustada foi de {smallestLecture} UPCs")
#script de aura pra calcular quantos % foi zona verde e ja printar direto
print(f"O percentual de leituras na zona verde realizadas foram de {(greenZone*100)/lecturesRealized:1.2f}%")







