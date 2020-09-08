sentence = []

while 1:
    word = input()
    if word != "0":
        sentence.append(word)
    else:
        break
sentence1 = sorted (sentence,key=lambda x:x[-1])    

sentence2 = ''
for i in range (len(sentence1)):
    sentence2 += sentence1[i][0:-1]
    
if sentence2[-1] == ' ':
    print(sentence2[0:-1]+'.')
