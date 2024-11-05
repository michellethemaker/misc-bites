# Description: Parses through all PDFs for specific texts, saving them in .csv file called output.csv. This file will be found in the same directory as the script itself.
# Requirements: At least Python 3.9.0. 
#               Install by running python installation file from the .exe in this link: https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
# Requirements: Run this in command prompt: pip install pymupdf
# Requirements: This pdfextractor.py script must be in the folder containing the folder containing the PDFs. 
#               e.g. Downloads folder
#                    =====> pdfextractor.py
#                    =====> pdfFolder
#                       =====> abc.pdf
#                       =====> def.pdf
# Run script in command line(make sure you're in the directory containing the script) with: python pdfextractor.pdf
# Author: michellethemaker
#======================================================================================================================

import os
import sys
from glob import glob
from os import path
import fitz
import csv

def findPDF(folderpath):
    filenames = []
    if os.path.exists(folderpath):
        for file in os.listdir(folderpath):
            if file.lower().endswith('.pdf'):
                # print(f"Found PDF file at: {folderpath}\n {file}\n=================")
                filenames.append(os.path.join(folderpath, file))
                
            else:
                sys.exit(f'ERROR: sorry, no PDFs detected in {folderpath}')
        return filenames
    else:
        sys.exit(f'ERROR: sorry, {folderpath} doesnt exist')

def parsethroughPDF(filenames):
    with open('output.csv', mode='w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['ROW NAME 1', 'ROW NAME 2', 'ROW NAME 3'])  

                try:
                    for file in filenames:
                        doc = fitz.open(file)
                
                        for page in doc:
                            rect = page.rect
                            # print(f'document dimensions: w: {rect.width}, h: {rect.height}\n\n')
                            clip = fitz.Rect(0, rect.height * 0.15, rect.width, rect.height*0.35)
                            text = page.get_text("blocks",clip=clip) # DO CLIP TO CROP WHERE FITZ IS SUPPOSED TO ANALYZE. BLOCKS RETURNS TEXT IN BLOCKS. YOU CAN RETURN IN OTHER FORMS (SEE DOCS https://pymupdf.readthedocs.io/en/latest/recipes-text.html FOR INFO)
                            # print(f'{text[5][4]}')
                            if text:
                                # adjust where you see fit. 
                                firstRowOfPdf = text[0][4].strip()
                                firstRowOfPdf_values = firstRowOfPdf.split('\n')  # split returned text by the '\n' text which i got for an example
                                secondRowOfPdf = text[3][4].strip()
                                secondRowOfPdf_values = secondRowOfPdf.split('\n')
                                thirdRowOfPdf = text[4][4].strip()
                                thirdRowOfPdf_values = thirdRowOfPdf.split('\n')

                                if len(firstRowOfPdf_values) >= 2:
                                    firstvarname = firstRowOfPdf_values[0] 
                                    secondvarname = secondRowOfPdf_values[0].split("UNWANTED TEXT AT START OF TEXT ")[1]
                                    thirdvarname = thirdRowOfPdf_values[0].split("UNWANTED TEXT AT START OF TEXT ")[1].replace(" ", ".")

                                    print(f'===========VALUES==========\n{firstvarname} {secondvarname}\n{thirdvarname}')
                                    
                                    csv_writer.writerow([firstvarname, secondvarname, thirdvarname])
                        doc.close()
                    print(f'Parsed through {len(filenames)} files, output saved in output.csv')
                except:
                    print(f'Error occured!')

def main():
    filenames = []
    folderpath = input('enter the name of the folder holding the PDFs. Just enter if PDFs are in the default folder name of ''pdfFolder'': ')
    if folderpath =='':
        print(folderpath)
        folderpath = os.path.abspath(f'./pdfFolder/')
    filenames = findPDF(folderpath)
    print(f'no. of files in folder: {len(filenames)}')
    if not filenames:
        print(f'no files detected in {folderpath}')
    if filenames:
        parsethroughPDF(filenames)


# Run main function
if __name__ == "__main__":
    main()