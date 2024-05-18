# -*- coding: utf-8 -*-
"""Exercise_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IINdSuKwAU0aWATApZRJE9es5xsfzN8h
"""

#Take string as an input
#Coding:If the word contains atleast 3 characters,remove the first letter and
#append it at the end and now append random 3 charc. at the start & end
# else:simply reverse string
#decoding:If the word contains less than 3 characters,reverse it
#else:
#remove 3 random characters from start and end.Now remove the last letter
#add last letter to the beginning


st = input("Enter the string: ")
words = st.split(" ")
coding = input("Enter (1) for Coding and (2) for Decoding: ")
coding = True if coding == "1" else False

nwords = []

for word in words:
    if len(word) >= 3:
        if coding:
            r1 = "pqr"
            r2 = "xyz"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
    else:
        nwords.append(word[::-1])

print(" ".join(nwords))