'''
Quinlan McGaugh
Programming Assignment 1
Standard

Sample Output:

>>> deduce("((A and B) or not C) and (C or B)")
  A B C
  -----
  F T F
  T T F
  T T T
>>>


'''

import sys
import math

def swap_letters(s, orig, new):
    """
    Swaps every occurence of orig character
    with character new in a string s.
    Used for changing each variable
    instance to True or False.
    """
    
    result = ""
    for char in s:
        if char == orig:
            result = result + new
        else:
            result = result + char
    
    return result



def deduce(input):
    """
    the implementation of the problem
    """
    #SET UP
    print("A B C")
    print("-----")
    
    #NESTED for loops to hit T and F for each variable
    for a in range(0,2):
        for b in range(0, 2):
            for c in range(0, 2):
                tempinput = input
                
                #goes through each character in the predicate
                for char in input:
                    if char == "A":
                        if a == 0:
                            tempinput = swap_letters(tempinput, "A", "False")
                        else:
                            tempinput = swap_letters(tempinput, "A", "True")
                    if char == "B":
                        if b == 0:
                            tempinput = swap_letters(tempinput, "B", "False")
                        else:
                            tempinput = swap_letters(tempinput, "B", "True")
                    if char == "C":
                        if c == 0:
                            tempinput = swap_letters(tempinput, "C", "False")
                        else:
                            tempinput = swap_letters(tempinput, "C", "True")
                            
                #prints only the combos that evaluate to TRUE
                if eval(tempinput) == True:
                    stringtoprint = str(a) + " " + str(b) + " " + str(c)
                    stringtoprint = swap_letters(stringtoprint, "1", "T")
                    stringtoprint = swap_letters(stringtoprint, "0", "F")
                    print(stringtoprint)

def helper():
    variabledict = {}
    variabledict[variable] = predicates

def challenge(input):
    tempinput = ''
    variablelist = []
    variabledict = {}
    i = 0
    #
    print(len(input))
    #
    while i < (len(input)):
        if input[i] == '(' or input[i] == ')' or input[i] == ' ':
            i = i + 1
        elif input[i:i+3] == 'and':
            i = i + 3
        elif input[i:i+2] == 'or':
            i = i + 2
        elif input[i:i+3] == 'not':
            i = i + 3
        else:
            variable = ''
            while input[i] != ' ':
                variable = variable + input[i]
                i = i + 1
            variablelist.append(variable)
            
    print("Variable List: " + variablelist)
    numterms = 2 ** len(variablelist)
    predicatesdict = {}
    for item in variablelist:
        print("Current Variable:" + item)
        falselist = []
        truelist = []
        for value in range(0, 2):
            if value == 0:
                val = "False"
                term = variablelist[i]
                predicate = swapletters(tempinput, item, val)
                print(item + " : " + predicate)
                for f in (range(len(numterms))/2):
                    falselist.append(predicate)
                predicatesdict['False'] = falselist
            else:
                val = "True"
                term = variablelist[i]
                predicate = swapletters(tempinput, item, val)
                print(item + " : " + predicate)
                for t in (range(len(numterms))/2):
                    truelist.append(predicate)
                predicatesdict['True'] = truelist
            print(predicatesdict)
            variabledict[variablelist[i]] = {variabledict:predicatesdict}
        
challenge("(A and B) or C")

def evaluation(variablesdict):
    final = len(variablesdict) - 1
    #PARSE THE DICTIONARY
    
        
        
                
        
    
            
                
