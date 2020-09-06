
#9.4 Write a program to read through the mbox-short.txt and figure out who
#has sent the greatest number of mail messages. The program looks for 'From '
#lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address
#to a count of the number of times they appear in the file. After the
#dictionary is produced, the program reads through the dictionary using a
#maximum loop to find the most prolific committer.



fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

counts=dict()
for line in fh:
    if not line.startswith("From: "):
        continue        
    words=line.split()
    #contador:
    for w in words:
        counts[w] = counts.get(w,0) + 1
        
bigword=None
bigcount=None
for w,c in counts.items():
    if w=='From:':
        continue
    if bigcount is None or c > bigcount:
        bigword=w
        bigcount=c
print(bigword, bigcount) 
    
  
