import streamlit as st

from src.parser import extract_text_from_pdf
from src.scorer import calculate_similarity
from src.skills import compare_skills


st.set_page_config(
    page_title="Resume Screening System"
)

st.title("AI Resume Screening System")

job_description = st.text_area("Paste Job Description")

uploaded_file = st.file_uploader(   # Upload Resume PDF
    "Upload Resume PDF",
    type=["pdf"]
)


if st.button("Analyze Resume"):

    if not uploaded_file:
        st.warning("Please upload a resume.")

    elif not job_description:
        st.warning("Please enter a job description.")

    else:

        resume_text = extract_text_from_pdf(uploaded_file)

        score = calculate_similarity(
            resume_text,
            job_description
        )

        matched_skills, missing_skills = compare_skills(
            resume_text,
            job_description
        )

        st.success("Analysis Complete")

        st.metric("Match Score", f"{score}%")

        st.subheader("Matched Skills")
        st.write(matched_skills)

        st.subheader("Missing Skills")
        st.write(missing_skills)

        st.subheader("Recommendation")

        if score > 80:
            st.success("Strong Match")

        elif score > 60:
            st.info("Potential Match")

        else:
            st.warning("Low Match")