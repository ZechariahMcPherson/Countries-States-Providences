import csv
import sys
import os

"""
    error handling for for creating a file
"""
def createFile(create, option):

    try:
        file = open(create, option,  newline='', encoding='utf-8')
        return file

    except OSError:
        print ("Error: could not create " + create)
        sys.exit()

"""
    error handling for opening a file
"""
def openFile(openFile):
    try:
        file = open(openFile, newline='', encoding='utf-8')
        return file

    except OSError:
        print ("Error: could not open " + openFile)
        sys.exit()

"""
    converts txt to csv for countryInfo.txt

    online src file:
    http://download.geonames.org/export/dump/countryInfo.txt
"""
def countryInfoTxt2Csv(destination, source, removeComments):

    #creates csv file and a writer to write to that file
    newCsv = createFile(destination, 'wt')
    newCsvWriter = csv.writer(newCsv, delimiter=',',
      quotechar='"', quoting=csv.QUOTE_ALL)

    #opens data file and creates a reader for that file
    dataTxt  = openFile(source)
    dataTxtReader = csv.reader(dataTxt, delimiter='\t')

    for row in dataTxtReader:

        #comment rows start with #
        if(row[0][0] != "#"):
            line = []

            #trims extra whitespaces
            for col in row:
                #print(row[0][0])
                #print(row)
                line.append(col.strip(' \t\n\r'))

            newCsvWriter.writerow(line)

    newCsv.close()
    dataTxt.close()


"""
    converts txt to csv for admin1admin1CodesASCII.txt

    online src file:
    http://download.geonames.org/export/dump/admin1CodesASCII.txt
"""
def admin1CodesASCIITxt2Csv(destination, source):

    #creates csv file and a writer to write to that file
    newCsv = createFile(destination, 'wt')
    newCsvWriter = csv.writer(newCsv, delimiter=',',
      quotechar='"', quoting=csv.QUOTE_ALL)

    #opens data file and creates a reader for that file
    dataTxt  = openFile(source)
    dataTxtReader = csv.reader(dataTxt, delimiter='\t')

    for row in dataTxtReader:

        line = []

        #trims extra whitespaces
        for col in row:
            line.append(col.strip(' \t\n\r'))

        newCsvWriter.writerow(line)


"""
    controls flow of parser
"""
def main():

    #ensures folder for storing clean data exists
    if(not os.path.exists('./cleanDATA')):
        os.makedirs('./cleanDATA')

    #ensures that the folder storing the source data exists
    if(not os.path.exists('./srcDATA')):
        print("Error: srcDATA folder is missing")
        sys.exit()

    countryInfoTxt2Csv('./cleanDATA/countryInfo.csv', './srcDATA/countryInfo.txt', False)

    admin1CodesASCIITxt2Csv('./cleanDATA/admin1CodesASCII.csv', './srcDATA/admin1CodesASCII.txt')

main()
