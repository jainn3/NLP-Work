import sys
def findAnagram(inputString):
    if(len(inputString)<=1):
        return inputString

    else:
        results = []
        for permutations in findAnagram(inputString[1:]):
            for i in range(len(inputString)):
                results.append(permutations[:i] + inputString[0:1] + permutations[i:])
        return results


testString = "ab"

text_file = open("anagram_out.txt", "wb")

outputStr = findAnagram(testString)
print type(outputStr)
outputStr.sort()

for mystring in outputStr:
    text_file.write(mystring + '\n')
text_file.close()



