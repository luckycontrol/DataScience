from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from fpdf import FPDF
import os

def readPDF(filePath):
    pdf = open(filePath, 'rb')
    reader = PdfFileReader(pdf)
    return reader, reader.getDocumentInfo()

def writePDF1(filePathOpened, filePathWritten):
    reader, _ = readPDF(filePathOpened)
    writer = PdfFileWriter()

    writer.addBlankPage(595.27559055, 841.889076378)

    p = reader.getPage(0)
    writer.addPage(p)

    with open(filePathWritten, 'wb') as f:
        writer.write(f)

def writePDF2(filePath):
    reader = PdfFileReader(filePath, 'rb')
    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
        p = reader.getPage(i)
        if p.getContents():
            writer.addPage(p)

    with open(filePath, 'wb') as f:
        writer.write(f)

def writePDF3(dir):
    pdf = FPDF(format='letter')
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    pdf.cell(200, 10, txt='Welcome to class!', ln=1, align='C')
    pdf.output(f'{dir}/class3.pdf')
    pdf.close()

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.ln(10)
        self.cell(60)
        self.cell(0, 0, txt='Created by Jongwoon Cho', align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 0, txt='Page %s' % self.page_no(), align='C')

def writePDF4(filePath):
    pdf = PDF(format='A5')

    pdf.add_page()
    pdf.set_font('Times', size=12)

    for i in range(1, 50):
        pdf.cell(0, 10, txt='This is my new line, line number is %s' % i, ln=1, align='C')

    pdf.output(filePath)

def mergePDF(dir):
    merger = PdfFileMerger()

    files = [x for x in os.listdir(dir) if x.endswith('.pdf')]
    print('File merged: ', files)

    for fname in sorted(files):
        merger.append(PdfFileReader(open(f'{dir}/{fname}', 'rb')))


    metadata = {'/edited': 'Jongwoon Cho'}
    merger.addMetadata(metadata)

    filePath = f'{dir}/output.pdf'
    merger.write(filePath)
    merger.close()

    return filePath

def rotatePDf(filePath):
    fp = open(filePath, 'rb')

    reader = PdfFileReader(fp)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    
    writer = PdfFileWriter()
    writer.addPage(page)

    dir, filename = os.path.split(filePath)
    fw = open(f'{dir}/rotated_{filename}', 'wb')
    writer.write(fw)

    fw.close()
    fp.close()

def encryptPDF(filePath, password):
    fp = open(filePath, 'rb')

    reader = PdfFileReader(fp)
    writer = PdfFileWriter()

    for page in range(reader.numPages):
        writer.addPage(reader.getPage(page))
    
    writer.encrypt(password)

    dir, filename = os.path.split(filePath)
    fw = open(f'{dir}/encrypted_{filename}', 'wb')
    writer.write(fw)

    fw.close()
    fp.close()