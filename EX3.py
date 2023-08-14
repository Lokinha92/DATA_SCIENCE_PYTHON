def ValorTransporte(peso):
    if peso <= 10:
        print("O VALOR É R$ 50,00")
    elif peso <= 20 :
        print("O VALOR É R$ 80,00")
    else:
        print("TRANSPORTE NÃO ACEITO")

    return

valor = int(input("INFORME O PESO: "))

ValorTransporte(valor)
