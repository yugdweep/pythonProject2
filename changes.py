from bs4 import BeautifulSoup
import requests
from csv import DictReader,DictWriter,writer,reader
import csv

rows = []
with open('file2.csv', 'r', newline='') as rf:
    csv_reader = DictReader(rf)
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row['TITLE'])

    print(f"Title is ----> {rows}  \n Sorted title is ----> {sorted(rows)}")
