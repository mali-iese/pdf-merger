
from PyPDF2 import PdfMerger, PdfReader


filenames=["1.pdf","2.pdf"]
merger = PdfMerger()
for filename in filenames:
    merger.append(PdfReader(open(filename, 'rb')))

merger.write("document-output.pdf")
