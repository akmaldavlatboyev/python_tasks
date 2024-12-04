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






