from typing import List
import re

def parse_skills_from_text(text: str) -> List[str]:
    """
    Extract potential skills from a block of text using simple keyword matching.
    This can be enhanced with NLP or custom models.
    """
    skill_keywords = [
        "python", "java", "javascript", "c++", "c#", "sql", "aws", "docker",
        "kubernetes", "react", "node.js", "flask", "django", "tensorflow",
        "pytorch", "machine learning", "data science", "nlp", "html", "css"
    ]
    text_lower = text.lower()
    found_skills = [skill for skill in skill_keywords if skill in text_lower]
    return found_skills
