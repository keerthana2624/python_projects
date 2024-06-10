def loadData(filename):
    d=""
    file=open("quizfile.txt","r")
    #print(file.readlines())
    for i in file.readlines():
        d+=i
    return d
x=loadData('questions.txt')

