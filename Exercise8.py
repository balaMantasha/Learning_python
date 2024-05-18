#Exercise
#Write a program to manipulate pdf files using pyPDF. Your proghram should be able to merge multiple
#pdf files into a single pdf. You are welcome to add more functionalities
#pypdf is a free and open source pure-python PDF library capabale of splitting, merging,cropping, and transforming 
#the pages of pdf files. It can aslo add custom data, Viewing options, and passwords to pdf files. pypdf can retrieve
#text and metadata from pdfs as well.
from PyPDF2 import PdfWriter
import os
merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()
