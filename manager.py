from datetime import datetime
import csv

headers = ['Date', 'Category', 'Amount', 'Description']

def firstcsv():
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
def writecsv(date, category, amount, description):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def readcsv():
    with open('expenses.csv', 'r', encoding='utf-8') as read_file:
            reader = csv.reader(read_file)
            rows = list(reader)
            header = rows[0]
            data = rows[1:] 
            return data , header

def datefilter(data,header):
    sorted_data = sorted(data, key=lambda row: datetime.strptime(row[0], "%Y-%m-%d"))
    print(','.join(header))
    for row in sorted_data:
        print(','.join(row))

def catfilter(data, header):
    category_filter = input("Enter category to filter: ")
    filtered = [row for row in data if row[1].lower() == category_filter.lower()]
    print(','.join(header))
    for row in filtered:
        print(','.join(row))
        
    