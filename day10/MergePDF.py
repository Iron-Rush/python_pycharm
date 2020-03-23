# MergePDF.py
from PyPDF2 import PdfFileReader, PdfFileMerger
merger = PdfFileMerger()
input1 = open("2020年接收推荐免试研究生（含直接攻博）招生目录.pdf", "rb")
input2 = open("3上海外国语大学2020年硕士研究生招生专业目录.pdf", "rb")

merger.append(fileobj = input1, pages=(0,2))
merger.merge(position = 2, fileobj = input2, pages = (0,1))
output = open("document-output.pdf", "wb")
merger.write(output)