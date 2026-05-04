def adjust_value(value):
    if value > 150:
        return value + value*0.08
    else:
        return value - value*0.04

def update_consecutive_red(value,con):
    if value > 250:
        return con + 1
    else:
        return 0
    
def get_stabillity_zone(value):
    if 180 > value > 120:
        return "Zona verde"
    elif value > 250:
        return "Zona vermelha"
    else:
        return "Zona amarela"


def end_system():
    
    print(f"\nSistema encerrado!")









def main_fuction():

    
    consecutive_red = 0
    value = float(input(f"\n Insira o valor da pressao em PCU, insira um valor negativo para encerrar o programa: "))
    while(value >= 0):

        value = adjust_value(value)
        print(f"\nValor  convertido: {value}")

        print(f"Faz parte da --> {get_stabillity_zone(value)}")

        consecutive_red = update_consecutive_red(value,consecutive_red)

        if consecutive_red < 2:
            value = float(input(f"\nInsira o valor da pressao em PCU, insira um valor negativo para encerrar o programa: "))
        else:
            break
    end_system()
            
main_fuction()
