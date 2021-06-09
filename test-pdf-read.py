# importing module
import PyPDF2

testfile_name = "test_pdf_emk_esku.pdf"

# create a pdf file object
pdfFileObj = open(testfile_name, 'rb')

# create a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracte text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()