# NLP-Work

#ANAGRAM
a Python program which will take a string as the first parameter, and write an output file called anagram_out.txt which contains of all the anagrams (permutations) of the string, one per line, sorted alphabetically. If you use Python 2.7, name your program anagram.py; if you use Python 3.4, name your program anagram3.py. For example, your program will be expected to handle:

> python anagram.py 'ron'

This program will output a file with the following 6 lines, in this order:

nor
nro
onr
orn
rno
ron

#UTF8 Encoder
A Python program which will take a path to an input file (absolute path name) as the first parameter. It will read the file as a binary file, and assume that it contains characters from Unicode's Basic Multilingual Plane (U+0000 to U+FFFF) in UTF-16 encoding (big endian), that is every 2 bytes correspond to one character and directly encode that character's Unicode code point. The program will encode each character in UTF-8 (between 1 and 3 bytes), and write the encoded bytes to a file called utf8encoder_out.txt.

#Input and Output
See in the folder.

#How to run:
> python utf8encoder.py /path/to/input

#Naive Bayes Classifier
A naive Bayes classifier to identify hotel reviews as either truthful or deceptive, and either positive or negative using add-one smoothing on training data. Two programs: nblearn.py will learn a naive Bayes model from the training data, and nbclassify.py will use the model to classify new data.

#Training data format:
A top-level directory with two sub-directories, one for positive reviews and another for negative reviews. Each of the subdirectories contains two sub-directories, one with truthful reviews and one with deceptive reviews. Each of these subdirectories contains any level of subdirectories of text files or text files with one review per file. (Readme file excluded)

#Output format:  
label_a label_b path1  
label_a label_b path2  
⋮  

In the above format, label_a is either “truthful” or “deceptive”, label_b is either “positive” or “negative”, and pathn is the path of the text file being classified.

#How to run:  
> python nblearn.py /path/to/trainingData  
> python nbclassify.py /path/to/testData

#Hidden Markov Model part-of-speech tagger 
Given a sequence of words a Hidden Markov Model tagger finds the most likely sequence of part of speech tags that generates that sequence of words using viterbi algorithm. The program uses add-one smoothing on the transition probabilities and no smoothing on the emission probabilities. For unknown words the program will ignore the emission probabilities and use only the transition probabilities.

#Training data format:
A file with tagged training data in the word/TAG format, with words separated by spaces and each sentence on a new line.

#Output format:
A file with tagged data in the word/TAG format, with words separated by spaces and each sentence on a new line.

#How to run:
> python hmmlearn.py /path/to/trainingData  
> python hmmdecode.py /path/to/testData

#BLUE
A Python program which will take a two paths as parameters: the first parameter will be the path to the candidate translation (a single file), and the second parameter will be a path to the reference translations (either a single file, or a directory if there are multiple reference translations). The program will write an output file called bleu_out.txt which contains a single floating point number, representing the BLEU score of the candidate translation relative to the set of reference translations.

#How to run:
> python calculatebleu.py /path/to/candidate /path/to/reference

Language	  Candidate	       Reference	BLEU score

German	    candidate-1.txt	 reference-1.txt	0.151184476557 

Greek	      candidate-2.txt	 reference-2.txt	0.0976570839819 

Portuguese	candidate-3.txt	 reference-3.txt	0.227803041867 

English	    candidate-4.txt	 reference-4a.txt 0.227894952018 


