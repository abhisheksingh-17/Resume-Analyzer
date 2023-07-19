Resume Analyzer-
Resume Analyzer is a web application built with Streamlit and Python that allows users to upload their resumes and determine if they are a frontend or backend developer based on the content of the resume.

Installation
1.Clone the repository:
git clone 

2.Navigate to the project directory:
cd resume

3.Install the required dependencies using pip:
pip install -r requirements.txt

4.Run the Streamlit app:
streamlit run resume.py
The application should now be running locally. Open your web browser and access the app at http://localhost:8501.

Usage-
1.Open the web application in your browser.
2.Click on the "Upload a resume file" button.
3.Select a resume file (supported formats: PDF, DOCX) from your local machine.
4.The application will process the resume and display the determined developer type (frontend, backend, or unknown) based on the resume content.

Technologies Used-
Python
Streamlit
spaCy

Here's a description of the code:
1.The code is a web application built using Streamlit, a Python library for creating interactive web pages. The application allows users to upload their resumes and determines if they are a frontend or backend developer based on the content of the resume.
2.The main functionality is implemented in the determine_developer_type function. This function uses the spacy library for Natural Language Processing (NLP) and creates a phrase matcher to match frontend and backend keywords in the resume text. It counts the number of matches for each developer type and determines the type with the highest count.
3.The Streamlit app is created using the streamlit library. It provides a user-friendly interface where users can upload their resume files. Once a file is uploaded, the app reads the file contents, passes them to the determine_developer_type function, and displays the determined developer type on the web page.

License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

Acknowledgments
1.The project uses the spaCy library for Natural Language Processing.
2.Special thanks to the Streamlit community for their support and guidance.


