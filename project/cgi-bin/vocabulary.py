#!/usr/bin/env python3
import cgi
# -*- codecs: utf-8 -*-
import codecs

form = cgi.FieldStorage()
text2 = form.getfirst("TEXT_2", "не задано")
text3 = form.getfirst("TEXT_3", "не задано")


print("Content-type: ttext/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

text = text2.split()

q = []
for i in text:
    q1 = list(i)
    q.append(q1)


first_letter = text[0][0]

tire ="-"

f = codecs.open("D:\Baza\%s.txt"%first_letter, "a", "utf-8")


f.write('\n')
word = []
word.append(text2)
word.append(tire)
word.append(text3)

f.write(' '.join(word))
f.close()



f.write("11111111111111111111111111111111111")
f.close()


print("<h1>Исправление успешно добавлено!</h1>")
print("<p>Исправленный текст: {}</p>".format(text2))


print("""</body>
        </html>""")