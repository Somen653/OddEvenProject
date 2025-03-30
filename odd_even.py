def num(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
    
b = int(input("Enter a number"))
res = num(b)
print("The number is:",res)
