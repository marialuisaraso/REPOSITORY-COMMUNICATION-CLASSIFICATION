from Vader.Vader.vaderSentiment import Vader

def main():
    print("A Global Communication Tone Index for Github's Open Source Repositories")
    escolha = input("Press 1 to generate the Index: ")

    if escolha == "1":
        Vader()

main()

