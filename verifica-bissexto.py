def ver_bissexto(ano):
    if ano % 4 == 0 or ano % 100 == 0 and ano % 400 != 0:
        return f"O ano {ano} é bissexto"
    else:
        return f"O ano {ano} não é bissexto"
    
if __name__ == "__main__":
    ano = int(input("Digite o ano: "))
    print(ver_bissexto(ano))

    # # TESTE SE O ANO É BISSEXTO DE 2000 a 2023: 
    # for ano in range(2000, 2030):
    #     print(ver_bissexto(ano))