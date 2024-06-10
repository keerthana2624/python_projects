def loadData(filename):
    d=""
    file=open("quizfile.txt","r")
    #print(file.readlines())
    for i in file.readlines():
        d+=i
    return d
x=loadData('questions.txt')



def parseQuestions(data):
    l=[]
    lines=data.split("\n")
    # print(lines)
    for i in lines:
        d={}
        s=i.split(":")
        # print(s)
        d["question_text"]=s[0]
        d["choices"]=s[1].split(",")
        d["correct_option"]=int(s[2])
        d["max_marks"]=int(s[3])
        d["penalty"]=int(s[4])
        l.append(d)
    # print(l)  
    return l 
y=parseQuestions(x)



