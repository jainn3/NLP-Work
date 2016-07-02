import os
import math
import sys

#path = "C:/544/op_spam_train"
path = sys.argv[1]
punc = {',', '.', '{', '}', '(', ')', '!', '"', '@', '#', '$', '%', '^', '&', '*', ':', ';', '/', '?', '<', '>', '=', '+','1','2','3','4','5','6','7','8','9','0'}
stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'one','two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

posIndex = 0
negIndex = 1
deceptIndex = 2
truthIndex = 3

posProb = 0.0
negProb = 0.0
decepProb = 0.0
truthProb = 0.0

dict = {}

totalCount = [0, 0, 0, 0]
totalWordCount = 0

def num_there(s):
    return any(i.isdigit() for i in s)

def resetGlobals():
    global posProb, negProb, decepProb, truthProb
    posProb = 0.0
    negProb = 0.0
    decepProb = 0.0
    truthProb = 0.0

def findMaxProb(filepath):
  #  print "filepath is :" + filepath
    output = ""
    if truthProb < decepProb:
  #      print("It is truth")
  #      print truthProb
        output += "deceptive" + " "
    else:
  #      print("It is deceptive")
   #     print(decepProb)
        output += "truthful" + " "

    if posProb < negProb:
  #      print "It is positive"
   #     print(posProb)
        output += "negative" + " "
    else:
  #      print "It is negative"
  #      print(negProb)
        output += "positive" + " "

    text_file.write(output + filepath + "\n")
    resetGlobals()

def calProb(index, word):
    list = dict.get(word)
    cnt = list[index]
    prob =  math.log(int(cnt)) - math.log(int(totalCount[index]) + int(totalWordCount))
    #print(word)
    #print prob
    return prob

def calAllProb(word):
    global posProb, negProb, decepProb, truthProb
    posProb += calProb(posIndex, word)
    negProb += calProb(negIndex, word)
    decepProb += calProb(deceptIndex, word)
    truthProb += calProb(truthIndex, word)

def classifyfile(fpath):
    f = open(fpath, "r")
    f1 = f.read()
    for word in f1.split():
        word = ''.join(ch for ch in word if ch not in punc)
        if word:
            if word not in stop_words:
                if True:
                    word = word.lower()
                    if dict.has_key(word):
                        calAllProb(word)

def readTextFile():
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") and not "README.txt" in file:
                classifyfile(os.path.join(root, file))
                findMaxProb(file)


f = open("nbmodel.txt", "r")
text_file = open("nboutput.txt", "wb")

line = f.readline()
if line:
    word = line.split()
    del word[0]

while True:
    line = f.readline()
    if not line:
        break
    word = line.split()
    key = word[0]
    del word[0]
    dict[key] = word
totalWordCount = len(dict)
readTextFile()
f.close()
text_file.close()