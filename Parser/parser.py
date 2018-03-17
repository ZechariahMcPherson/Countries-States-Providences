import csv
import sys

#error handling for for creating a file
def createFile(create):

    try:
        file = open(create, 'wt',  newline='', encoding='utf-8')

    except OSError:
        print "Error: could not create ", create
        sys.exit()

#error handling for opening a file
def openFile(open):
    try:
        file = open(open, 'wt',  newline='', encoding='utf-8')

    except OSError:
        print "Error: could not open ", open
        sys.exit()






def main():


main()
