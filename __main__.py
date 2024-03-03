from Vader.Vader.vaderSentiment import Vader

def main():
    print("ANÁLISE DE SENTIMENTOS EM REPÓSITÓRIO MINERADO DO GITHUB")
    escolha = input("DIGITE 1 PARA COMEÇAR: ")

    if escolha == "1":
        Vader()

main()

