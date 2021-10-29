def rightshift(list1, num):
    temp = [] 
    for i in range(len(list1) - num, len(list1)):
        temp.append(list[i])     
    for i in range(0, len(list1) - num):
        temp.append(list1[i])
          
    return temp


shift = 2
a = [1, 2, 3, 4, 5] 
  
print(rightshift(a, shift))
