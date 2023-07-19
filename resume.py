import streamlit as st
import spacy

# Function to determine if the resume indicates frontend or backend developer
def determine_developer_type(text):
    nlp = spacy.load('en_core_web_sm')
    
    frontend_keywords = ['HTML', 'CSS', 'JavaScript', 'React', 'Angular']
    backend_keywords = ['Python', 'Java', 'C#', 'Node.js', 'SQL']
    
    frontend_count = sum([1 for keyword in frontend_keywords if keyword.lower() in text.lower()])
    backend_count = sum([1 for keyword in backend_keywords if keyword.lower() in text.lower()])
    
    if frontend_count > backend_count:
        return 'Frontend Developer'
    elif backend_count > frontend_count:
        return 'Backend Developer'
    else:
        return 'Unknown Developer Type'

# Streamlit web app
def main():
    st.title("Resume Analyzer")
    st.write("Upload your resume to determine if you are a frontend or backend developer.")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a resume file", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        text = file_contents.decode('utf-8', errors='ignore')  # Ignore decoding errors
        developer_type = determine_developer_type(text)
        
        st.write(f"Developer Type: {developer_type}")

# Run the app
if __name__ == '__main__':
    main()
