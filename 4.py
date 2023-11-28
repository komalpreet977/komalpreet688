def takeinput():
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))
    c = str(input("Enter operator (+, -, *, /): "))

    return x, y, c

def displyresult(x, y, c):
    result = 0
    formula = f"(x)(y)"

    if c == '+':
        result = x + y
    elif c == '-':
        result = x - y
    elif c == '*':
        result = x * y
    elif c == '/':
        result = x / y

    formula = f"(x)(y)"
    print(f"Formula: {formula}")
    print(f"Result: {result}")

if __name__ == "__main__":
    
    x, y, c = takeinput()

    
    displyresult(x, y, c)
