# predict.py
import re

from url_features_extractor import extract_url_features
from homograph_vision import detect_homograph

PHISHING_WORDS = ["verify", "urgent", "click", "login", "update"]

def classify(data: str, input_type: str = "text"):
    """
    input_type = "url" or "text" (email/plain text).
    Returns (label, confidence_percent).
    """

    text = data.lower()
    phishing_count = sum(word in text for word in PHISHING_WORDS)

    # ---------- URL MODE ----------
    if input_type == "url":
        features, url_score = extract_url_features(data)
        homo = detect_homograph(data)

        # base score from rules (0–100)
        score = url_score

        # keyword hit in URL adds some extra
        if phishing_count > 0:
            score += 10

        # homograph boost
        if homo:
            score += 25

        score = min(score, 100)

        if score >= 70:
            return "Phishing", score
        elif score >= 40:
            return "Suspicious", score
        else:
            return "Legitimate", score

    # ---------- EMAIL / TEXT MODE ----------
    else:
        if phishing_count >= 2:
            return "Phishing", 90
        elif phishing_count == 1:
            return "Suspicious", 70
        else:
            return "Legitimate", 85