def adjust_value(value):
    if value > 150:
        return value + value*0.08
    else:
        return value - value*0.04



def handle_consecutive_red(value,con):

    if value > 250:
        return con + 1
    else:
        return 0
    
def print_estabillity(value):
    if 180 > value > 120:
        print(f"Valor apos dilatacao: {value} -> Zona verde")
    elif value > 250:
        print(f"Valor apos dilatacao: {value} -> Zona vermelha")
    else:
        print(f"Valor apos dilatacao: {value} -> Zona amarela")



def end_system():
    
    print("Sistema encerrado!")


def main_fuction():

    
    consecutive_red = 0
    value = float(input("Insira o valor da pressao em PCU, insira um valor negativo para encerrar o programa: "))
    while(value >= 0):

        value = adjust_value(value)
        print_estabillity(value)
        consecutive_red = handle_consecutive_red(value,consecutive_red)

        if consecutive_red < 2:
            value = float(input("Insira o valor da pressao em PCU, insira um valor negativo para encerrar o programa: "))
        else:
            break
    end_system()
            


main_fuction()


