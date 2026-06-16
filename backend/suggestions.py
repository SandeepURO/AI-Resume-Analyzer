def generate_suggestions(
    skills,
    education,
    projects,
    experience
):

    suggestions = []

    if len(skills) < 5:
        suggestions.append(
            "Add more technical skills."
        )

    if len(education) == 0:
        suggestions.append(
            "Education section not detected."
        )

    if projects < 2:
        suggestions.append(
            "Add more projects."
        )

    if experience == 0:
        suggestions.append(
            "Add internship or work experience."
        )

    if len(suggestions) == 0:
        suggestions.append(
            "Excellent resume. Keep it up!"
        )

    return suggestions