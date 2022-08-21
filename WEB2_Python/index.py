#!C:\Users\LJC\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type: text/html")
print()

import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/' + pageId, 'r', encoding="utf-8").read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
print('''<!doctype html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        <!---
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</a></li>
        <li><a href="index.py?id=Python">Python</a></li>
        --->
        {listStr}
    </ol>
    <a href="create.py">create</a>
    {update_link}
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link))
