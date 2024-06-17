def computepay(h, r):   
    if hrs <= 40:
        return h*r
    else:
        return 40*r + (h-40)*r*1.5

hrs = input("Enter Hours:")
hrs = float(hrs)
rt = input ("Enter Rate:")
rt = float(rt)
p = computepay(hrs, rt)
print("Pay", p)