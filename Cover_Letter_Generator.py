# Import necessary libraries
from openai import OpenAI # pip install openai
import gradio as gr #pip install gradio
from gradio import Interface, Textbox
import re
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
import os
from PyPDF2 import PdfReader # pip install PyPDF2
import docx2txt # pip install docx2txt

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

def _extract_text_from_upload(file, allowed_extensions=["pdf", "docx"]):
  """
  Extracts text from an uploaded file.

  Args:
    file: A file object uploaded by the user.
    allowed_extensions: List of allowed file extensions.

  Returns:
    Extracted text content from the file.
  """

  filename, extension = os.path.splitext(file.name)
  extension = extension.lower()[1:]

  if extension not in allowed_extensions:
    raise Exception(f"Unsupported file format: {extension}")

  text = ""
  if extension == "pdf":
    reader = PdfReader(file)
    for page in reader.pages:
      text += page.extract_text()
  elif extension == "docx":
    text = docx2txt.process(file)

  return text  

def preprocess_text(text):
  """
  Preprocesses the input text for cover letter generation.

  Args:
    text: The input text to be preprocessed.

  Returns:
    The preprocessed text.
  """

  wnl = WordNetLemmatizer()

  # Remove special characters and punctuation
  text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

  # Lemmatize words
  text = " ".join(wnl.lemmatize(word) for word in text.split())
  
  return text.strip()

def generate_cover_letter(resume_file, job_description):
  """
  Generates a cover letter based on the provided resume and job description.

  Args:
    resume: Text of the user's resume.
    job_description: Text of the job description.

  Returns:
    A string containing the generated cover letter.
  """

  # Extract text from uploaded resume file
  resume = _extract_text_from_upload(resume_file)

  # Preprocess text
  resume = preprocess_text(resume)
  job_description = preprocess_text(job_description)
  # Exam the preprocessed resume
  print (resume)
  
  # Generate cover letter
  messages = [
    {"role": "user", "content": f"Generate a cover letter based on the following resume:\n{resume} match the following job requirements: {job_description} \nin 150 words only. Highlight relevant skills, experiences, and achievements from the resume that align with the job description. Ensure the cover letter is concise, well-structured, and tailored to the specific requirements of the role. Avoid including any information that is not present in the provided resume."},
  ]
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.3
  )

  return response.choices[0].message.content
# Alternative prompts:
# Compose a professional cover letter based on the resume:\n{resume} match the following job requirements: {job_description} \nin 150 words only. Highlight relevant skills, experiences, and achievements from the resume that align with the job description. Ensure the cover letter is concise, well-structured, and tailored to the specific requirements of the role. Avoid including any information that is not present in the provided resume.
# Generate a cover letter based on the following resume:\n{resume} match the following job requirements: {job_description} \nin 150 words only. Highlight relevant skills, experiences, and achievements from the resume that align with the job description. Ensure the cover letter is concise, well-structured, and tailored to the specific requirements of the role. Avoid including any information that is not present in the provided resume.

# Resume Surviver:
# Prompt for revise your resumes to better align with job descriptions and improve the chances of passing through Applicant Tracking Systems (ATS).
# Revise my resume: {resume} to fit in the job description: {job_description} to survive in the Applicant Tracking Systems.

# File validation
def validate_file(file):
  filename, extension = os.path.splitext(file.name)
  extension = extension.lower()[1:]

  if extension not in ["pdf", "docx"]:
    raise Exception(f"Unsupported file format: {extension}")

# Gradio interface
inputs = [
    gr.File(type="filepath", label="Upload Resume"),
    gr.Textbox(label="Job Description", type="text", lines=5),
]

outputs = gr.Textbox(label="Cover Letter", type="text")

interface = gr.Interface(
    fn=generate_cover_letter, inputs=inputs, outputs=outputs, title="Cover Letter Generator"
)

interface.launch()