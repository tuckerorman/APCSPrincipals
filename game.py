import random
rnum=random.randint(1000, 9999)
print(rnum)
strnum=str(rnum)
guesslist= []
rnumlist= []
for digit in strnum:
    rnumlist.append (int(digit))

userinput1 = input("input 4 numbers")
if int(userinput1) == rnum:
    print("correct")
print(rnumlist)

for digit in strnum:
    rnumlist.append (int(digit))

for i in rnumlist:
    for j in guesslist:
     if i == j:
            print(rnumlist.index(i))
    else:
        print ("not correct")















