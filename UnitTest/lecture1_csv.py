import csv

def read_csv1(filePath):
    f = open(filePath, 'rt')
    reader = csv.reader(f)
    data = list(reader)
    f.close()
    return data

def read_csv2(filePath):
    f = open(filePath, 'rt')
    reader = csv.DictReader(f)
    data = list(reader)
    f.close()
    return data

def write_csv(filePath, names, grades):
    f = open(filePath, 'wt')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('Sr.', 'Names', 'Grades'))
    for i in range(len(names)):
        writer.writerow((i+1, names[i], grades[i]))

    f.close()

def write_tsv(filePath, names, grades):
    f = open(filePath, 'wt')
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    writer.writerow(('Sr.', 'Names', 'Grades'))
    for i in range(len(names)):
        writer.writerow((i+1, names[i], grades[i]))

    f.close()

def csv_dialect(filePath):
    csv.register_dialect('pipes', delimiter='-')
    with open(filePath, 'rt') as f:
        reader = csv.DictReader(f, dialect='pipes')
        return list(reader)

def manage_ca_employees(filePathOpened, filePathWritten):
    fr = open(filePathOpend, 'rt')
    fw = open(filePathWritten, 'wt')

    reader = csv.DictReader(fr)
    writer = csv.writer(fw, lineterminator='\n')

    data = list(reader)
    for e in data:
        if e['state'] == 'CA':
            csvWriter.writerow((e['email'], e['phone']))
    
    fr.close()
    fw.close()


        