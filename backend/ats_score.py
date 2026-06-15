def calculate_ats_score(skills):

    score = len(skills) * 8

    if score > 100:
        score = 100

    return score