from Vader.Vader.vaderSentiment import Vader

def main():
    print("A Global Communication Tone Index for Github's Open Source Repositories")
    choice = input("Press 1 to generate the Index using Vader: ")

    if choice == "1":
        Vader()

main()

