def initializeplatform():
    platform=[]
    return platform
# print(initializeplatform())

def creat_post(platform,content):
        new_post={}
        new_post["content"]=content
        new_post["likes"]=0
        new_post["comments"]=[]
        platform.append(new_post)
        return platform
# platform=initializeplatform()
# content="name"
# print(creat_post(platform,content))

def viewtimeline(platform):
    for post in platform:
        dic={"post_name":post["content"],
              "no_of_likes":post["likes"],
              "comments":post["comments"]}
        print(dic)
# platfrom=initializeplatform()
# p=creat_post(platfrom,content="hello")
# print(viewtimeline(p))

def like_post(platform,postindex):
        if postindex>=len(platform) or postindex < 0:
            print("Warning! list out of index")
            return
        else:
            platform[postindex]["likes"]+=1
        return platform
# platform=initializeplatform()
# platfrom=initializeplatform()
# p=creat_post(platfrom,content="hello")
# print(like_post(p,0))


def commenton_post(platform,Postindex,comment):
    if Postindex>=len(platform) or Postindex<0:
        print("warning! list the index")
    else:
        platform[Postindex]["comments"].append(comment)
    return platform
# platform=initializeplatform()
# platform = creat_post(platform, content="hello")
# comment = "it looks nice"
# postindex = 0
# print(commenton_post(platform,postindex,comment))

def startPlatform():
    platform=initializeplatform()
    print(platform)
    while True:

        print("a >> creat new post: ")
        print("b >> view the time line: ")
        print("c >> like a post: ")
        print("d >> comment on a post: ")
        print("e >> exit: ")

        user_input=input("enter your choice: ")
        if user_input=="a":
            content=input("enter your content name: ")
            platform=creat_post(platform,content)

        if user_input=="b":
             viewtimeline(platform)

        if user_input=="c":
            postindex=int(input("like your post as index: "))
            platform=like_post(platform,postindex)

        if user_input=="d":
            index=int(input("enter your index to add comment: "))
            comment=input("add your comment ")
            platform=commenton_post(platform,index,comment)

        if user_input=="e":
            print("closed!")
            break

startPlatform()
                      





