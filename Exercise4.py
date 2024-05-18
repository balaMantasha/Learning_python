# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.
#coding:
#if the word contains atleast 3 characters, remove the first letter and append it at the end
#now append three random characters at the starting and the end
#else:
#simply reverse the string

#Decoding:
#if the word contains less than 3 characters, reverse it
#else:
#remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.
st = input("Enter message")
words = st.split(" ")
coding = True
if(coding):
    nwords = []
    for word in words:
     if (len(word)>=3):
        r1 = "sss"
        r2 = "bbb"
        stnew = r1+words[1:] + words[0]+r2
        nwords.append(stnew)
        print(stnew)
    else:
       print("sss")
else:
 pass