import csv

def main():


    with open('test.csv', 'wt', newline='') as csvfile:
        spamwriter = csv.writer(csvfile,
          quotechar='|', quoting=csv.QUOTE_MINIMAL)
        print("hi")

        with open('../Data/countryInfo.txt', newline='') as csvfile2:
             spamreader = csv.reader(csvfile2, delimiter='\t', quotechar='|')
             for row in spamreader:
                 spamwriter.writerow(row)
                 print(row)


main()
