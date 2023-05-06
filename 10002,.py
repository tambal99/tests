import docx
doc = docx.Document('D:\вф\suv sathi.docx')
text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text)
print('\n'.join(text))

print(doc)