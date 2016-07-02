from __future__ import division
import os
from collections import Counter
import math
import codecs
import sys
def ngrams(input, n):
  input = input.split()
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  ngramList = [' '.join(x) for x in output]
  return ngramList

def modified_precision(candidate, references, n, numerator, denom):

    #count is a list
    #ngram of the cadidate | counts is the candidate
    counts = Counter(ngrams(candidate,n+1))
    if not counts:
        return 0
    max_counts = {}

    #reference is a string
    for reference in references:
        reference_count = Counter(ngrams(reference,n+1))
        #iterate each ngram in candidate and find maximum value of each ngram amoung all the references
        for ngram in counts:
            max_counts[ngram]=max(max_counts.get(ngram,0), reference_count[ngram])

    #checking if maximum count(match with each reference) is less than the count of ngram in candidate
    clipped_count = dict((ngram,min(count, max_counts[ngram])) for ngram, count in counts.items())

    #return sum(clipped_count.values()) / sum(counts.values())
    numerator[n]+=sum(clipped_count.values())
    denom[n]+= sum(counts.values())
    #return sum(clipped_count.values())


def compute(candidate, references,p_ns,denom):
    #candidate = [c.lower() for c in candidate]
    #references = [[r.lower() for r in reference] for reference in references]

    for i,_ in enumerate(p_ns,start=0):
        modified_precision(candidate,references,i,p_ns,denom)

def brevity_penalty(candidate, references):
    c = 0
    for item in candidate:
        c+=len(item.split())

    min = sys.maxint

    r = 0
    r1len = 0

    for i in range(len(candidate)):
        min = sys.maxint
        for ref in references:
            clen = len(candidate[i].split())
            reflen = len(ref[i].split())
            if abs(clen-reflen) < min:
                min = abs(clen-reflen)
                r1len = reflen
        r+=r1len
    if c > r:
        return 1
    else:
        return math.exp(1 - r / c)


def iterateAllCandidate(arrayCandid, arrayRef):
    p_ns = [0.0,0.0,0.0,0.0]

    denom = [0,0,0,0]
    weights = [0.25,0.25,0.25,0.25]
    for i in range(len(arrayCandid)):
        allreferences = []
        for ref in arrayRef:
            allreferences.append(ref[i])
        compute(arrayCandid[i],allreferences,p_ns,denom)

    s = math.fsum(w * math.log(p_n/den) for w, p_n,den in zip(weights, p_ns,denom) if p_n)

    bp = brevity_penalty(arrayCandid, arrayRef)

    return bp * math.exp(s)

def driverProgram(candidPath, refDir):
    arrayCandid = []
    arrayRef = []

    f = codecs.open(candidPath, 'r')
    for line in f:
        arrayCandid.append(line.strip("\n").strip())

    if os.path.isdir(refDir):
        for root, dirs, files in os.walk(refDir):
            for file in files:
                ref = []
                if file.endswith(".txt"):
                    print(os.path.join(root, file))
                    f = codecs.open(os.path.join(root, file), 'r')
                    for line in f:
                        ref.append(line.strip("\n").strip())
                arrayRef.append(ref)
    else:
        ref = []
        f = codecs.open(refDir, 'r',)
        for line in f:
            ref.append(line.strip("\n").strip())
        arrayRef.append(ref)

    return iterateAllCandidate(arrayCandid,arrayRef)


def writeToOutputFile(filepath, value):
    text_file = open(filepath, "wb")
    text_file.write(str(value))
    text_file.close()



pathc = sys.argv[1]#candidate-1.txt
pathr = sys.argv[2]#reference-1.txt

retValue=1.0
try:
    retValue= driverProgram(pathc,pathr)
    #retValue= driverProgram("candidate-1.txt","reference-1.txt")
    path ="bleu_out.txt"
except:
    pass

writeToOutputFile(path,retValue)
