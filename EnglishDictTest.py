# encoding: utf-8

# This is a word learning program (dictionary). Create a cvs file and put every word/sentence you want.
# first part of row: word in your language
# second part of row: english word for example


import csv
import random

sentence = {}
FILENAME = 'resources/20200326.txt'
with open(FILENAME) as f:
    reader = csv.reader(f, skipinitialspace=True, quotechar=",")
    for row in reader:
        sentence[row[0]] = row[1]


def quiz_me():
    quiz_base = list(sentence.keys()) # casting as list for python 3 compatibility
    ok_answer, bad_answer = 0, 0
    all_answer = len(quiz_base)

    while len(quiz_base):
        j = len(quiz_base)
        print("Number of questions: "+str(j)+"/"+str(all_answer))
        key = random.choice(quiz_base)
        i = input(key + ': ')

        if i == sentence[key]:
            print('correct!')
            quiz_base.remove(key)  # if answer is correct, remove from the list
            ok_answer += 1

        else:
            print('incorrect')
            print("Answer:" + sentence[key])
            bad_answer += 1

    print("There's no other question. You know everything:)")
    print("Number of correct answers " + str(ok_answer))
    print("Number of incorrect answers " + str(bad_answer))


quiz_me()
