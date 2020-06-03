import unittest
from lecture2_xlxs import *

# Permission denied 에러는 파일이 열려있는 경우 발생
class TestString(unittest.TestCase):
    def setUp(self):
        print('201704028  조 종운\n')

    def tearDown(self):
        print()

    def test_read_xlxs(self):
        book, sheet = read_xlxs('lecture2/myxlxs.xlxs')
        print('Sheets:', book.sheetnames)
        print('Sheet:', sheet.title)
        print('First cell:', sheet['A1'].value)
        print('Other cell:', sheet.cell(row=3, column=2).value)

        fm = '%-7s'
        for r in sheet.rows:
            print(f"{fm}: %s, %s" % (r[0].value, r[1].value, r[2].value))

    def test_write_xlxs(self):
        data = (
            ['Rent', 1000],
            ['Gas', 100],
            ['Food', 300],
            ['Gym', 50]
        )

        write_xlxs('lecture2/expenses.xlxs', 'expenses', data)


    def test_write_format_xlxs(self):
        data = (
            ['Rent', 1000],
            ['Gas', 100],
            ['Food', 300],
            ['Gym', 50]
        )

        cells = 'B1:B4'
        fm = {
            'bg_color': 'blue'
        }
        condition = {
            'type': 'cell',
            'criteria': '>=',
            'value': 150
        }

        write_format_xlxs('lecture2/expenses.xlxs', 'expenses', data, cells, fm, condition)
        

if __name__ == '__main__':
    unittest.main()