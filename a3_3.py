score = input("Enter Score: ")
try:
    score = float(score)
except:
    print('Invalid')
    quit()

if score < 0:
    print('Re-enter score')
elif score < 0.6:
    print('F')
elif score < 0.7:
    print('D')
elif score < 0.8:
    print('C')
elif score < 0.9:
    print('B')
elif score <= 1:
    print ('A')
else:
    print('Re-enter score') 