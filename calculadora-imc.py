def imc(massa:float, altura:float):
    imc = massa / (altura ** 2)

    if imc < 18.5 and imc < 25:
        "Abaixo do Peso"
    