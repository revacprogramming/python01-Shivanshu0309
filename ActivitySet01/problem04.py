# Conditional Execution

hrs = input("Enter Hours:")
h=float(hrs)
rate=input("enter rate:")
r=float(rate)
if ( h > 40 ):
    pay=h*r
    ot=(h-40)*0.5*r
    p=pay+ot
    print("",p)
else :
    h = h
    p = h*r
    print("",p)
