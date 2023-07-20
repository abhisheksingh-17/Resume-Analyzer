
# Resume Analyzer

Resume Analyzer is a web application built with Streamlit and Python that allows users to upload their resumes and determine if they are a frontend or backend developer based on the content of the resume. The application employs Natural Language Processing (NLP) techniques to analyze the resume's content and identify relevant keywords and technologies commonly associated with frontend and backend development.



## Installation
1.Clone the repository:
```bash
git clone https://github.com/abhisheksingh-17/Resume-Analyzer.git
```
2.Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
3.There’s one more thing you’ll have to install:
```bash
python -m spacy download en_core_web_sm
There are various spaCy models for different languages. The default model for the English language is designated as en_core_web_sm. Since the models are quite large, it’s best to install them separately—including all languages in one package would make the download too massive
```
4.Run the Streamlit app:
```bash
streamlit run resume_analyzer.py
The application should now be running locally. Open your web browser and access the app at http://localhost:8501.
```

## Acknowledgements

 1.The project uses the spaCy library for Natural Language Processing.

 2.Special thanks to the Streamlit community for their support and guidance.

Feel free to customize this README file to include any additional information or instructions specific to your project.
## Usage and Instuctions

 1.Installation: The project's README provides clear instructions on how to clone the repository, install dependencies using pip, and run the application locally.

 2.Web Interface: The web interface is user-friendly, allowing users to easily upload their resume files and see the results on the same page.

 3.Open the web application in your browser.

 4.Click on the "Upload a resume file" button.

 5.Select a resume file (supported formats: PDF, DOCX) from your local machine.

 6.The application will process the resume and display the determined developer type (frontend, backend, or unknown) based on the resume content.
## How the Code Works

 1.Dependencies: The code uses two main libraries: streamlit for creating the web interface and spacy for Natural Language Processing. The requirements.txt file lists the necessary packages and their versions.

 2.Determining Developer Type: The core functionality is implemented in the determine_developer_type function. This function takes the resume text as input and identifies the presence of keywords related to frontend and backend development using spacy's NLP capabilities.

 3.Matching Keywords: To identify keywords, the function creates a PhraseMatcher from spacy and adds patterns for frontend and backend development-related keywords. The resume text is processed with spacy, and the matcher finds matches for these patterns.

 4.Counting Matches: The function counts the number of matches for frontend and backend keywords. Based on the count, it determines whether the resume leans more towards frontend development, backend development, or if the type cannot be conclusively determined.

 5.Web Application: The application uses streamlit to create a simple and intuitive web interface. Users can upload their resume files in PDF or DOCX format. The uploaded files are read, and their contents are passed to the determine_developer_type function.

 6.Displaying Results: The determined developer type (frontend, backend, or unknown) is displayed on the web page to the user.
## Technologies Used

1.Python
2.Streamlit
3.spaCy
## Project Scope and Future Enhancements

 1.The project's scope is limited to identifying frontend and backend development roles based on keyword matching. Future enhancements could involve more sophisticated NLP techniques to determine other types of developer roles or skills.

 2.The application could be expanded to include additional features, such as extracting other relevant information from resumes (e.g., work experience, education, skills) and presenting more detailed insights to the user.

 3.Integrating a machine learning model to classify the developer type based on the resume content could potentially improve accuracy.

 4.The user interface could be further improved with better visualizations and more interactive elements.
## License & Contribution
The project is open-source and licensed under the MIT License, allowing others to use, modify, and distribute the code freely.

The README file also encourages contributions from the community. Users can report bugs, suggest features, and submit pull requests to improve the application.

Overall, the Resume Analyzer is a simple yet valuable tool for individuals seeking to gain insights into their developer roles based on their resumes. As an open-source project, it has the potential to grow and improve through community contributions and feedback.