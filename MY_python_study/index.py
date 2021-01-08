#!D:\PYTHON\python.exe

print("content-type: text/html; charset=utf-8\n") #header
print()
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print(pageId) 
print('''
<!DOCTYPE html>
<html lang="ko">
    <head>
        <title>COTTON CODE</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet"
    </head>
    <body>
    <h1>
        <a href="index.py?id=Home">
            {title}
        </a>
    </h1>
    <ul style="list-style: none;">
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    </ul>    
        
    </body>
</html>
'''.format(title='COTTON CODE'))
