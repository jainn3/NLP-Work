from collections import defaultdict
import sys
class Training:
    def __init__(self):
        self.emit = defaultdict(int)
        self.transition = defaultdict(int)
        self.context = defaultdict(int)

    def trainData(self, filepath):
        with open(filepath) as f:
            for line in f:
                line = line.rstrip('\n')
                previous = "<s>"
                self.context[previous]+=1

                for word in line.split():
                    wordList = word.rsplit('/',1)
                    word = wordList[0]
                    tag = wordList[1]

                    self.transition[previous + " " + tag] += 1
                    self.context[tag]+=1
                    self.emit[tag + " " + word] += 1
                    previous = tag

                self.transition[previous + " </s>"] = 1
        self.writeAllFile("hmmmodel.txt")


    def writeDictToFile(self, fp, d):
        for key, value in d.iteritems():
            fp.write(key + " " + str(value) + '\n')

    def writeAllFile(self, filepath):
        text_file = open(filepath, "wb")
        text_file.write("context_count:" + str(len(self.context)) + " transition_count:" + str(len(self.transition)) + " emission_count:" + str(len(self.emit)) + '\n')
        self.writeDictToFile(text_file,self.context)
        self.writeDictToFile(text_file,self.transition)
        self.writeDictToFile(text_file,self.emit)
        text_file.close()

path = sys.argv[1]
#path = 'C:\\544\HW2\\catalan_corpus_train_tagged.txt'
obj = Training()
#obj.trainData('C:\\544\HW2\\catalan_corpus_train_tagged.txt')
obj.trainData(path)

