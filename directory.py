import os

# PathList from user store here
pathList= []
# All found files store here
files = []

numberOfQueries = int(input("Which number of directories are you want to search? "))

for quesSearch in range(numberOfQueries):
    dirctoryInput = input('Enter your desired directory: ')
    pathList.append(dirctoryInput)
    for eachPath in pathList:
        for dirPath, dirName, fileName in os.walk(eachPath):
            for file in fileName:
                if '.' in file:
                    files.append(os.path.join(dirPath, file))

        for allFiles in files:
            print(allFiles)