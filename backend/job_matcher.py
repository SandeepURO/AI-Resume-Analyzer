def calculate_job_match(
    resume_skills,
    job_description
):

    job_text = job_description.lower()

    matched = []

    missing = []

    for skill in resume_skills:

        if skill.lower() in job_text:
            matched.append(skill)

    common_skills = [
        "python",
        "flask",
        "sql",
        "git",
        "docker",
        "aws",
        "machine learning",
        "tensorflow",
        "pandas",
        "numpy"
    ]

    for skill in common_skills:

        if skill in job_text and skill not in [
            s.lower() for s in resume_skills
        ]:
            missing.append(skill)

    if len(common_skills) == 0:
        score = 0
    else:
        score = int(
            (len(matched) /
            max(len(matched) + len(missing), 1))
            * 100
        )

    return score, matched, missing