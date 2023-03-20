import PyPDF2
from gtts import gTTS
import os

# Open the PDF file
pdf_file = open('example.pdf', 'rb')

# Read the PDF file using the PdfReader class
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract the text from each page of the PDF
text = ''
for page in pdf_reader.pages:
    text += page.extract_text()

# Convert the text to speech
tts = gTTS(text=text, lang='en')

# Save the audio file
tts.save('example.mp3')

# Play the audio file
os.system('example.mp3')
