from datetime import datetime
from fpdf import FPDF, HTMLMixin

class PaySlip(FPDF, HTMLMixin):
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Google', 1, 0, 'C')
        self.ln(20)

def generate_payslip(data):
        month = datetime.now().strftime('%B')
        year = datetime.now().strftime('%Y')

        pdf = PaySlip(format='letter')
        pdf.add_page()

        pdf.set_font('Times', size=12)
        pdf.cell(200, 10, txt='Pay Slip for %s, %s' % (month, year), ln=3, align='C')
        pdf.cell(50)
        pdf.cell(100, 10, txt='Employee Id: %s' % data['id'], ln=1, align='L')
        pdf.cell(50)
        pdf.cell(100, 10, txt='Employee Name: %s' % data['name'], ln=3, align='L')

        html = """
            <table border="0" align="center" width="50%">
            <thead>
                <tr>
                    <th align="left" width="50%"> Pay Slip Details </th>
                    <th align="right" width="50%"> Amount in USD </th>
                </tr>
            <tbody>
                <tr> <td> Payment </td> <td align="right"> """ + str(data['payment']) + """ </td> </tr>
                <tr> <td> Tax </td> <td align-"right"> """ + str(data['tax']) + """ </td> </tr>
                <tr> <td> Total </td> <td align="right"> """ + str(data['total']) + """ </td> </tr>
            </tbody>
            </table>
            """

        pdf.write_html(html)

        filePath = 'UnitTest/lecture3/payslip %s.pdf' % data['id']
        pdf.output(filePath)
        return filePath