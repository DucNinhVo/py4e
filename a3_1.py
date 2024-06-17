hrs = input("Enter Hours:")
h = float(hrs)
print(h)
rate = input("Enter Rate:")
r = float(rate)
print(r)
pay = 0
if h <= 40:
    pay = h*r
    print(pay)
else:
    pay = 40*r + (h-40)*r*1.5
    print(pay)
print(pay)