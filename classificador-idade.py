def classificador_idade(idade):
    idade = int(idade)
    if idade >= 0 and idade <= 12:
        return "Criança"
    elif idade > 12 and idade <=17:
        return "Adolescente"
    elif idade > 17 and idade <=59:
        return "Adulto"
    elif idade > 59:
        return "Idoso"

if __name__ == "__main__":
    idade = input("Digite a idade: ")
    print(classificador_idade(idade))