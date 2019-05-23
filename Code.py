#Exercise1 Half Square:

for i in range (1, 6):
    for j in range(1, 7 - i):
        print('#',  end = '')
    print('\n')

#Exercise2 triangle

for i in range (1, 9):
    for j in range(1, (4 - abs(4-i))+1):
            print('#',  end = '')
    print('\n')
    
    
 #Exercise 3 Luhn Formula
 
num = input('enter ID number ')
listO = [int(i) for i in str(num)]
listOp = listO[::-1] #inverting the list as it's supposed to be everyother character from the right

#Doubling the value of everyother digits
for i in range(1, len(listOp), 2):
    listOp[i] = 2*listOp[i]
    
#Creating a new int with the modified list and making a new list
newnum = ''.join((str(i) for i in listOp))
list1 = [int(j) for j in str(newnum)]


#adding the list elements together
tot = 0
for k in range(0, len(list1)):
    tot = tot + int(list1[k])
    
if tot%10 == 0:
    print(num + ' is valid under Luhn formula')
elif tot%10 != 0:
    print(num + ' is not valid under Luhn formula')