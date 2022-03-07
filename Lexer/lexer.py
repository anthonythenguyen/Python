#Anthony Nguyen
#CS4550 Programming Languages
#Dr Tim Ball

import re

search_file = open('input.txt')

def whatIs(s):
    
    if re.compile("^([0-9]+)$").match(s) is not None:
        return ["Number", s, 0]
    elif re.compile("([+\-\/*])").match(s) is not None:
        return ["Operator", s, 0]
    elif re.compile("(=)").match(s) is not None:
        return ["Assignment", s, 0]
    elif re.compile("^(\?)").match(s) is not None:
        return ["Comment", s, 1]
    elif re.compile('([\"][^(/")]*[\"])').match(s) is not None:
        return ["String", s, 3]
    elif re.compile('([\"][^(/")]*)').match(s) is not None:
        return ["StringStart", s, 3]
    elif re.compile('([^(/")]*[\"]$)').match(s) is not None:
        return ["StringEnd", s, 3]
    elif re.compile("^([A-Z]+[A-Za-z0-9]*)").match(s) is not None:
        return ["Keyword", s, 2]
    elif re.compile("(;)").match(s) is not None:
        return ["EndOfStatement", s, 0]
    elif re.compile("(^[a-z]+[a-z0-9]*)").match(s) is not None:
        return ["Identifier", s, 0]
    else:
        return ["Whitespace", s, 1]


inputFileArray = search_file.read().split('\n')
splitArray = []
for line in inputFileArray:
    words = line.split(' ')
    splitArray+=words
    splitArray.append("\n")

tokenizedSymbols = []
commentStarted = False
stringStart = False
tempString = ""
for word in splitArray:
    wordType = whatIs(word)
    if commentStarted == False and stringStart == False:
        if wordType[0] == "Comment":
            commentStarted = True
        elif wordType[0] == "StringStart":
            stringStart = True
            tempString= tempString+word[1:]
        elif wordType[0] == "Whitespace":
            continue
        elif wordType[0] == "String":
            tokenizedSymbols.append({
                "Value": word[1:-1],
                "Type": wordType[0]
            })
        else:
            tokenizedSymbols.append({
                "Value": word,
                "Type": wordType[0]
            })
    elif commentStarted:
        if word.find("\n") >= 0:
            commentStarted = False
    elif stringStart: 
        if wordType[0]=="StringEnd":
            stringStart = False
            tempString= tempString + ' '+word[:-1]
            tokenizedSymbols.append({
                "Value": tempString,
                "Type": "String"
            })
            tempString = ""
        else:
            tempString= tempString + ' '+word
            
    else:
        print("Sadge")


#for symbol in tokenizedSymbols:
#    if symbol["Type"] == "Keyword" and symbol["Value"] == "Update":
#        print("Value : " + symbol["Value"] + " , Type : " + symbol["Type"] + ", Description: Updating a variable")
#    elif symbol["Type"] == "Keyword" and symbol["Value"] == "Define":
#        print("Value : " + symbol["Value"] + " , Type : " + symbol["Type"] + ", Description: Defining a variable")
#    elif symbol["Type"] == "Keyword" and symbol["Value"] == "Print":
#        print("Value : " + symbol["Value"] + " , Type : " + symbol["Type"] + ", Description: Printing on the screen")
#    else:
#        print("Value : " + symbol["Value"] + " , Type : " + symbol["Type"])
outputFile = open("output.txt", "w")
for symbol in tokenizedSymbols:
    if symbol["Type"] == "Keyword" and symbol["Value"] == "Update":
        outputFile.write("Value : " + symbol["Value"] + " , Type : " + symbol["Type"] + ", Description: Updating a variable")
        outputFile.write("\n")
    elif symbol["Type"] == "Keyword" and symbol["Value"] == "Define":
        outputFile.write("Value : " + symbol["Value"] + " , Type : " + symbol["Type"] + ", Description: Defining a variable")
        outputFile.write("\n")
    elif symbol["Type"] == "Keyword" and symbol["Value"] == "Print":
        outputFile.write("Value : " + symbol["Value"] + " , Type : " + symbol["Type"] + ", Description: Printing on the screen")
        outputFile.write("\n")
    else:
        outputFile.write("Value : " + symbol["Value"] + " , Type : " + symbol["Type"])
        outputFile.write("\n")
outputFile.close()