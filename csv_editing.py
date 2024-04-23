import csv

with open('movie.csv', 'r', newline='') as csv_file:
    spamreader = csv.reader(csv_file, delimiter=' ', quotechar='|')

    print(spamreader)
