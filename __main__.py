from Vader.Vader.vaderSentiment import Vader

def main():
    print("ANÁLISE DE SENTIMENTOS EM REPÓSITÓRIO MINERADO DO GITHUB")
    escolha = input("DIGITE 1 PARA DISPARAR A ANÁLISE DE SENTIMENTOS: ")

    if escolha == "1":
        Vader()

main()

