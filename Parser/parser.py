import csv
import sys

#error handling for for creating a file
def createFile(create):

    try:
        file = open(create, 'wt',  newline='', encoding='utf-8')
        return file

    except OSError:
        print "Error: could not create ", create
        sys.exit()


#error handling for opening a file
def openFile(open):
    try:
        file = open(open, 'wt',  newline='', encoding='utf-8')
        return file
        
    except OSError:
        print "Error: could not open ", open
        sys.exit()

#converts txt to csv for countryInfo.txt
def countryTxt2Csv(destination, source):

    #creates csv file and a writer to write to that file
    newCsv = createFile(destination)
    newCsvWriter = csv.writer(newCsv, delimiter=',',
      quotechar='"', quoting=csv.QUOTE_ALL)

    #opens data file and creates a reader for that file
    dataTxt  = openFile(source)
    dataTxtReader = csv.reader(dataTxt, delimiter='\t')



def main():


main()
