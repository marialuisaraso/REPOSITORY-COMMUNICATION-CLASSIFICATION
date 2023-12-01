from Vader.Vader.vaderSentiment import Vader

def main():
    print("MENU DE FERRAMENTAS ANÁLISE DE SENTIMENTOS PARA OS DADOS EXTRAÍDOS:")
    print("1- VADER")
    print("2- SENTISTRENGTH")

    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        Vader()
    if escolha == "2":
        print("Opção 2")

main()

