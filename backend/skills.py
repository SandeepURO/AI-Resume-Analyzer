SKILLS_DB = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Flask",
    "Django",
    "FastAPI",
    "MongoDB",
    "MySQL",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Computer Vision",
    "NLP",
    "Data Science",
    "Git",
    "GitHub",
    "Docker",
    "AWS"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS_DB:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))