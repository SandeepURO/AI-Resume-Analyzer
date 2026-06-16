def extract_education(text):

    education_keywords = [
        "b.tech",
        "btech",
        "b.e",
        "be",
        "m.tech",
        "mtech",
        "bachelor",
        "master",
        "engineering",
        "university",
        "college"
    ]

    found = []

    text_lower = text.lower()

    for keyword in education_keywords:

        if keyword in text_lower:
            found.append(keyword)

    return list(set(found))