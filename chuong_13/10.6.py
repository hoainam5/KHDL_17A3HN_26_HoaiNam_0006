import csv

def write_csv_file(filename, listContent):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(listContent)

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

phone_list = [
    ["name", "fone"],
    ["Jonny", "0989 753951"],
    ["Jack", "0913 123456"],
    ["Lucy", "0913 753951"],
    ["Johnny Lee", "0913 753852"],
    ["Peter Son", "0989 753951"],
    ["Johnathan", "0903 123456"]
]

write_csv_file('dienthoai.csv', phone_list)

read_csv_file('dienthoai.csv')

