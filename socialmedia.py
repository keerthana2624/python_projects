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






