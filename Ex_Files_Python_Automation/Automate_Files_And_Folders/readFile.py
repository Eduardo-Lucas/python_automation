f = open('inputFile.txt', 'r')
passedFile = open('passedFile.txt', 'w')
failedFile = open('failedFile.txt', 'w')
passQty = 0
failQty = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passedFile.write(line)
        passQty += 1
    else:
        failedFile.write(line)
        failQty += 1

f.close()
passedFile.close()
failedFile.close()

print('Passed: '+str(passQty))
print('Failed: '+str(failQty))
print('Total : '+str(passQty+failQty))
