list=["a","b","c","d"]
def list_element(list,i=0):
    if(i==len(list)):
        return
    print(list[i])
    list_element(list,i+1)
list_element(list)