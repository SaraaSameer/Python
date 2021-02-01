N = int(input())
L=[]
openingBrace= "("
closingBrace= ")"

for i in range(0,N):
    str1=input().split()
    str2="L."
    if(str1[0]=='insert'):
        str2+=str1[0]
        str2+=openingBrace
        str2+=str1[1]
        str2+=','
        str2+=str1[2]
        str2+=closingBrace

    elif (str1[0]=='append' or str1[0]=='remove'):
        str2 += str1[0]
        str2 += openingBrace
        str2 += str1[1]
        str2 += closingBrace

    elif (str1[0]=='print'):
        print(L)
        continue
    else:
        str2 += str1[0]
        str2+= openingBrace
        str2+= closingBrace
    eval(str2)
