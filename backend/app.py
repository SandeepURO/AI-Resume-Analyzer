from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from resume_parser import extract_text_from_pdf
from skills import extract_skills
from ats_score import calculate_ats_score
from education import extract_education
from projects import count_projects
from experience import detect_experience
from suggestions import generate_suggestions
from job_matcher import calculate_job_match
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return {
        "message": "AI Resume Analyzer Backend Running"
    }

@app.route("/frontend")
def frontend():
    return send_from_directory("../frontend", "index.html")

@app.route("/upload", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    extracted_text = extract_text_from_pdf(filepath)

    skills = extract_skills(extracted_text)

    education = extract_education(extracted_text)

    projects = count_projects(extracted_text)

    experience = detect_experience(extracted_text)

    
    suggestions = generate_suggestions(skills, education, projects, experience)

    job_description = """
Python Intern

Requirements:
Python
Flask
SQL
Git
Docker
AWS
Machine Learning
"""

    ats_score = calculate_ats_score(len(skills), len(education), projects, experience)

    job_match_score, matched_skills, missing_skills = calculate_job_match(skills, job_description)

    print("Suggestions:", suggestions)

    print("Match Score:", job_match_score)
    print("Matched:", matched_skills)
    print("Missing:", missing_skills)
    return jsonify({
    "filename": file.filename,
    "ats_score": ats_score,
    "skills": skills,
    "education": education,
    "projects": projects,
    "experience": experience,
    "suggestions": suggestions,

    "match_score": job_match_score,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "text": extracted_text[:1000]
})

if __name__ == "__main__":
    app.run(debug=True)