#1. Take input of two integer lists and Concatenate two lists index-wise
list1= list(map(int,input("Enter values for first list: ").split()))
list2 = list(map(int,input("Enter values for first list: ").split()))

conc_list=[]
max_len = max (len(list1),len(list2))
min_len = min (len(list1),len(list2))
max_list = []
min_list = []
if len(list1)> len(list2):          #find the large list 
    max_list = list1
    min_list = list2
else:
    max_list = list2
    min_list = list1

for i in range (0,max_len):
    if i<min_len:
        conc_list.append(max_list[i]+min_list[i])
    elif i>= min_len:
        conc_list.append(max_list[i])

print(conc_list)

#2. Reverse a list 
reverse_list = [i for i in input("Enter list value for reverse list: ").split()]
reverse_list = reverse_list[::-1]
print ("Reverse list:", reverse_list)


#3. add item at the list
reverse_list.insert(3, "25")

#4 remove 20 from the list:
for i in reverse_list:
    if i=="20":
        reverse_list.remove(i)
print (reverse_list)

