from generator import generate_password
from checker import check_password_strength
from utils import print_feedback

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Générer un mot de passe")
        print("2. Tester un mot de passe")
        print("3. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            length = int(input("Longueur du mot de passe (8-20) : "))
            pwd = generate_password(length)
            print(f"Mot de passe généré : {pwd}")

        elif choice == "2":
            pwd = input("Entrez le mot de passe à tester : ")
            level, feedback = check_password_strength(pwd)
            print_feedback(level, feedback)

        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu()