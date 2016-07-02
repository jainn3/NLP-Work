from __future__ import division
from collections import defaultdict

import sys
class Classify:
     def __init__(self):
        self.emit = defaultdict(int)
        self.transition = defaultdict(int)
        self.context = defaultdict(int)
        self.states = set()
        self.seenwords = defaultdict(int)

     def readFile(self,fileName):
         with open(fileName) as f:
             line = f.readline()
             #print line
             context_size, tran_size, emit_size = line.split()
             context_size = int(context_size.split(":")[1])
             tran_size = int(tran_size.split(":")[1])
             emit_size = int(emit_size.split(":")[1])
             cnt = 1
             for line in f:
                 #print line
                 key,val = line.rsplit(' ',1)
                 if cnt <=context_size:
                     self.context[key] = int(val)
                     self.states.add(key)
                 elif cnt > context_size and cnt <=(tran_size + context_size):
                     self.transition[key] = int(val)
                 elif cnt >= (context_size+tran_size):
                     self.emit[key] = int(val)
                     _word = key.split(" ",1)[1]
                     self.seenwords[_word] = 1
                 cnt += 1

         #print self.emit
         #print str(len(self.context)) + " " + str(len(self.transition)) + " " + str(len(self.emit))

     def viterbi(self,obs):
        V = [defaultdict(int)]
        V2 = [defaultdict(int)]
        for i in self.states:
            emit_prob = (self.emit[i + " "+ obs[0]])/(self.context[i])
            tran_prob = (self.transition["<s>" + " " + i]+1)/(self.context["<s>"] + len(self.context))
            if emit_prob == 0:
                emit_prob = 1
            V[0][i] = tran_prob * emit_prob
            V2[0][i] = "<s>"
            #print V[0][i]

        maxstate = ""
        for t in range(1,len(obs)):
            V.append(defaultdict(int))
            V2.append(defaultdict(int))
            for y in self.states:
                emit_prob = (self.emit[y+" "+obs[t]])/(self.context[y])
                if self.seenwords[obs[t]] == 0:
                    emit_prob = 1.0
                elif emit_prob == 0.0:
                    continue
                maxprob = -sys.maxint - 1
                maxstate = ""
                for y0 in self.states:
                    tran_prob = (self.transition[y0 + " " + y]+1)/(self.context[y0] + len(self.context))
                    prob = V[t - 1][y0] * tran_prob * emit_prob
                    if prob >= maxprob:
                        if prob == maxprob:
                            if y0 in V2[t-1]:
                                maxprob = prob
                                maxstate = y0
                        else:
                            maxprob = prob
                            maxstate = y0

                # print prob
                V[t][y] = maxprob
                V2[t][y] = maxstate

        currentState = ""
        backpointerLen = len(V)-1
        currentState = maxstate
        #h = max(V[-1].values())

        #print "max is :" + str(h)
        #print "max was :" + str(V[backpointerLen][currentState])
        maxp = -sys.maxint - 1
        j =V[-1]
        for key,val in j.iteritems():
            if val > maxp:
                currentState = key
                maxp = val

        output = ""
        while currentState !="<s>":
            #print currentState
            output = obs[backpointerLen] + "/" + str(currentState) +" "+ output
            currentState = V2[backpointerLen][currentState]
            backpointerLen -= 1
        return output
        #print currentState

     def executeViterbi(self,path):
         text_file = open("hmmoutput.txt", "wb")
         with open(path) as f:
             for line in f:
                line = line.rstrip('\n')
                #print line
                obs = line.split(" ")
                    #print obs
                try:
                     res = self.viterbi(obs)
                     text_file.write(res + '\n')
                except:
                     try:
                         returned = []
                         tag = ""
                         for key, value in self.context.iteritems():
                            tag = key
                            break

                         for i in range(0, len(obs)):
                           returned.append(tag)
                         output_line = ""
                         for i in range(0,len(obs)):
                            output_line+=obs[i]+'/'+returned[i]+" "

                         text_file.write(output_line+'\n')
                     except:
                         pass
                     pass
         text_file.close()

path = sys.argv[1]
#path = "C:\\544\\HW2\\catalan_corpus_dev_raw.txt"
obj = Classify()
obj.readFile("hmmmodel.txt")
#start = time.time()
obj.executeViterbi(path)
#obj.executeViterbi("C:\\544\\HW2\\catalan_corpus_dev_raw.txt")

#end = time.time()
#print(end - start)
