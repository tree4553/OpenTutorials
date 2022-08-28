#!C:\Users\LJC\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type: text/html")
print()

import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    description = open('data/' + pageId, 'r', encoding="utf-8").read()
    #description = description.replace('<', '&lt;')
    #description = description.replace('>', '&gt;')
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        <form>
    '''.format(pageId)
else:
    title = pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
print('''<!doctype html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <h2><a href="../index.html">HOME</a></h2>
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
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(
title=title,
desc=description,
listStr=view.getList(),
update_link=update_link,
delete_action=delete_action))
