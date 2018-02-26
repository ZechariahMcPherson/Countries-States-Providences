import csv


#takes countryInfo text file from geonames and makes csv
def parseCountriesTxt(newFile, dataFile):
    with open(newFile, 'wt',  newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
          quotechar='"', quoting=csv.QUOTE_ALL)

        with open(dataFile, newline='', encoding='utf-8') as csvfile2:
             spamreader = csv.reader(csvfile2, delimiter='\t')
             for row in spamreader:
                 if(spamreader.line_num == 81):
                    print(row)
                 #rows that don't contain data start with #
                 if(row[0][0] != "#"):
                     #print(row[0][0])
                     #print(row)
                     spamwriter.writerow(row)

#takes the countryInfo csv and pulls specific columns
def parseCountriesCsv(newFile, dataFile):
    with open(newFile, 'wt',  newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
          quotechar='"', quoting=csv.QUOTE_ALL)

        with open(dataFile, newline='') as csvfile2:
             spamreader = csv.reader(csvfile2)
             for row in spamreader:
                 if(spamreader.line_num == 30):
                     print(row)
                     print(row[4])
                 #row[0] - ISO
                 #row[1] - ISO3
                 #row[4] - country name
                 #row[16] - geoID assigned by geonames
                 line = [row[0], row[1], row[4], row[16]]
                 #print(line)
                 spamwriter.writerow(line)


def main():
    parseCountriesTxt('test.csv','../DATA/countryInfo.txt')
    parseCountriesCsv('testFilter.csv', './test.csv')
main()
