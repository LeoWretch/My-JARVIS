from docx import Document

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# def read_word_file(path): #this code for later work
#     doc = Document(path)
#     text = ""

#     for para in doc.paragraphs:
#         text += para.text + "\n"

#     return text