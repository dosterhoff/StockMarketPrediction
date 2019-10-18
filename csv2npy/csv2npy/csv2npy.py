import numpy as np
import csv

#Creates a variable named filename. It then asks the user to input the name of the file contianing the data. The user enters the data and the program will then
    #append the .csv extension to the file name. This makes it easier for the user.
filename = input('Enter name of the file (only enter file name. .csv is added automatically): ') + '.csv'  

#Defines a function to read the file
def readMyFile(filename):
    
    AdjClose = []   #creates an empty array

    try:    #the TRY function will prevent the program from opening nonexistent files.
        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            next(csvReader) #this skips the first line, which is the header in this case.
            for row in csvReader:
                AdjClose.append(row[5]) #row(5) will get the data from each row in column 5 (adjusted close)
                #scores.append(row[1])
    except:
        print('The file doesnt exist. Please exit and run the program again.')
        exit(0,99)

    return AdjClose

AdjClose = readMyFile(filename)
print(AdjClose)

SaveType= input('Do you wish to specify a file name? (selecting no will automatically save the files as test_data.npy and train_data.npy) y/n: ') #savetype exists so that we have the option of saving the files automatically for use with the agent, or we can specify a unique name to keep track of things.

if SaveType == 'y':
    saveFilename = input('Save Array as: ')
    np.save(saveFilename, AdjClose)

else:
    print('saving test_data and train_data files')
    np.save('test_data', AdjClose)
    np.save('train_data', AdjClose)
    print('files have been saved in this programs directory')

