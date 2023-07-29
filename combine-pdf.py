from pypdf import PdfWriter
import sys


print(sys.argv[1:])
merger = PdfWriter()
for pdf in sys.argv[1:]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
