#2.4

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 10
count = 0
fac = factorial(num)
list_text = list(str(fac))
list_text.reverse() # reverse list

for i in list_text:
    
    if i == "0":
        count = count + 1
    else:
        break

print("The factorial of", num, "is", factorial(num) , "and the last digit is", list_text[0] , "and the number of zero is", count)