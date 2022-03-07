#   Anthony Nguyen
#   CS4550 Web Programming
#   Dr Tim Ball

import re

#First function, takes a start point and then line
def calcFirst(s, productions):
    
    first = set()
    
    #For loop starting at the first production item.
    for i in range(len(productions[s])):
        #Nested for loop starting at the first one's and then it's itteration
        for j in range(len(productions[s][i])):
            
            c = productions[s][i][j]
            
            #isupper basically says if it's a non-terminal or not
            #And from there it either appends it to the firsts list or it will call the first function on it if it is not a terminal
            if(c.isupper()):
                f = calcFirst(c, productions)
                if('.' not in f):
                    for k in f:
                        first.add(k)
                    break
                else:
                    if(j == len(productions[s][i])-1):
                        for k in f:
                            first.add(k)
                    else:
                        f.remove('.')
                        for k in f:
                            first.add(k)
            else:
                first.add(c)
                break
                
    return first

#Follow function, takes the start, the production line and then firsts
def calcFollow(s, productions, first):
    follow = set()
    #empty set
    if len(s)!=1 :
        return {}
    #if its the start, add $
    if(s == list(productions.keys())[0]):
        follow.add('$') 
    
    #now we go through the production rule
    for i in productions:
        for j in range(len(productions[i])):
            if(s in productions[i][j]):
                idx = productions[i][j].index(s)
                
                if(idx == len(productions[i][j])-1):
                    if(productions[i][j][idx] == i):
                        break
                    else:
                        f = calcFollow(i, productions, first)
                        for x in f:
                            follow.add(x)
                else:
                    while(idx != len(productions[i][j]) - 1):
                        idx += 1
                        if(not productions[i][j][idx].isupper()):
                            follow.add(productions[i][j][idx])
                            break
                        else:
                            f = calcFirst(productions[i][j][idx], productions)
                            
                            if('.' not in f):
                                for x in f:
                                    follow.add(x)
                                break
                            elif('.' in f and idx != len(productions[i][j])-1):
                                f.remove('.')
                                for k in f:
                                    follow.add(k)
                            
                            elif('.' in f and idx == len(productions[i][j])-1):
                                f.remove('.')
                                for k in f:
                                    follow.add(k)
                                
                                f = calcFollow(i, productions, first)
                                for x in f:
                                    follow.add(x)
                            
    return follow

#main function incase it needs to be called again in the future
def main():
    productions = {}

    #takes the input file

    #cfg = open("test.txt", r)
    #cfg = open("test2.txt", r)
    cfg = open("test3.txt", "r")
    
    first = {}
    follow = {}
    
    #for the input file, it splits it into a list
    for prod in cfg:
        l = re.split("( /->/\n/)*", prod)
        m = []
        #from the list it reads the line and ignores new lines or the ->
        for i in l:
            if (i == "" or i == None or i == '\n' or i == " " or i == "-" or i == ">" or i == "<"):
                pass
            else:
                m.append(i)
        
        #left and right productions
        leftProduction = m.pop(0)
        rightProduction = []
        t = []
        
        for j in m:
            if(j != '|'):
                t.append(j)
            else:
                rightProduction.append(t)
                t = []
        
        rightProduction.append(t)
        productions[leftProduction] = rightProduction
    
    for s in productions.keys():
        first[s] = calcFirst(s, productions)
    print("My epsilons are denoted as '.' ")
    print("")
    print("Firsts:")
    for leftHandSide, rightHandSide in first.items():
        print(leftHandSide, ":" , rightHandSide)
    
    print("")

    for lhs in productions:
        follow[lhs] = set()
    
    for s in productions.keys():
        follow[s] = calcFollow(s, productions, first)
    
    print("Follows:")
    for lhs, rhs in follow.items():
        print(lhs, ":" , rhs)
    
    cfg.close()

main()