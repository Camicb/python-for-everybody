#Each student will have a distinct data file for the assignment - so only use
#your own data file for analysis. The file contains much of the text from the
#introduction of the textbook except that random numbers are inserted
#throughout the text. The basic outline of this problem is to read the file,
#look for integers using the re.findall(), looking for a regular expression
#of '[0-9]+' and then converting the extracted strings to integers and summing
#up the integers. Enter the sum from the actual data and your Python code below:
#Sum:  (ends with 295)



import re
fh=open('actualdata.txt')
lista=list()

for line in fh:
    line=line.rstrip()
    buscar=re.findall('([0-9]+)',line) #() alrededor de [0-9]+ reemplaza re.search
    for num in buscar:
        if len(buscar) > 0: #queda xq hay muchos vacios
            num=int(num)
            lista.append(num)
print(sum(lista))


