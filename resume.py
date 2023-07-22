import streamlit as st
import spacy
from spacy.matcher import PhraseMatcher
import re

# Load English language model for NLP
nlp = spacy.load("en_core_web_sm")

# Function to find the developer type from the resume text
def find_developer_type(resume_text):
    
    backend_keywords = ['backend', 'python','java','node.js','php','ruby','django','flask','server-side', 'database', 'SQL', 'API']
    frontend_keywords = ['frontend', 'client-side', 'HTML', 'CSS', 'JavaScript','react','angular','vue']
    full_stack_keywords = ['full stack', 'full-stack','mean','mern','lamp','laravel','express','end-to-end']
 
    # Create a SpaCy document for the resume text
    doc = nlp(resume_text)

    # Check for developer type in document text
    text_lower = resume_text.lower()
    if any(keyword in text_lower for keyword in full_stack_keywords):
        return 'Full Stack Developer'
    elif any(keyword in text_lower for keyword in backend_keywords):
        if any(keyword in text_lower for keyword in frontend_keywords):
            return 'Full Stack Developer'
        else:
            return 'Backend Developer'
    elif any(keyword in text_lower for keyword in frontend_keywords):
        return 'Frontend Developer'
    else:
        # Check for developer type in document headings
        for heading in doc.ents:
            if any(keyword in heading.text.lower() for keyword in full_stack_keywords):
                return 'Full Stack Developer'
            elif any(keyword in heading.text.lower() for keyword in backend_keywords):
                if any(keyword in heading.text.lower() for keyword in frontend_keywords):
                    return 'Full Stack Developer'
                else:
                    return 'Backend Developer'
            elif any(keyword in heading.text.lower() for keyword in frontend_keywords):
                return 'Frontend Developer'

    return 'Developer Type Not Specified'

# Function to extract years of experience from the resume text
def find_experience(resume_text):
    # Regular expression pattern to find experience in the format 'X years' or 'X months'
    experience_pattern = r'\b(\d+)\s*(?:years?|months?)\b'
    experience_matches = re.findall(experience_pattern, resume_text, re.IGNORECASE)

    if experience_matches:
        total_experience = sum(map(int, experience_matches))
        return f"{total_experience} {'Years' if total_experience > 1 else 'Year'} of Experience"

    # Check for experience in the format 'start_date - end_date'
    date_range_pattern = r'(\d{4})\s*-\s*(?:present|current|\d{4})'
    date_range_matches = re.findall(date_range_pattern, resume_text, re.IGNORECASE)

    if date_range_matches:
        start_date, end_date = date_range_matches[0]
        start_year = int(start_date)
        end_year = int(end_date) if end_date.isdigit() else int(st.session_state.current_year)
        total_experience = end_year - start_year
        return f"{total_experience} {'Years' if total_experience > 1 else 'Year'} of Experience"

    # Check for experience in words like 'five years of experience'
    words_pattern = r'\b(\w+)\s*(?:years?|months?)\b'
    words_matches = re.findall(words_pattern, resume_text, re.IGNORECASE)

    if words_matches:
        total_experience = sum(int(word) for word in words_matches if word.isdigit())
        return f"{total_experience} {'Years' if total_experience > 1 else 'Year'} of Experience"

    return "Fresher"

# Function to rank candidates based on their experience, content, achievements, and knowledge
def rank_candidates(candidates):
    ranked_candidates = []

    for candidate in candidates:
        developer_type, resume_text, experience = candidate

        # You can add more factors to consider in the ranking here
        content_score = compute_content_score(resume_text)
        keyword_score = compute_keyword_score(resume_text)
        achievement_score = compute_achievement_score(resume_text)
        knowledge_score = compute_knowledge_score(resume_text)

        # Calculate the overall score based on different factors (you can adjust weights as needed)
        overall_score = 0.3 * content_score + 0.2 * keyword_score + 0.2 * achievement_score + 0.3 * knowledge_score

        ranked_candidates.append((developer_type, experience, overall_score, resume_text))

    # Sort candidates based on their overall score
    ranked_candidates = sorted(ranked_candidates, key=lambda x: (x[2]), reverse=True)

    return ranked_candidates

# Functions to compute different scores for ranking (you can customize these functions)
def compute_content_score(resume_text):
    # Calculate the content score based on the length of the resume text
    return len(resume_text)

def compute_keyword_score(resume_text):
    # You can define a list of keywords relevant to the job position and calculate the keyword score
    # For example, you can count the occurrences of these keywords in the resume text
    keywords = ['python', 'javascript', 'database', 'frontend', 'backend', 'framework', 'algorithm']
    return sum(resume_text.lower().count(keyword) for keyword in keywords)

def compute_achievement_score(resume_text):
    # You can analyze the resume text to identify specific achievements and assign scores accordingly
    # For example, count the number of times "achieved," "led," or "implemented" appear in the text
    return resume_text.lower().count("achieved") + resume_text.lower().count("led") + resume_text.lower().count("implemented")

def compute_knowledge_score(resume_text):
    # You can analyze the resume text for specific technical jargon or domain-specific terms
    # and assign scores based on the depth of knowledge demonstrated
    return resume_text.lower().count("machine learning") + resume_text.lower().count("data analysis")

# Main function for Streamlit web app
def main():
    st.title("Resume Analyzer")

    uploaded_files = st.file_uploader("Upload resume(s)", type=["txt", "pdf"], accept_multiple_files=True)

    if uploaded_files:
        # Initialize the list of candidates for ranking
        candidates = []

        for uploaded_file in uploaded_files:
            try:
                resume_text = uploaded_file.read().decode('utf-8', errors='ignore')
            except:
                st.error(f"Error reading {uploaded_file.name}. Please make sure it's a valid text or PDF file.")
                continue

            st.subheader(f"Analysis for {uploaded_file.name}")

            # Find Developer Type
            developer_type = find_developer_type(resume_text)
            st.write("Developer Type:", developer_type)

            # Find Experience
            experience = find_experience(resume_text)
            st.write("Experience:", experience)

            # Collect candidate details for ranking (only if multiple resumes are uploaded)
            if len(uploaded_files) > 1:
                candidate_details = (developer_type, resume_text, experience)
                candidates.append(candidate_details)

        # Rank candidates (only if multiple resumes are uploaded)
        if len(candidates) > 1:
            ranked_candidates = rank_candidates(candidates)


if __name__ == "__main__":
    # Initialize the current year for calculating the experience with "present" or "current" dates
    st.session_state.current_year = 2023
    main()
