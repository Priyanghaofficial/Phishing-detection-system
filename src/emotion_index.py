def emotion_score(text: str):
    score = 0
    reasons = []
    t = text.lower()

    # Strong urgency
    if any(w in t for w in ["urgent", "immediately", "asap"]):
        score += 30
        reasons.append("Urgency language detected")

    # Explicit verification requests
    if any(w in t for w in ["verify", "confirm"]):
        score += 25
        reasons.append("Verification request detected")

    # Sensitive update requests (only when account-related)
    if "update" in t and any(w in t for w in ["account", "login", "password"]):
        score += 15
        reasons.append("Sensitive update request detected")

    # Click pressure
    if any(w in t for w in ["click", "click the link", "tap here"]):
        score += 20
        reasons.append("User asked to click a link")

    if score == 0:
        reasons.append("No emotional manipulation detected")

    return score, reasons
