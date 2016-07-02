import os
import os.path
import sys
#path = "C:/544/op_spam_train"
path = sys.argv[1]
dict = {}

posIndex = 0
negIndex = 1
deceptIndex = 2
truthIndex = 3

totalCount = [0, 0, 0, 0]

punc = {',', '.', '{', '}', '(', ')', '!', '"', '@', '#', '$', '%', '^', '&', '*', ':', ';', '/', '?', '<', '>', '=', '+','1','2','3','4','5','6','7','8','9','0'}
stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'one','two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']


def num_there(s):
    return any(i.isdigit() for i in s)


def fillHashTable(index1, index2, fpath):
               # print("Current text file is : " + fpath)
                f = open(fpath, "r")
                f1 = f.read()
                for word in f1.split():
                    word = ''.join(ch for ch in word if ch not in punc)
                    if word:
                        if word not in stop_words:
                            if True:
                                word = word.lower()
                                list = dict.get(word, [1, 1, 1, 1])
                                list[index1] += 1
                                list[index2] += 1
                                dict[word] = list
                                totalCount[index1] += 1
                                totalCount[index2] += 1


def readTextFile(class1Index, class2Index, filepath):
        #print(class1 + " " + class2 + " " + filepath)
        for txtFile in os.listdir(filepath):
            fillHashTable(class1Index, class2Index, filepath + "/" + txtFile)

def outputHashToFie(outputFilePath):
    text_file = open(outputFilePath, "wb")

    #text_file.write("Nimesh" + "Total words in Dict is :")
    #text_file.write(str(len(dict)))
    #text_file.write("globalcounts " + " " + str(totalCount[0]) + " " + str(totalCount[1]) + " " + str(totalCount[2]) + " " + str(totalCount[3]) + "\n")
    for key, val in dict.items():
        mystring = str(key)
        for cnt in dict[key]:
            mystring += " " + str(cnt)
        text_file.write(mystring + '\n')
    text_file.close()


for subdirectory in os.listdir(path):
    if subdirectory.__contains__("positive"):
        for posDirectory in os.listdir(path + "/" + subdirectory):
            if posDirectory.__contains__("deceptive"):
                for foldDirectory in os.listdir(path + "/" + subdirectory + "/" + posDirectory):
                    if foldDirectory.__contains__("fold"):
                       # print("Fold directory reached for positive + deceptive" + foldDirectory)
                        readTextFile(posIndex, deceptIndex, path + "/" + subdirectory + "/" + posDirectory + "/" + foldDirectory)
            elif posDirectory.__contains__("truthful"):
                for foldDirectory in os.listdir(path  + "/" + subdirectory + "/" + posDirectory):
                    if foldDirectory.__contains__("fold"):
                        #print("Fold directory reached for positve + truthfulness" + foldDirectory)
                        readTextFile(posIndex, truthIndex, path + "/" + subdirectory + "/" + posDirectory + "/" + foldDirectory)
    elif subdirectory.__contains__("negative"):
        for negDirectory in os.listdir(path  + "/" + subdirectory):
            if negDirectory.__contains__("deceptive"):
                for foldDirectory in os.listdir(path + "/" + subdirectory + "/" + negDirectory):
                    if foldDirectory.__contains__("fold"):
                       # print("Fold directory reached for negative + deceptive" + foldDirectory)
                        readTextFile(negIndex, deceptIndex, path + "/" + subdirectory + "/" + negDirectory + "/" + foldDirectory)
            elif negDirectory.__contains__("truthful"):
                for foldDirectory in os.listdir(path  + "/" + subdirectory + "/" +negDirectory):
                    if foldDirectory.__contains__("fold"):
                        #print("Fold directory reached for positve + truthfulness" + foldDirectory)
                        readTextFile(negIndex, truthIndex, path + "/" + subdirectory + "/" +
                                     negDirectory + "/" + foldDirectory)
    outputHashToFie("nbmodel.txt")

'''
create a method with 2 arguments and directory path: 12 calls to this method
Open all text file and add to hash table
see how to output hashtable to file
'''
