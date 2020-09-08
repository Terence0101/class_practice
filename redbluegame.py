score = 0
combo = 0
combomax = 0

computer = input()
play = input()

for i in range (len(computer)):
    if computer[i] == '-':
        continue
    elif computer[i] == play[i]:
        combo += 1
        score += combo*100
        if combo > combomax:
            combomax = combo
    else:
        combo = 0
        
print(score,combomax)
