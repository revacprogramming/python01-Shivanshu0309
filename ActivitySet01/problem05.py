# Functions


def computepay(h, r):
    if h > 40:
        x = h*r
        o = (h - 40)*0.5*r
        p = x+o
        return p 
    else:
        x = h*r
        return x 
      
    

hrs = input("Enter Hours:")
h = float(hrs)
rte = input("enter rate per hour?")
r = float(rte)
p = computepay(h,r)
print("Pay", p)
