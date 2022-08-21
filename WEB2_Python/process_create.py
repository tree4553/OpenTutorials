#!C:\Users\LJC\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opend_file = open('data/'+title, 'w')
opend_file.write(description)

print("Location: index.py?id="+title)
print()
