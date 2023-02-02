import csv
with open('Posts.csv', 'r', newline='',encoding="utf-8") as csvfile:
    postreader = csv.reader(csvfile, delimiter=',', 
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for row in postreader:
      print("-".join(row))
      print("")