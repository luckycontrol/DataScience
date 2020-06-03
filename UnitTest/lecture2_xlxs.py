import openpyxl as xr
import xlsxwriter as xw
import os

def read_xlxs(filePath, sheetName=None):
    # data_only = True ( 수식을 제외시킴 )
    book = xr.load_workbook(filePath,  data_only=True)
    return book, (book[sheetName] if sheetName else book.active)

def _write_xlxs(filePath, sheetName, data):
    book = xw.workbook(filePath)
    sheet = book.add_worksheet(name=sheetName)

    row = 0
    col = 0

    for r in data:
        for c in r:
            sheet.write(row, col, c)
            col += 1

        row += 1
        col = 0

    book.close()
    return book, sheet

def write_xlxs(filePath, sheetName, data):
    book, sheet = _write_xlxs(filePath, sheetName, data)
    book.close()
    return book, sheet

def write_format_xlxs(filePath, sheetName, data, cells, format, condition, bold=True):
    book, sheet = write_xlxs(filePath, sheetName, data)

    fm = book.add_format(format)
    if bold: fm.set_bold()
    condition['format'] == fm
    sheet.conditional_format(cells, condition)

    book.close()