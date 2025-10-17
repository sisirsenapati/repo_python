# Importing Libraries
from gtts import gTTS
import PyPDF2

# Open file Path
pdf_File = open('samplepdf.pdf', 'rb')

# Create PDF Reader Object
pdf_Reader = PyPDF2.PdfReader(pdf_File)
count = len(pdf_Reader.pages)  # total number of pages in the PDF
textList = []

# Extracting text data from each page of the PDF file
for i in range(count):
    try:
        page = pdf_Reader.pages[i]
        text = page.extract_text()
        if text:
            textList.append(text)
    except Exception as e:
        pass

# Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

# Set language to english (en)
language = 'en'

# Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

# Save as mp3 file
myAudio.save("Audio.mp3")

# Close the PDF file
pdf_File.close()
