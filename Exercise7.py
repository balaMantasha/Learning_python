#Write a program to clear the clutter inside a folder on your computer.
#You should use OS module to rename all the png images from 1.png all the 
#way till n.png where n is the numbe of png files in that folder.
#Do the same for other file formats
import os
files = os.listdir("Cluttered")
i =1
for file in files:
    if file.endswith(".jpg"):
      print(file)
      os.rename(f"Cluttered/{file}",f"Cluttered/{i}.jpg")
      i = i +1
