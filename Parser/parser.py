import csv
import sys
import os
import json

from pprint import pprint

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
    dataCsv  = openFile(source)
    dataCsvReader = csv.reader(dataCsv, delimiter=',')

    for row in dataCsvReader:
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
    dataCsv.close()

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
    dataCsv  = openFile(source)
    dataCsvReader = csv.reader(dataCsv, delimiter=',')

    for row in dataCsvReader:
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

    #closed open files
    newCsv.close()
    dataCsv.close()





"""
    takes filteredCountryInfo.csv and converts it to countryInfo.json

    this json format is validated by https://jsonlint.com/ they are awesome!
"""
def countryInfoCsv2Json(source, destination):

    #creates csv file and a writer to write to that file
    newJson = createFile(destination, 'wt')

    #opens data file and creates a reader for that file
    dataCsv  = openFile(source)
    dataCsvReader = csv.reader(dataCsv, delimiter=',')


    #opens json object array
    newJson.write("[\n")

    for row in dataCsvReader:

        data = {'ISO' : row[0], 'ISO3' : row[1], 'CountryName' : row[2],
            'GeonameId' : row[3]}

        json.dump(data, newJson, indent=4)

        #adds comman and new line after each json object
        newJson.write(",\n")

    """
    removes extra comma from the end of the last json object
        and closes json array
    """
    pos = newJson.tell()
    newJson.seek(pos-3)
    newJson.write("}\n]")

    #closed open files
    newJson.close()
    dataCsv.close()


"""
    takes filteredAdmin1CodesASCII.csv and converts it to
        adminCodes.json

    Note: Currently I only have United State's state ISOs in the json
        other states and provinces of the world do not have their ISOs listed

    this json format is validated by https://jsonlint.com/ they are awesome!
"""
def adminCodesCsv2Json(source, destination):

    #creates csv file and a writer to write to that file
    newJson = createFile(destination, 'wt')

    #opens data file and creates a reader for that file
    dataCsv  = openFile(source)
    dataCsvReader = csv.reader(dataCsv, delimiter=',')


    #opens json object array
    newJson.write("[\n")

    for row in dataCsvReader:

        data = {'CountryISO' : row[0], 'StateISO' : row[1], 'StateProvince' : row[2], 'GeonameId' : row[3]}

        json.dump(data, newJson, indent=4)

        #adds comman and new line after each json object
        newJson.write(",\n")

    """
    removes extra comma from the end of the last json object
        and closes json array
    """
    pos = newJson.tell()
    newJson.seek(pos-3)
    newJson.write("}\n]")

    #closed open files
    newJson.close()
    dataCsv.close()



"""
    takes filteredAdmin1CodesASCII.csv and converts it to
        adminCodes.json

    Note: Currently I only have United State's state ISOs in the json
        other states and provinces of the world do not have their ISOs listed

    this json format is validated by https://jsonlint.com/ they are awesome!
"""
def createCountryAndStatesJson(countryInfoPath, adminCodesPath,
    countriesAndStatesPath):

    #creates csv file and a writer to write to that file
    #newJson = createFile(countriesAndStatesJson, 'wt')

    #opens data file and creates a reader for that file
    #countryJson  = openFile(countryInfoJson)

    #opens data file and creates a reader for that file
    #statesJson  = openFile(adminCodesJson)

    countriesAndStatesFile = createFile(countriesAndStatesPath, 'wt')

    countryInfoFile = openFile(countryInfoPath)

    countryInfoData = json.load(countryInfoFile)

    adminCodesFile = openFile(adminCodesPath)

    adminCodesData = json.load(adminCodesFile)

    #opens json object array
    countriesAndStatesFile.write("[\n")

    for rowCountryInfo in countryInfoData:

        #object array of all of the states associated with the country
        statesList = []
        '''
        data = {'ISO' : rowCountryInfo['ISO'], 'ISO3' : rowCountryInfo['ISO3'], 'CountryName' : rowCountryInfo['ISO3'], 'GeonameId' : rowCountryInfo['GeonameId']}
        '''

        #json.dump(data,countriesAndStatesFile, indent=4)

        for rowAdminCodes in adminCodesData:

            #if the country has a state
            if(rowCountryInfo['ISO'] == rowAdminCodes['CountryISO']):

                statesList.append(
                {'CountryISO' : rowAdminCodes['CountryISO'], 'StateISO' : rowAdminCodes['StateISO'], 'StateProvince' : rowAdminCodes['StateProvince'], 'GeonameId' : rowAdminCodes['GeonameId']})


        statesList.sort(key=lambda x: x['StateProvince'])

        data = {'ISO' : rowCountryInfo['ISO'], 'ISO3' : rowCountryInfo['ISO3'], 'CountryName' : rowCountryInfo['CountryName'], 'GeonameId' : rowCountryInfo['GeonameId'], 'States' : statesList.copy()}

        #write state object array into country object
        #stateData = statesList.copy()

        json.dump(data,countriesAndStatesFile, indent=4)

        countriesAndStatesFile.write(',\n')

    pos = countriesAndStatesFile.tell()
    countriesAndStatesFile.seek(pos-3)
    countriesAndStatesFile.write("}\n]")



    #print(data[0])

    #opens json object array
    '''
    newJson.write("[\n")

    for row in dataCsvReader:

        data = {'CountryISO' : row[0], 'StateISO' : row[1], 'StateProvince' : row[2], 'GeonameId' : row[3]}

        json.dump(data, newJson, indent=4)

        #adds comman and new line after each json object
        newJson.write(",\n")

    '''

    """
    removes extra comma from the end of the last json object
        and closes json array
    """
    '''
    pos = newJson.tell()
    newJson.seek(pos-3)
    newJson.write("}\n]")

    '''

    #closed open files
    countryInfoFile.close()
    adminCodesFile.close()
    countryInfoFile.close()


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

    """
    countryInfoTxt2Csv('./srcDATA/countryInfo.txt', './csvDATA/countryInfo.csv', False)

    admin1CodesASCIITxt2Csv('./srcDATA/admin1CodesASCII.txt', './csvDATA/admin1CodesASCII.csv')

    filterCountryInfo('./csvDATA/countryInfo.csv', './DATA/filteredCountryInfo.csv')

    filterAdmin1CodesASCII('./csvDATA/admin1CodesASCII.csv', './DATA/filteredAdmin1CodesASCII.csv')


    countryInfoCsv2Json('./DATA/filteredCountryInfo.csv', './DATA/countryInfo.json')

    adminCodesCsv2Json('./DATA/filteredAdmin1CodesASCII.csv', './DATA/adminCodes.json')
    """

    createCountryAndStatesJson('./DATA/countryInfo.json',
        './DATA/adminCodes.json', './DATA/countriesAndStates.json')



main()
