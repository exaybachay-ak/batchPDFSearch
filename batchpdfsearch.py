### Scan all files in directory for lines containing a word or phrase
# Updated 3-25-2024: Update deprecated calls to PyPDF2 and re.findall

# Imports
import PyPDF2
#from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader
import re
import os

# Functions
def getPdfContents(path):
		content = []
		if re.findall('\\.pdf', path):
				p = open(path, "rb")
				#pdf = PdfFileReader(p)
				pdf = PdfReader(p)
				#for i in range(0, pdf.numPages):
				for i in range(0, len(pdf.pages)):
						#content += pdf.getPage(i).extractText().splitlines()
						content += pdf.pages[i].extract_text().splitlines()
				return content

def findText(pattern):
		# Get all files in directory for searching
		files = os.listdir()
		for file in files:
				text = getPdfContents(file)
				try:
						for line in text:
								found = re.search(r'.*'+searchpattern+'.*', line, re.IGNORECASE)
								if found:
										print(line)
				except:
						print("Didn't work for some reason.. probably a type error.")

# Main program functionality
if __name__ == "__main__":
		searchpattern = input("What text are you looking for?")
		findText(searchpattern)
