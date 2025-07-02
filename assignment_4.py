#task 1
try:
    print("Reading File Content")
    file=open('sample.txt','r')
    print('Line 1',file.readline())
    print('Line 2',file.readline())
    file.close()
except FileNotFoundError :
    print('Error: The file \'sample.txt\' does not exist ')
    
#task 2 Write and append in file
a=input('Enter Text to write to the file:')
file=open('output.txt','w')
file.write(a)
file.write('\n')
print('Data successfully written to output.txt.\n')
file.close()

a=input('Enter additional Text to append:')
file=open('output.txt','a')
file.write(a)
print('Data successfully appended.\n')
file.close()

print('Final Content of output.txt')
file=open('output.txt','r')
print(file.read())
