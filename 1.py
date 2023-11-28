print("welcome to Melanie dental clinic")
x = str(input("patient name:"))
y = str(input("Has you ever been here before(Y/N):"))
a = float(input("patient height (in cm):"))
b = float(input("patient weight (in kg):"))
c = str(input("When was the patient last weighed in (1/1/2000 if never weighed)?"))
d = float(input("What was the patient’s weight (in kg, -1 if never weighed)?"))
e = int(input("Practitioner’s overall assessment of the patient’s health (-5=very poor to +5=excellent, 0 for neutral)"))

print("height:", a)
print("weight:", b)
f = d - b
print("change from previous weight in kg:", f)

m = (b / (a ** 2)) * 100

print("your BMI: ", round(m, 1))

if m > 30:
    print("you are obese!")
    g = 0
elif 29.9 > m > 25:
    print("you are overweight!")
    g = 0
elif 24.9 > m > 18.5:
    print("you are healthy!")
    g = 0
elif 18.4 > m > 17:
    print("you are underweight!")
    g = 0
else:
    print("you are too thin!")
    g = 0
    print("your intermediate health score is:", g)

    if f == -1:
        h = g + 1
        print("new intermediate health score:", h)
    else:
        if f == 0 or f == 1 or f == -1:
            h = g - 1
            print("new intermediate health score:", h)
        else:
            if 18.4 > m > 17:
                if f < 0:
                    h = g - 3
                    print("new intermediate health score:", h)
                else:
                    h = g + 2
                    print("new intermediate health score:", h)
            elif m < 17:
                if f < 0:
                    h = g - 5
                    print("new intermediate health score:", h)
                else:
                    h = g + 5
                    print("new intermediate health score:", h)

    if 29.9 > m > 25:
        if f > 0:
            h = g - 3
            print("new intermediate health score:", h)
        elif h < -1:
            h = g + 3
            print("new intermediate health score:", h)
        else:
            h = g
            print("new intermediate health score:", h)
    elif m > 30:
        if f > 0:
            h = g - 5
            print("new intermediate health score:", h)
        elif h < -1:
            h = g + 5
            print("new intermediate health score:", h)
        else:
            h = g
            print("new intermediate health score:", h)
        
i=h+e

if i>=5:
    print("great condition")
elif 5>i>=3:
    print("need a little work")
elif 3>i>=1:
    print("need a little work")
else:
    print("at risk!")
print("melanie diet clinic") 
print("*--------------------------*")
print("receipt for patient name:",x)
print("patient weight:",b)
if e==1/1/2000 or f==-1:
    print("days since last visit:",c)
print("--------------------------------")
print("BMI:",m)
print("health:",e)
print("----------------------------------")

print("overall:",i)       

        
        
