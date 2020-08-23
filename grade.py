a=eval(input("enter 1st subject marks:"))
b=eval(input("enter 2nd subject marks:"))
c=eval(input("enter 3rd subject marks:"))
d=eval(input("enter 4th subject marks:"))
p=(a+b+c+d)/400*100
if(p>=70):
    print('A+ Grade')
if(p>=60 and p<70):
    print('A Grade')
if(p>=50 and p<60):
    print('B Grade')
if(p>=40 and p<50):
    print('C Grade')
if(p<40):
    print('D Grade')
