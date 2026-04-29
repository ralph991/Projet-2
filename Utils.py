def print_feedback(level, feedback):
    print(f"Score de sécurité : {level}")
    if feedback:
        print("Conseils :")
        for f in feedback:
            print(f"- {f}")