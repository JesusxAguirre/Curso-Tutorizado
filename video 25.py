#trabajando con archivos

import csv
with open('inventario.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print('-'.join(row))