import csv


def parseFile(parseToFile, fileToParse):
    with open(parseToFile, 'wt',  newline='') as csvfile:
        spamwriter = csv.writer(csvfile,
          quotechar='|', quoting=csv.QUOTE_MINIMAL)

        with open(fileToParse, newline='') as csvfile2:
             spamreader = csv.reader(csvfile2, delimiter='\t', quotechar='|')
             for row in spamreader:
                 spamwriter.writerow(row)
                 print(row)



def main():

    parseFile('test.csv','../Data/countryInfo.txt' )


main()
