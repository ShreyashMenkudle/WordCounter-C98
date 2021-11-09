def countWordsFromFile():
    fileName= input("Enter your file name:-")
    wordCount=0
    file= open(fileName,'r')
    
    for line in file:
        words = line.split()
        print(words)
        wordCount = wordCount+ len(words)

    print("Number of words:-",wordCount)

countWordsFromFile()