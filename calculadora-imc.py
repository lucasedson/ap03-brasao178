def imc(massa:float, altura:float):
    imc = float(massa) / (float(altura) ** 2)

    if imc < 18.5:
        return "Abaixo do Peso"
    elif imc < 25:
        return "Peso Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
       return "Obeso"
    
if __name__ == "__main__":
    while True:
        print("Calculadora de IMC!")
        peso = input("Digite o peso: ")
        altura = input("Digite a altura: ")

        print(imc(peso, altura))
        input("Aperte enter para continuar ou ctrl+c para sair")