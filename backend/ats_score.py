def calculate_ats_score(
    skills_count,
    education_count,
    project_count,
    experience_count
):

    score = 0

    score += min(skills_count * 4, 40)

    score += min(education_count * 5, 15)

    score += min(project_count * 5, 20)

    score += min(experience_count * 5, 15)

    score += 10

    return min(score, 100)