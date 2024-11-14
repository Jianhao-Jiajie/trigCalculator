#input: str, float, int
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
        print('Enter a valid number')

#print(round(float(input('type a number: '))))

#rounds down floats
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
        print('enter a number')

print(factorial(input('type a number: ')))
