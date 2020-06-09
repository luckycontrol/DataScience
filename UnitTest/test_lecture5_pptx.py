import unittest
from lecture5_pptx import *

dir = 'UnitTest/lecture5'

class TestString(unittest.TestCase):
    def setUp(self):
        print('201704028 조 종운 \n')

    def tearDown(self):
        print('')

    def test_readPPT(self):
        prs = readPPT(f'{dir}/myprofile.pptx')

        i = 1
        for slide in prs.slides:
            print('Slide: ', i)
            print('Layout: ', slide.slide_layout.name)
            
            for shape in slide.shapes:
                print('Shape: ', shape.shape_type)
            
            print()

            i += 1
            
        text_runs = []
        for slide in prs.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                
                for paragraph in shape.text_frame.paragraph:
                    for run in paragraph.runs:
                        text_runs.append(run.text)

        print('Text is: ', text_runs)

    def test_writePPT(self):
        writeNewPPT(f'{dir}/yoPython.pptx')

    def test_writePPT1(self):
        writePPT1(f'{dir}/yoPython.pptx')

    def test_writePPT2(self):
        writePPT2(f'{dir}/two_content.pptx')

    def test_writePPT3(self):
        writePPT3(f'{dir}/textBox.pptx')

    def test_write_shapes(self):
        writeShapesPPT(f'{dir}/shape.pptx')

    def test_write_table(self):
        writeTable(f'{dir}/table.pptx')