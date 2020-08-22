# -*- codecs: utf-8 -*-
import codecs
import copy
import enchant
from enchant.checker import SpellChecker


a = input("")

text = a.split()

q = []
for i in text:
    q1 = list(i)
    q.append(q1)

i = 0

try:
    while i != len(text):
        i_1 = 0
        replacement = 0
        first_letter = text[i][0]
        f = codecs.open("D:\Baza\%s.txt"%first_letter, "r", "utf-8")
        fd = f.readlines(0)

        while i_1 != len(fd) and replacement != 1:
            list1 = fd[i_1].split()

            if list1[0].lower() == text[i].lower() or list1[2].lower() == text[i].lower():

                text[i] = list1[2]
                replacement = 1

            i_1 += 1

        if replacement == 0:

            i_1 = 0
            i_2 = 0
            delt = []

            text_copy = []

            while i_2 != len(text[i]):
                text_copy.append(text[i][i_2])
                i_2 += 1
                i_3 = len(text_copy)
            while i_3 != 0 and replacement != 1:
                delt.append(text_copy[len(text_copy) - 1])
                text_copy.pop()
                myString = ''.join(text_copy)
                i_1 = 0

                while i_1 != len(fd) and replacement != 1:
                    list1 = fd[i_1].split()

                    if list1[0].lower() == myString.lower()  or list1[2].lower() == myString.lower():

                        word = []
                        word.append(list1[2])
                        if delt != 0:
                            while len(delt) != 0:

                                word.append(delt[len(delt) - 1])
                                delt.pop()

                        text[i] = ''.join(word)
                        replacement = 1

                    i_1 += 1
                i_3 -= 1

        i += 1
except:
    i += 1

try:
    a = (' '.join(text))
    chkr = enchant.checker.SpellChecker("ru_RU")
    chkr.set_text(a)

    for err in chkr:
        sug = err.suggest()[0]
        err.replace(sug)

    text_total = chkr.get_text()
    print(text_total)
except:
    text_total = print(' '.join(text))

text = text_total.split()
q = []
for i in text:
    q1 = list(i)
    q.append(q1)
hesh = []
i = 0
while i != len(text):
    if len(text[i]) >= 7:

        if text[i][0].lower() == "и" and text[i][1].lower() == "н":
            f = codecs.open("D:\Request\интерне.txt", "r", "utf-8")
            hesh.append("#интернет")
        if text[i][0].lower() == "т" and text[i][4].lower() == "в":
            f = codecs.open("D:\Request\телевид.txt", "r", "utf-8")
            hesh.append("#телевидиние")
        if text[i][0].lower() == "т" and text[i][4].lower() == "ф":
            # print("ф")
            f = codecs.open("D:\Request\телефон.txt" , "r", "utf-8")
            hesh.append("#телефон")

        # fd = f.readlines(0)
        # i_1 = 0
        # while i_1 != 3:
        #     list1 = fd[i_1].split()
        #
        #     print(list1)
        #     i_1 += 1


    i += 1

print(hesh)
