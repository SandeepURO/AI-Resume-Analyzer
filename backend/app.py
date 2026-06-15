from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from resume_parser import extract_text_from_pdf
from skills import extract_skills
from ats_score import calculate_ats_score
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

    ats_score = calculate_ats_score(skills)

    return jsonify({
    "filename": file.filename,
    "ats_score": ats_score,
    "skills": skills,
    "text": extracted_text[:1000]
})

if __name__ == "__main__":
    app.run(debug=True)