import csv
import sys

"""
    error handling for for creating a file
"""
def createFile(create):

    try:
        file = open(create, 'wt',  newline='', encoding='utf-8')
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
    newCsv = createFile(destination)
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

            spamwriter.writerow(line)

    newCsv.close()
    dataTxt.close()

"""
    controls flow of parser
"""
def main():

    countryInfoTxt2Csv('./cleanDATA/countryInfo.csv', './srcDATA/countryInfo.txt', False)

main()
