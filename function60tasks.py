import math

# # 1. 
# def func(a, b, c, d, e):
#     return a**3, b**3, c**3, d**3, e**3
a = 72
b = 25
c = 66
d = 6
e = 7
# print(func(a,b,c,d,e))   

# 2.
# def myfunc(a, b, c):
#     return (a**2, a**3, a**4), (b**2, b**3, b**4), (c**2, c**3, c**4)    
# print(myfunc(a,b,c))
# # 3. 
# def mean(a, b, c, d):
#     arithmeticMean = (a + b + c + d) / 4
#     geometricMean = math.sqrt(a * b * c * d)
#     return arithmeticMean, geometricMean
# print(mean(a,b,c,d))    

# # 4.
# def triangle(a, b, c):
#     perimeter = a + b + c
#     s = perimeter / 2
#     area = (s * (s - a) * (s - b) * (s - c))**0.5
#     return area, perimeter

# print(triangle(a,b,c))
# # 5.
# def rectPs(x1, y1, x2, y2):
#     length = abs(x2 - x1)
#     width = abs(y2 - y1)
#     area = length * width
#     perimeter = 2 * (length + width)
#     return area, perimeter
# print(rectPs(x1=12,y1=3,x2=18,y2=8))
# # 6.
# def DigitCountSum(n):
#     digits = [int(d) for d in str(n)]
#     count = len(digits)
#     totalSum = sum(digits)
#     return count, totalSum
# print(DigitCountSum(n=32))    


# 8. 
# def addRightDigit(k, r):
#     return int(str(k) + str(r))
# print(addRightDigit(k=23,r=12))    


# 9. 
# def addLeftDigit(k, r):
#     return int(str(r) + str(k))
# print(addLeftDigit(k=23,r=32))    

# 10. 
# def swap(a, b):
#     return b, a
# print(swap(a,b))    
    

# 12. 
# def sortInc3(a, b, c):
#     return sorted([a, b, c])
# print(sortInc3(a,b,c))    

# 13. 
# def sortDec3(a, b, c):
#     return sorted([a, b, c], reverse=True)
# print(sortDec3(a,b,c))    

# 14. 
# def shiftRight3(a, b, c):
#     return c, a, b
# print(shiftRight3(a,b,c))    

# 15.
# def shiftLeft3(a, b, c):
#     return b, c, a
# print(shiftLeft3(a,b,c))    

# 16. 
# def sign(a):
#     return -1 if a < 0 else (1 if a > 0 else 0)
# print(sign(a))    

# 17. 
# def quadraticRoots(a, b, c):
#     discriminant = b**2 - 4*a*c
#     if discriminant < 0:
#         return None
#     x1 = (-b + math.sqrt(discriminant)) / (2*a)
#     x2 = (-b - math.sqrt(discriminant)) / (2*a)
#     return x1, x2
# print(quadraticRoots(a,b,c))    

# 18. 
# def circle(radius):
#     pi = 3.1415
#     return pi * radius**2
# print(circle(radius=40))    

# 19.
# def rings(r1, r2):
#     pi = 3.1415
#     return pi * (r1**2 - r2**2)
# print(rings(r1=302,r2=50))    

# 20. 
def triangleP(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    perimeter = a + b + hypotenuse
    return perimeter
print("TriangleP:", triangleP(a,b))
# a = 3
# b = 12
# c = 18
# def sumRange(a, b):
#     if a > b:
#         return 0
#     sum = 0 
#     for i in range(a + 1, b + 1): 
#         sum += i
#     return sum

# # print(sumRange(a, b))

# def sumrange(b,c):
#     if b > c:
#         return 1
#     total = 0
#     for i in range(b,c+1):
#         total += i
#     return total
# res = sumRange(a,b)
# print(sumrange(b,c)+res)         

#22
# a = 30
# b = 6
# op = input("arifmetik amal kirit: ['+','-','*','/']")
# def calc(a,b,op):
#     if op == '+':
#         n1 = a + b
#         return n1
#     elif op == '-':
#         n2 = a - b
#         return n2
#     elif op == '*':
#         n3 = a * b
#         return n3
#     elif op == '/':
#         n4 = a / b
#         return n4
#     else:
#         print("Bunday amalni funksiya qollamaydi")                

# print(calc(a,b,op))        

#23

# x = 3
# y = 4
# def quarter(x,y):
#     if x > 0 and y > 0:
#         chorak1 ="1-chorakda yotibdi"
#         return chorak1
#     elif x < 0 and y > 0:
#         chorak2 ="2-chorakda yotibdi"
#         return chorak2    
#     elif x < 0 and y < 0:
#         chorak3 ="3-chorakda yotibdi"
#         return chorak3
#     elif x > 0 and y < 0:
#         chorak4 ="4-chorakda yotibdi"
#         return chorak4        
# print(quarter(x,y))        

#24

num1 = 43
num2 = 12
num3 = 128
num4 = 32
num5 = 11
k = 5
n = 20

# def even(k):
#     if k % 2 == 0:
#         return True
#     else:
#         return False

# print(even(k))
# print()

# print(even(num1))
# print(even(num2))
# print(even(num3))

#25
# def isSquare(k):
#     if k > 0:
#         root = k ** 0.5
#         return root.is_integer()
#     return False
# print(isSquare(k)) 
# print()
# print(isSquare(num1)) 
# print(isSquare(num2)) 
# print(isSquare(num3)) 


#26

# def isPower5(k):
#     if k > 0:
#         while k % 5 == 0:  
#             k //= 5
#         return k == 1  
#     return False

# print(isPower5(k))  
# print()
# print(isPower5(num1))  
# print(isPower5(num2))  
# print(isPower5(num3))
# print(isPower5(num4))  
# print(isPower5(num5))  


#27

# n = 8
# def isPowerN(k):
#     if k > 0:
#         while k % n == 0:  
#             k //= n
#         return k == 1  
#     return False

# print(isPowerN(k))  
# print()
# print(isPowerN(num1))  
# print(isPowerN(num2))  
# print(isPowerN(num3))
# print(isPowerN(num4))  
# print(isPowerN(num5))  


#28
def isPrime(n):
    if n < 2:
        return False 
    counter = 0
    i = 1
    while i <= n:
        if n % i == 0:
            counter += 1
        i += 1
    if counter == 2:
        return True
    else:
        return False    










