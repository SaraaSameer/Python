#Set Mutations Problem
#For Set Methods:  update,intersection_update,symmetric_difference_update,difference_update

string2="(tempSet)"
setLength=int(input())
originalSet=set()
elementString =input()
elementString=elementString.strip().split()
for x in elementString:
    originalSet.add(x)

insTimes =int(input())
for x in range(insTimes):
    string1 = "originalSet."
    instruction= input()
    instruction=instruction.strip().split()
    ins=instruction[0]
    tempSetLength=int(instruction[1])

    tempSet=set()
    elementString=input()
    elementString = elementString.strip().split()
    for y in elementString:    #Input Set02 Elements
        tempSet.add(y)
    string1+=ins
    string1+=string2
    eval(string1)

sum=0
for x in originalSet:
    sum+=int(x)
print(x)

