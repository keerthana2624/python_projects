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


def startQuiz(questions):
    # print(questions)
    for d in questions:
        # print(i)
        print(d["question_text"])
        print(" ".join(d["choices"]))   
        n = int(input(" enter the choice(1/2/3/4):"))
        d["user_choice"]=n
        if n==int(d["correct_option"]):
            d["score"]=d["max_marks"]
        else:
            d["score"]=d["penalty"]
   
    return questions
z=startQuiz(y)

def scoreReport(questions):
    totalScore=0
    for d in questions:
        if d["correct_option"]==d["user_choice"]:
            print("correct Answer!- ", d["max_marks"])
            totalScore+=d["score"]
        else:
            print("Wrong answer! -",d["penalty"])
            totalScore+=d["score"]
    return totalScore
print(scoreReport(z))









