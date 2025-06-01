import re
from typing import List
import spacy
from PyPDF2 import PdfReader

# Load spaCy model (make sure to install 'en_core_web_sm' or a larger model)
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def extract_skills(text: str) -> List[str]:
    """
    Extract skills from resume text using simple keyword matching and NLP.
    This can be enhanced with custom models or regex.
    """
    # Example skill keywords - this list can be expanded
    skill_keywords = [
        "python", "java", "javascript", "c++", "c#", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "flask", "django", "tensorflow",
        "pytorch", "machine learning", "data science", "nlp", "html", "css"
    ]
    text_lower = text.lower()
    found_skills = [skill for skill in skill_keywords if skill in text_lower]
    return found_skills
