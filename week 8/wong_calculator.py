# 
# ============================================
# ; Title:  Exercise 8.3
# ; Author: Devan Wong
# ; Date:   2 December 2020
# ; Description: Python in Action
# ;===========================================
# 

# addition 
def add(a,b):
    return a + b

# subtract
def subtract(a,b):
    return a - b

# divide
def divide(a,b):
    return a / b

print(add(1,2))
print(subtract(4, 1))
print(divide(8, 2))

# if/elses statement
num1 = 0
num2 = 0
if num1 > num2:
    print("num1  greater than num2")
elif num1 == num2:
    print("num1  is equal to num2")
else: 
    print("num1 is not greater than num2")
