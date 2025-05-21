def conversor_temperatura(u_origem:str, u_destino:str, valor):    
    u_origem = u_origem.upper()
    u_destino = u_destino.upper()

    if u_origem == "C" and u_destino == "F":
        return (valor * 9/5) + 32
    elif u_origem == "F" and u_destino == "C":
        return (valor - 32) * 5/9
    elif u_origem == "C" and u_destino == "K":
        return valor + 273.15
    elif u_origem == "K" and u_destino == "C":
        return valor - 273.15
    elif u_origem == "F" and u_destino == "K":
        return ((valor - 32) * 5/9) + 273.15
    elif u_origem == "K" and u_destino == "F":
        return  ((valor - 273.15) * 9/5) + 32
    else:
        return '''
        Digite uma unidade válida!!!
        Unidade: C = Celsius, F = Fahrenheint, K = Kelvin '''


    
if __name__ == "__main__":
    # print(conversor_temperatura("C", "F", 45))     -> 113
    # print(conversor_temperatura("F", "C", 113))  -> 45
    
    # print(conversor_temperatura("C", "K", 45))  -> 318.15  
    # print(conversor_temperatura("K", "C", 318.15)) -> 45
    
    # print(conversor_temperatura("K", "F", 318.15)) -> 113
    
    # print(conversor_temperatura("F", "K", 113)) -> 318.15
    
    while True:
        print("Conversor de Temperatura")

        u_origem = input("Insira a unidade de origem: ")
        u_destino = input("Insira a unidade no qual vc queira converter: ")
        temperatura = float(input("Digite a temperatura: "))

        print(conversor_temperatura(u_origem, u_destino, temperatura))

        cmd = input("Aperte enter para continuar ou q para sair: ")
        
        if cmd == 'q':
            exit()