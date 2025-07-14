import csv

unique_rows = set()

def clean_row(row):
    return tuple(cell.strip() for cell in row)

def read_csv_to_set(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            cleaned = clean_row(row)
            unique_rows.add(cleaned)

read_csv_to_set('rmc.csv')
read_csv_to_set('rmc2.csv')

with open('unique_rows.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in unique_rows:
        writer.writerow(row)
