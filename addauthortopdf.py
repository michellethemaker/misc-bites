from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, TextStringObject
import os
import sys
from glob import glob
from os import path


def addAuthorToPDF(input_pdf_path, output_pdf_path, author_name):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # access existing metadata, create copy
    metadata = reader.metadata

    # prepare metadata dictionary
    new_metadata = {NameObject(k): TextStringObject(v) for k, v in metadata.items()}

    # add new author field to  metadata
    new_metadata[NameObject('/Author')] = TextStringObject(author_name)

    # assign updated metadata to writer
    writer.add_metadata(new_metadata)


    # write output PDF with updated metadata
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)
        print("DONE: successfully added authorship")

def listPDF(partialfilename=""):
    path = sys.path[0]
    allfiles = []
    if partialfilename:
        partialfilename = partialfilename.lower()
    for file in os.listdir(path):
        if file.lower().endswith('.pdf'):
            if partialfilename in file.lower():
                allfiles.append(file)
    print(f'files: {allfiles}')

def checkFileExists(filename):
    while True:
        pdf_path = os.path.abspath(filename)
        if not filename.endswith('.pdf'):
            sys.exit(f'Please make sure the file has a .pdf extension.')

        if os.path.exists(pdf_path) and os.path.isfile(pdf_path):
            print(f"Found PDF file at: {pdf_path}")
            return filename
        else:
            sys.exit(f'ERROR: sorry, {filename} doesnt exist')

def main():
    nextpdf = True
    while nextpdf:
        partialfilename = input('enter partial filename to start pdf name search: ')
        listPDF(partialfilename)
        input_pdf = checkFileExists(input('Name of pdf: '))
        output_pdf = f"updated_{input_pdf}"
        author_name = input('Enter author name: ')
        if not author_name:
            sys.exit(f'ERROR: Where the name at?')
        
        nextpdfprompt = input('Anymore PDFs? Enter y to keep going, any other key to exit: ')
        if nextpdfprompt != 'y':
            print(f'Thank you for using addPDFToAuthor. Exiting now...')
            nextpdf = False

# Run main function
if __name__ == "__main__":
    main()
