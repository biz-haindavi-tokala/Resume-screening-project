SKILLS = [
    # Programming Languages
    "python", "java", "c++", "c", "r", "scala", "javascript", "typescript",
    
    # Databases & Querying
    "sql", "mysql", "postgresql", "mongodb", "nosql", "oracle", "sqlite",
    
    # Operating Systems & Tools
    "linux", "unix", "windows", "git", "github", "bash", "shell scripting",
    
    # Machine Learning
    "machine learning", "deep learning", "artificial intelligence",
    "supervised learning", "unsupervised learning", "reinforcement learning",
    "feature engineering", "model evaluation", "model deployment",
    "hyperparameter tuning", "data preprocessing",
    
    # Deep Learning & AI
    "neural networks", "cnn", "rnn", "lstm", "transformers",
    "nlp", "natural language processing", "computer vision",
    "generative ai", "llm", "bert", "gpt","RAG","LLM"
    
    # Data Science & Analytics
    "pandas", "numpy", "scipy", "matplotlib", "seaborn",
    "data analysis", "data visualization", "statistics",
    "exploratory data analysis", "eda","linear algebra", "probability", "statistics"
    
    # Big Data & Distributed Systems
    "spark", "hadoop", "hive", "kafka", "databricks",
    "distributed systems", "big data",
    
    # Cloud Platforms
    "aws", "amazon web services",
    "azure", "google cloud", "gcp",
    
    # MLOps & Deployment
    "docker", "kubernetes", "fastapi", "flask",
    "mlflow", "airflow", "ci/cd", "jenkins",
    
    # Databases Advanced
    "redis", "elasticsearch", "data warehouse",
    
    # Software Engineering
    "rest api", "microservices", "system design",
    "object oriented programming", "oop",
    
    # Others (modern AI stack)
    "llm fine tuning", "prompt engineering",
    "vector databases", "faiss", "langchain","langgraph"
]

def extract_skills(text):
    """
    Extract skills from text.
    """
    text = text.lower()
    extracted_skills = []
    for skill in SKILLS:
        if skill in text:
            extracted_skills.append(skill)  # extract skills common from skillset and job description/resume text
    return extracted_skills
    
def compare_skills(
    resume_text,
    job_description
):
    resume_skills = set(
        extract_skills(resume_text)         # extract skills from resume text in the skillset
    )

    jd_skills = set(
        extract_skills(job_description)     # extract skills from job description in the skillset
    )

    matched = resume_skills.intersection(
        jd_skills                           # common skills between resume and job description
    )

    missing = jd_skills - resume_skills     # skills in job description but not in resume

    return (
        sorted(list(matched)),
        sorted(list(missing))
    )