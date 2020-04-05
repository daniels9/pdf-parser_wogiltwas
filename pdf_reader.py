import PyPDF2
import re

# Transform pdf to raw text
def readpdf(pdf):
    pdfReader = PyPDF2.PdfFileReader(pdf)

    # Get basic information from pdf (creation date, modification date)
    info = pdfReader.getDocumentInfo()
    print(info)

    # Get number of pages and extract text from every page
    for page in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(page)
            pagetext = pageObj.extractText()
            #rawtext.append(pagetext)
            filterpdf(pagetext)

#print(rawtext)
#filterpdf(rawtext)
#info = pageObj.getDocumentInfo()
#print(info)


# Filter raw text for defined regularexpressions
def filterpdf(rawtext):
    r1 = re.search("(Verbot)(\w|\W)*$", rawtext)
    print(r1)
    r2 = re.search("(Ausgenommen)(\w|\W)*$", rawtext)
    print(r2)
