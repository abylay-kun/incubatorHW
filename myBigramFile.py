# import re
# re.findall(^, word).append("^")
import random
import re

with open('text.txt', 'r') as file:
    text = file.read()

def readData():
    data = text
    splittedData = []
    for i in range(len(data)):
        for word in data[i].split():

            splittedData.append(word)
    return splittedData


def createBigram(data):
    listOfBigrams = []
    bigramCounts = {}
    unigramCounts = {}

    for i in range(len(data)-1):
        if i < len(data) - 1 and data[i+1]:

            listOfBigrams.append((data[i], data[i + 1]))

            if (data[i], data[i+1]) in bigramCounts:
                bigramCounts[(data[i], data[i + 1])] += 1
            else:
                bigramCounts[(data[i], data[i + 1])] = 1

        if data[i] in unigramCounts:
            unigramCounts[data[i]] += 1
        else:
            unigramCounts[data[i]] = 1
    return listOfBigrams, unigramCounts, bigramCounts


def calcBigramProb(listOfBigrams, unigramCounts, bigramCounts):

    listOfProb = {}

    for bigram in listOfBigrams:
        word1 = bigram[0]
        word2 = bigram[1]
        listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
        print(bigram)
    return listOfProb


def main():
    data = readData()
    listOfBigrams, unigramCounts, bigramCounts = createBigram(data)

    bigramProb = calcBigramProb(listOfBigrams, unigramCounts, bigramCounts)

    print("\n Bigrams probability ")
    print(bigramProb)

    def createNewName(text):

        listOfBigramsForName = []

        for i in range(len(text)-1):
            bigram = text[i:i+1]
            listOfBigramsForName.append(bigram)
        # print(listOfBigramsForName[randNum])
        # print(listOfBigramsForName)

        newName = ""
        countFirstLetter = 0
        while True:
            randNum = random.randint(0, len(listOfBigramsForName))
            if listOfBigramsForName[randNum] == "\n":
                continue
            elif listOfBigramsForName[randNum - 1] == "\n" and countFirstLetter == 0:

                newName += listOfBigramsForName[randNum]
                countFirstLetter += 1

            elif listOfBigramsForName[randNum + 1] == "\n" and newName != "":

                newName += listOfBigramsForName[randNum]

                print("Future child's terrible name is: ")
                break
            else:
                newName += listOfBigramsForName[randNum]

        print(newName)

    createNewName(text)
main()




