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
def countryInfoTxt2Csv(source, destination, removeComments):

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

    #closed open files
    newCsv.close()
    dataTxt.close()



"""
    converts txt to csv for admin1admin1CodesASCII.txt

    online src file:
    http://download.geonames.org/export/dump/admin1CodesASCII.txt
"""
def admin1CodesASCIITxt2Csv(source, destination):

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

    #closed open files
    newCsv.close()
    dataTxt.close()

"""
    filters countryInfo.csv for ISO, ISO3, country name and geonameid
"""
def filterCountryInfo(source, destination):

    #creates csv file and a writer to write to that file
    newCsv = createFile(destination, 'wt')
    newCsvWriter = csv.writer(newCsv, delimiter=',',
      quotechar='"', quoting=csv.QUOTE_ALL)

    #opens data file and creates a reader for that file
    dataTxt  = openFile(source)
    dataTxtReader = csv.reader(dataTxt, delimiter=',')

    for row in dataTxtReader:
        line = []

        try:
            #row[0] ISO
            #row[1] ISO3
            #row[4] country name in English
            #row[16] geonameid
            line.append(row[0])
            line.append(row[1])
            line.append(row[4])
            line.append(row[16])
        except IndexError:
            line = null

        newCsvWriter.writerow(line)



    #closed open files
    newCsv.close()
    dataTxt.close()

"""
    filters admin1CodesASCII.csv for:
    country ISO: two letters be for '.' stored in column 0
    state/province two digit code: just gathering this for US
    english name: for state/province
    geonameid: for the state/province
"""
def filterAdmin1CodesASCII(source, destination):

    #creates csv file and a writer to write to that file
    newCsv = createFile(destination, 'wt')
    newCsvWriter = csv.writer(newCsv, delimiter=',',
      quotechar='"', quoting=csv.QUOTE_ALL)

    #opens data file and creates a reader for that file
    dataTxt  = openFile(source)
    dataTxtReader = csv.reader(dataTxt, delimiter=',')

    for row in dataTxtReader:
        line = []

        #splits "US.SC" into ["US","SC"]
        colOne = row[0].split('.')


        #if "US.SC" write "US","SC"
        if(colOne[0] == "US"):
            line.append(colOne[0])
            line.append(colOne[1])

        #if not us state write "AZ",""
        else:
            line.append(colOne[0])
            line.append("")

        #english state/province name
        line.append(row[2])

        #geonameid for state/province
        line.append(row[3])


        newCsvWriter.writerow(line)


"""
    controls flow of parser
"""
def main():

    #ensures that the folder storing the source data exists
    if(not os.path.exists('./srcDATA')):
        print("Error: srcDATA folder is missing")
        sys.exit()

    #ensures folder for storing clean data exists
    if(not os.path.exists('./csvDATA')):
        os.makedirs('./csvDATA')

    #ensures folder for storing finalized DATA exists
    if(not os.path.exists('./DATA')):
        os.makedirs('./DATA')


    countryInfoTxt2Csv('./srcDATA/countryInfo.txt', './csvDATA/countryInfo.csv', False)

    admin1CodesASCIITxt2Csv('./srcDATA/admin1CodesASCII.txt', './csvDATA/admin1CodesASCII.csv')

    filterCountryInfo('./csvDATA/countryInfo.csv', './DATA/filteredCountryInfo.csv')

    filterAdmin1CodesASCII('./csvDATA/admin1CodesASCII.csv', './DATA/filteredAdmin1CodesASCII.csv')

main()
