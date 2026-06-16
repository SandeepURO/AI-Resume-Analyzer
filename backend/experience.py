def detect_experience(text):

    experience_keywords = [
        "internship",
        "experience",
        "worked",
        "freelance",
        "employee"
    ]

    score = 0

    text_lower = text.lower()

    for keyword in experience_keywords:

        if keyword in text_lower:
            score += 1

    return score