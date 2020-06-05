import unittest
from lecture4_docx import *

dir = 'UnitTest/lecture4'

class TestString(unittest.TestCase):
    def setUp(self):
        print('201704028 조 종운')

    def tearDown(self):
        print('')

    def test_read_document(self):
        doc, prop = readDocument(f'{dir}/test.docx')

        print('Title: %s' % doc.paragraphs[0].text)
        print('Author: %s' % prop.author)
        print('Created: %s' % prop.created)
        print('Revision: %s' % prop.revision)
        print()

        if doc.tables:
            table = doc.tables[0]

            for i in range(len(table.rows)):
                row = table.rows[i]
                print('Row: %d' %(i+1))
                
                for j in range(len(row.cells)):
                    print(row.cells[j].paragraphs[0].text)
                print()

    def test_write_document(self):
        writeNewDocument(f'{dir}/write_document.docx')

    def test_write_new_document(self):
        writeDocument(f'{dir}/write_document.docx')

    def test_new_hire_orientation(self):
        employee_data = [
            {
                'id': 123,
                'name': 'John Sally',
                'department': 'Operations',
                'isDue': True
            },

            {
                'id': 245,
                'name': 'Robert Langford',
                'department': 'Software',
                'isDue': False
            },
        ]

        agenda = {
            'Operations': ['SAP Overview', 'Inventory Management'],
            'Software': ['Language Overview', 'Computer Architecture'],
            'Hardware': ['Computer Aided Tools', 'Hardware Design']
        }

        generate_document(dir, employee_data, agenda)