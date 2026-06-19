import re


def calculate_similarity(resume_text, job_text):
    
    jd_skills=set(re.findall(r'\b\w+\b', job_text.lower())) #Hello, world, 123, abc_def (\b - word boundaries)
    resume_skills=set(re.findall(r'\b\w+\b', resume_text.lower()))
    score=len(jd_skills.intersection(resume_skills))/len(jd_skills) if jd_skills else 0

    return round(score * 100, 2)

