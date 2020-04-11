import csv

l = []
for i in range(0, 15625):
    l.append(i)

with open("data.csv", 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(l)

csvFile.close()