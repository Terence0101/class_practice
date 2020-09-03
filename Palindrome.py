def checkpd (line):
    for string in line:
        if string[0::] == string[::-1]:
            print('YES')
        else:
            print('NO')
        
line = []
while True:
    ip = input()
    if ip != '-----':
        line == line.append(a)
    else:
        break
check(line)
