import csv
def read_file_csv(filename): 
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        a=[]
        for i in csv_reader:
            for j in i:
                a.append(j.split(';'))
    return a
        