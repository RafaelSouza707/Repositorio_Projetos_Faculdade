while True:
    resposta_User = int(input("""
                          Escolha uma opcao:
                          Sem peso - [1]
                          Com peso - [2]
                          """))
    print()
    if resposta_User == 1:
        print("Digite suas notas em uma única linha com espaço entre cada nota: ", end="")
        pn, sn, tn = list(map(float,input().split()))
        media = (pn+sn+tn)/3
        print("Sua note média foi de: {:.2f}".format(media))
        if media < 70:
            print("Sorry, c foi de arrasta pra cima. :/")
        else:
            print("Parabéns, vc passou de fase! :)")
    if resposta_User == 2:
        print("Digite os pesos em sequencia de cada nota: ", end="")
        peso1, peso2, peso3 = list(map(int,input().split()))
        print("Digite suas notas em uma única linha com espaço entre cada nota: ", end="")
        pn, sn, tn = list(map(float,input().split()))
        media = (pn*peso1+sn*peso2+tn*peso3)/(peso1+peso2+peso3)
        print("Sua note média foi de: {:.2f}".format(media))
        if media < 70:
            print("Sorry, c foi de arrasta pra cima. :/")
        else:
            print("Parabéns, vc passou de fase! :)")
