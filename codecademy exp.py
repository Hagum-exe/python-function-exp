#parts of variables: 1.variable name(exp: num1) 2. variable value(exp: 5)
#exp of using def as function
#the def RETURNS the sum of 2 PARAMETERS(variables passed into the function)

def ratiocalculator (num1, num2):
    global sum
    sum = num1/num2
    
def sumsqr():
    return sum**2   # equals to 2/(Sum*Sum)
    
Num1 = int(input('Enter first numer:'))
Num2 = int(input('Enter second numer:'))

#call def sumcalculator
ratiocalculator(Num1, Num2) #specified argument
print(sum)
#
#call def sumsqr
squared_sum = sumsqr()  #none specified argument
print(squared_sum)
#




