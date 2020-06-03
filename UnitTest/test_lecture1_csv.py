import unittest
from lecture1_csv import *

class TestString(unittest.TestCase):
    def setUp(self):
        print('\n201704028 조 종운\n')

    def tearDown(self):
        print()

    def test_read_csv1(self):
        data = read_csv1('/lecture1/billboard.csv')
        print(data)
        print()
        print("Data cells from csv:")
        print(f"%s: %s" % (data[0][0], data[1][0]))
        print(f"%s: %s" % (data[0][1], data[1][1]))
        print(f"%s: %s" % (data[0][2], data[1][2]))

    def test_read_csv2(self):
        data = read_csv2('lecture1/billboard.csv')
        print(data)

        print("Data cells from csv")
        for e in data:
            print()
            [print(f"%s: %s" % (key, value)) for key, value in e.items()]\

    def test_write_csv(self):
        names = ['John', 'Fate', 'Jadon']
        grades = ['C', 'A', 'B']
        write_csv('lecture1/newlist.csv', names, grades)

    def test_write_tsv(self):
        names = ['John', 'Fate', 'Jadon']
        grades = ['C', 'A', 'B']
        write_tsv('lecture1/newlist.tsv', names, grades)

    def test_csv_dialect(self):
        data = csv_dialect('lecture1/pipes.csv')
        print('Data cells from csv:')
        for e in data:
            print()
            [print(f"%s: %s" % (key, value)) for key, value in e.items()]

    def test_ca_employees(self):
        manage_ca_employees('lecture1/mylist.csv', 'lecture1/mylist.csv')
        

if __name__ == "__main__":
    unittest.main()