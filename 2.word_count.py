from collections import Counter #import Counter from collections module
print("filename or path")
path=str(input())               #taking input of name of path
file=open(path)                 #opening path
data=file.read()                #read file
word=Counter(data.split())      #count words in the file and stored as dictionary values
for i in word:
    print(i,':',word[i])        #print words and count of their occurence
file.close()    
