import csv

def helper(word,file):
    file.write(word)
    file.write("\n")

with open('dev-key.csv') as csv_file:
    file = open('correct_output.txt', 'w+')
    csv_reader = csv.reader(csv_file,delimiter = ',')
    for row in csv_reader:
        helper(row[1],file)