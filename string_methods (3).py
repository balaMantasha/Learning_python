# -*- coding: utf-8 -*-
"""String Methods

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11IwLfCFwJYzr2MjNqh3PhPSvTw8xAEyj
"""

a='!!!!!sADAF!!! 1111'
print(a)
print(len(a))
print(a.lower())
print(a.upper())
print(a.rstrip('!'))
print(a.replace('sADAF', 'Peerzada'))
print(a.split(" "))
print(a.capitalize())
b="peerzada sadaf sadaf ajaz baba"
print(b.capitalize())
print(b.center(75))
print(len(b.center(75)))
print(len(b))
print(b.count("sadaf"))
print(b.endswith("!!!"))
print(b.endswith("a",5,6))
print(b.find('e'))
print(b.find("q"))
#print(b.index("q"))
#index throws error if not present in the variable
print(b.isalnum()) #alphabets and number
c="sadaf12"
print(c.isalnum())
print(c.isalpha()) #only alphabets
string='New to python' #will give false if any letter is in upper case
print(string.islower())
print(string.isprintable())
D="sadaf\n"
print(D.isprintable())
string1="        "     #using space bar
string2="             " #using tab
print(string1.isspace())
print(string2.isspace())
#istitle() returns T only if the first letter of every word is capitalized
abc="Sadaf Is Learning Python"
abcd="Sadaf IS Learning 123"
abcde="Sadaf is learning python"
print(abc.istitle())
print(abcd.istitle())
print(abcde.istitle())
print(abcde.isupper())
q='123'
print(q.isupper())
print(q.startswith('1'))
print(abcd.swapcase())
Task="Python is an interpreted language"
print(Task.title())


