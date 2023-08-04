import math
num = int(input("Enter the range: "))
primeNos = [] 
for i in range(2, num):
    flag = 0
    for j in range(2, i):
        if(i != j and i % j == 0):
            flag = 1
    if(flag == 0):
        primeNos.append(i)    
print(primeNos)