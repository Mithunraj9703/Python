# with open("demo.txt","r") as f:
#     data=f.read()

# if(data.find("learning")!=-1):
#     print("found")
# else:
#     print("not found")

def word_line():
    word="learning"
    data=True
    line_no=1
    with open("demo.txt","r") as f:
        while data:
            data=f.readline()
            if(data.find(word)!=-1): #if(word in data):
                print(line_no)
                return
            else:
                line_no+=1
        print(-1)    
word_line()