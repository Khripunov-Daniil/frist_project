
num = [1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]



def number(num):
    sum1 = sum2 = 0
    num3= []
    for i in range(num):
        if i > 0:
            sum1 += i
            num3.append(sum1) 
        elif i < 0:
            sum2 += i
            num3.append(sum2)
        return num3
        
        
 
print(number(num))

