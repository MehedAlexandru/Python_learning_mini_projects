import PyPDF2
import sys

imput = sys.argv[1:]

def merger(file_to_merge):
    merged = PyPDF2.PdfFileMerger()
    for pdf in file_to_merge:
        print(pdf)
        merged.append(pdf)
    merged.write("merged.pdf")

merger(imput)

    
