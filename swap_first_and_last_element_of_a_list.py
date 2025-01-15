#Approach 1 : using temporary variable

list1 = [10,90,80,70,60,50,40,30,20,100]

size = len(list1)

temp = list1[0]
list1[0] = list1[size-1]
list1[-1] = temp

print(list1)

#Approach 2 :

list2 = [100,20,30,40,50,60,70,80,90,10]

list2[0],list2[-1] = list2[-1],list2[0]

print(list2)

#Approach 3 : using tuple

list3 = [10,2,3,4,5,6,7,8,9,1]

get = (list3[0],list3[-1])
list3[-1],list3[0] = get

print(list3)

#Approach 4 : using * operand

list4 = [1,9,8,7,6,5,4,3,2,10]

start,*middle,end = list4
list4 = end,*middle,start
print(list4)
print(end,*middle,start)

#Approach 5 : Using pop() method

list5 = [99,22,33,44,55,66,77,88,11]

first = list5.pop(0)
last = list5.pop(-1)

list5.insert(0,last)
list5.append(first)

print(list5)
