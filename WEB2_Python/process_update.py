#!C:\Users\LJC\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opend_file = open('data/'+pageId, 'w')
opend_file.write(description)
opend_file.close()

os.rename('data./'+pageId, 'data./'+title)

print("Location: index.py?id="+title)
print()
