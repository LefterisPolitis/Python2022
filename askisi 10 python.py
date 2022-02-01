f= open("C:\\Users\\User\\Desktop\\two_cities_ascii.txt")
text=f.read().replace('\n','')
print("LOADING FILE....")

binary=""
binary2=""
bitarray16=[]
numbers=[]

for i in range(0,len(text)):
    #metatrepoume to char se binary 
    binary+=bin(ord(text[i]))[2:]
    # kratame ta 2 prwta kai ta 2 teleftaia bits apo to binary
    binary2+=bin(ord(text[i]))[2:][:2]+""+bin(ord(text[i]))[2:][5:] 

for i in range(0,len(binary2),16):
    #kratame ta bits ana 16
    bitarray16.append(binary2[i:i+16])

for bit in bitarray16:
    #metatrepoume ta 16bita se aplous arithmous se dekadiko sistima
    numbers.append(int(bit,2))

# % -> akairea diairesi

zigoi=0.0
for number in numbers:
    if (number%2==0):
        zigoi+=1

diairetestou3=0.0
for number in numbers:
    if (number%3==0):
        diairetestou3+=1

diairetestou5=0.0
for number in numbers:
    if (number%5==0):
        diairetestou5+=1

diairetestou7=0.0
for number in numbers:
    if (number%7==0):
        diairetestou7+=1

print("====POSOSTA====")
print(" ZIGOI   | "+str(zigoi/len(numbers)*100)+"%")
print(" TOU 3   | "+str(diairetestou3/len(numbers)*100)+"%")
print(" TOU 5   | "+str(diairetestou5/len(numbers)*100)+"%")
print(" TOU 7   | "+str(diairetestou7/len(numbers)*100)+"%")
