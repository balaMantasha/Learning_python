# -*- coding: utf-8 -*-
"""f-strings

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GpCoLQtAugHo6sf_tACPvWS6bDgDh4gC
"""

#f-string is used for string formating
letter = "hey my name is {} and I am from {}"
country= "India"
name = "Sadaf"

print(f'hey my name is {name} and I am from {country}')
print(f'hey my name is {{name}} and I am from {{country}}')

txt = "For only {} dollars"
price= "2.00009"
print(f'For only {price} dollars') #confusion