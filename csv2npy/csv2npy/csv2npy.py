import numpy as np
import csv

def readMyFile(filename):
    filename = input('Enter name of the file (only enter file name. .csv is added automatically): ') + '.csv'  
    
    AdjClose = []

    try:
        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                AdjClose.append(row[0])
                #scores.append(row[1])
    except:
        print('The file doesnt exist. Please exit and run the program again.')
        exit(0,99)

    return AdjClose

AdjClose = readMyFile('BAcsv.csv')
print(AdjClose)

SaveType= input('Do you wish to specify a file name? (selecting no will automatically save the files as test_data.npy and train_data.npy) y/n: ')

if SaveType == 'y':
    saveFilename = input('Save Array as: ')
    np.save(saveFilename, AdjClose)

else:
    print('saving test_data and train_data files')
    np.save('test_data', AdjClose)
    np.save('train_data', AdjClose)
    print('files have been saved in this programs directory')

