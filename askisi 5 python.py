
f= open("C:\\Users\\User\\Desktop\\two_cities_ascii.txt")
print("LOADING FILE....")
text=f.read()
text=text.lower()
text=text.replace('\"','')
text=text.replace(',','')
text=text.replace('?','')
text=text.replace('\n','')
text=text.replace('.','')
text=text.replace('!','')
text=text.replace('*','')
text=text.replace(':','')
text=text.replace('(','')
text=text.replace(')','')
text=text.replace(';','')
text=text.replace('-','')
text=text.replace('//','')
words = text.split(' ')


#bubble sort
def sortWords(words,wordsCounter):
     for i in range(0,len(wordsCounter)-1):
          for j in range(0,len(wordsCounter)-i-1):
               if (wordsCounter[j]<wordsCounter[j+1]):
                    #swap
                    temp=wordsCounter[j]
                    wordsCounter[j]=wordsCounter[j+1]
                    wordsCounter[j+1]=temp
                    #we need to change the words too
                    temp=words[j]
                    words[j]=words[j+1]
                    words[j+1]=temp
     return words,wordsCounter


# Kratame mia lista me tis lekseis
# kratame enan counter me tin sixnotita twn leksewn
# kanoume sortarisma kai sta dio tables me vasi tin sixnotita
newWords=[]
newWordsCounter=[]

for word in words:
     if (word not in newWords):
          newWords.append(word)
          newWordsCounter.append(1)
     else:
          tempIndex=newWords.index(word)
          newWordsCounter[tempIndex]+=1

sortedWords,sortedWordsCounter=sortWords(newWords,newWordsCounter)
print("10 MOST FREQUENT WORDS")
print(sortedWords[:10])
print(sortedWordsCounter[:10])

twoCharacters=[]
twoCharactersCounter=[]
for word in words:
     tempWord=word[:2]
     if (tempWord not in twoCharacters):
          twoCharacters.append(tempWord)
          twoCharactersCounter.append(1)
     else:
          tempIndex=twoCharacters.index(tempWord)
          twoCharactersCounter[tempIndex]+=1

sortedWords,sortedWordsCounter=sortWords(twoCharacters,twoCharactersCounter)
print("3 MOST FREQUENT TWO CHARACTERS")

print(sortedWords[:3])
print(sortedWordsCounter[:3])

threeCharacters=[]
threeCharactersCounter=[]
for word in words:
     tempWord=word[:3]
     if (tempWord not in threeCharacters):
          threeCharacters.append(tempWord)
          threeCharactersCounter.append(1)
     else:
          tempIndex=threeCharacters.index(tempWord)
          threeCharactersCounter[tempIndex]+=1

sortedWords,sortedWordsCounter=sortWords(threeCharacters,threeCharactersCounter)
print("3 MOST FREQUENT THREE CHARACTERS")

print(sortedWords[:3])
print(sortedWordsCounter[:3])
