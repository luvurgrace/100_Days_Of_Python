from PyPDF2 import PdfReader
from gtts import gTTS

# Read PDF
pdf_path = "book.pdf"
reader = PdfReader(pdf_path)

text = ""
for page in reader.pages:
    text += page.extract_text()

print(f"Extracted {len(text)} characters")

# Convert to speech
tts = gTTS(text=text, lang='en', slow=False)
tts.save("audiobook.mp3")

print("Done! Saved as audiobook.mp3")