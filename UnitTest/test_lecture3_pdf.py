import unittest
from lecture3_pdf import *
from lecture3_employee_payslip import *
import os

dir = 'UnitTest/lecture3'

class TestString(unittest.TestCase):
    def setUp(self):
        print('201704028 조 종운 \n')

    def tearDown(self):
        print()

    def test_read_pdf(self):
        reader, info = readPDF(f'{dir}/test1.pdf')

        print(f'Title: {info.title}')
        print(f'Author: {info.author}')
        print(f'Number of Pages: {reader.getNumPages()}')
        print()

        print('Page 1:')
        page = reader.getPage(1)
        print(page.extractText())
        print()

        print('Outline:')
        for heading in reader.getOutlines():
            if type(heading) is not list:
                print(dict(heading).get('Title'))

    def test_write1_pdf(self):
        writePDF1(f'{dir}/test2.pdf', f'{dir}/myPDF.pdf')

    def test_write2_pdf(self):
        writePDF2(f'{dir}/myPDF.pdf')

    def test_write3_pdf(self):
        writePDF3(dir)

    def test_write4_pdf(self):
        writePDF4(f'{dir}/header_footer.pdf')

    def test_merge_pdf(self):
        filePath = mergePDF(f'{dir}/pdfs')

        reader, info = readPDF(filePath)
        print(info)

    def test_rotate_pdf(self):
        rotatePDf(f'{dir}/myPDF.pdf')

    def test_encrypted_pdf(self):
        encryptPDF(f'{dir}/myPDF.pdf', '12345')

    def test_employee_payslip(self):
        employee_data = [
            {
                'id': 111,
                'name': 'Chongwoon Cho',
                'payment': 20000,
                'tax': 3000,
                'total': 17000,
                'birth': '970924'
            },

            {
                'id': 115,
                'name': 'Dongwon Gang',
                'payment': 50000,
                'tax': 7000,
                'total': 43000,
                'birth': '840212'
            }
        ]

        for emp in employee_data:
            filePath = generate_payslip(emp)
            encryptPDF(filePath, emp['birth'])

if __name__ == '__main__':
    unittest.main()