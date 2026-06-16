def count_projects(text):

    project_keywords = [
        "project",
        "developed",
        "built",
        "implemented",
        "created"
    ]

    count = 0

    text_lower = text.lower()

    for keyword in project_keywords:
        count += text_lower.count(keyword)

    return count