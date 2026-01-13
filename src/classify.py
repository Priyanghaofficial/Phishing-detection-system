def classify(text: str):
    text = text.lower()

    phishing_words = [
        "verify", "urgent", "click",
        "login", "update", "password"
    ]

    count = sum(word in text for word in phishing_words)

    score = min(count * 15, 60)

    label = "Phishing" if score >= 30 else "Legitimate"
    return label, score
