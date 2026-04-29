import string
def check_password_strength(password):
    score = 0
    feedback = []
    # Longueur
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Mot de passe trop court.")
    # Diversité des caractères
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    # Motifs faibles
    weak_patterns = ["123", "password", "abc", "qwerty"]
    if any(p in password.lower() for p in weak_patterns):
        feedback.append("Motif faible détecté.")
        score -= 2
    # Résultat
    if score <= 2:
        level = "Faible"
    elif score <= 4:
        level = "Moyen"
    else:
        level = "Fort"

    return level, feedback