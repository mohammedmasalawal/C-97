introString=input("enter a string:")
characterCount=0
wordCount=1
for i in introString:
    characterCount+=1
    if(i==" "):
        wordCount+=1
print("number of words in the string:")
print(wordCount)
print("number of Characters in the string:")
print(characterCount)