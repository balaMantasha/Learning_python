# -*- coding: utf-8 -*-
"""Enumerate function

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Ghhp3l8iAK-8LKEwT0vT1KWxXs4fMXY
"""

marks = [12,56,32,98,12,45,1,4]
index = 0
for mark in marks:
  print(mark)
  if(index ==3):
    print("Sadaf's marks")
  index +=1

marks = [12,56,32,98,12,45,1,4]
for index, mark in enumerate(marks,start=1):
  print(mark)
  if(index ==3):
    print("Sadaf's marks")