# DAV-6500-Capstone_Cover-Letter-Generator
The Cover Letter Generator utilizes the Gradio library for creating a user-friendly interface and OpenAI's GPT-3.5 model for generating customized cover letters. The project allows users to upload their resumes and input job descriptions and then generate a tailored cover letter based on the provided information.

## Key Features
1. **User Interface:** The project provides an intuitive interface developed with Gradio, enabling users to interact with the application effortlessly.
2. **Text Processing:** Uploaded resumes are processed to remove special characters and punctuation and then lemmatized to normalize the text for better analysis.
3. **Cover Letter Generation:** Leveraging prompt engineering techniques, OpenAI's GPT-3.5 model generates cover letters tailored to the provided resume and job description. These cover letters highlight relevant skills, experiences, and achievements aligned with the job requirements.
4. **Resume Revision for ATS:** Since this application is built using Prompt Engineering. simply by changing the prompt, this application can turn into a Resume Survivor to enhance their chances of successfully passing through Applicant Tracking Systems (ATS) and increasing their visibility to recruiters.

## Getting Started
To get started with the Cover Letter Generator, follow these steps:
- Install the necessary dependencies (`gradio`, `openai`, `PyPDF2`, `docx2txt`, `nltk`) using `pip`.
- Ensure you have an API key for OpenAI, and replace `YOUR_OPENAI_API_KEY` in the code with your actual API key.
- Run the application: Just simply drop off your resume in the box, copy and paste only the job requirements in the text box.</br>
Hit the generate button, voilà your cover letter will be generated! 🎉
