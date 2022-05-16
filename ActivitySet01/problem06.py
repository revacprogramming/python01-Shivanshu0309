# Loops & Iterators
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    n = int(num)
    try :
        if largest is None:
            largest = n
        elif n > largest:
             largest = n

        if smallest is None:
             smallest = n
        elif n < smallest :
             smallest = n
    except :
         print ("Invalid input")
         continue 

print("Maximum", largest)
print ("smallest",smallest)




  

         

    




