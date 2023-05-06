with open('file.txt', 'r', encoding='utf-8-sig') as input_file:
    contents = input_file.read()

with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(contents)

import docx

# Create a new Word document
doc = docx.Document()

# Open the text file and read its contents
with open('output.txt.txt', 'r') as file:
    contents = file.read()

# Write the contents of the text file to the Word document
doc.add_paragraph(contents)

# Save the Word document
doc.save('output1.docx')

