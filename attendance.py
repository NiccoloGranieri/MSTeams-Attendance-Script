import csv
import pprint

with open ('attendance.csv', newline='', encoding="utf16") as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        print(row['Full Name'], row['User Action'], row['Timestamp'])
