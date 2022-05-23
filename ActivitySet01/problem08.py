# Files
fname = input("Enter file name: ")
count = 0
b= 0

try :
    open(fname)
    
except :
    print("enter a valid name ")
    
fh = open(fname)
h= 0

    
for line in fh:
    h = h +1
    if  line.startswith("X-DSPAM-Confidence:"):
        
        x = line.find(':')
        y = line[x+2:]
        a = float(y)
        b += a
        count = count+1
   
    
z = b/count
print("Average spam confidence:",z)


