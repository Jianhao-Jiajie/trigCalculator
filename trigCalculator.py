#input: number or number in string\
pi = 3.141592653589793238462643383279502
def round(num):
    try:
        extra = float(num) - int(num)
        if (extra < 0.5 and extra > 0) or (extra > -0.5 and extra < 0):
            return int(num)
        elif int(num) < 0:
            return int(num) - 1
        else:
            return int(num) + 1
    except:
        print('enter a valid number for round')

#print(round(float(input('type a number: '))))

#rounds down float parameters
#input: int or int in string
def factorial(num):
    try:
        num = int(float(num))
        if num < 0:
            print('enter a positive number to factorial')
            return
        n = 0
        final = 1
        while n < num:
            final *= num - n
            n += 1
        return final
    except:
        print('enter a valid number for factorial')

#print(factorial(input('type a number: ')))

def sine(num):
    try:
        num %= (2*pi)
 #    degree parameter (work on this later)
 #       if degree == True:
 #           num = num/180*pi
        temp = 0
        for x in range(20):
            temp += (-1)**x /factorial(2*x+1) * num**(2*x+1)
        return(temp)
    except:
        print("error with sine")

#ifDegree = input('calculate in degree?(True/False): ')
radian = float(input('enter the angle: '))
print(f"sine of {radian} = {sine(radian):.10f}")


def cosine(num):
    try:
        num %= (2*pi)
#杰哥做事！！
        temp = 0
        for x in range(20):
            temp += (-1)**x /factorial(2*x) * num**(2*x)
        return(temp)
    except:
        print("error with cosine")
  
print(f"cosine of {radian} = {cosine(radian):.10f}")

def tangent(num):
    try:
        if cosine(num) < 0.0000001 and cosine(num)> -0.0000001:
            return("has asymptote")
        else:    
            return(round((sine(num)/cosine(num))*(10**10))/(10**10))
    except:
        print("error with tangent")

print(f"tangent of {radian} = {tangent(radian)}")
