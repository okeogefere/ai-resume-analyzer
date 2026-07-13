SKILLS = [
    "python","fastapi","django","flask","sql","postgresql","mysql",
    "mongodb","pandas","numpy","scikit-learn","tensorflow","pytorch",
    "docker","kubernetes","git","github","linux","aws","azure","gcp",
    "power bi","excel",
]



def extract_keywords(text):
    keywords = set()

    for skill in SKILLS:
        if skill in text:
            keywords.add(skill)

    return keywords

def compare_keywords(resume_keywords, job_keywords):
    matched = resume_keywords & job_keywords
    missing = job_keywords - resume_keywords
    extra = resume_keywords - job_keywords

    return {
        "matched": matched,
        "missing": missing,
        "extra": extra
    }

def calculate_match_score(matched, total):
    if total == 0:
        return 0

    return round((len(matched) / total) * 100, 2)