#Assignment 1 - Nusrat Jahan
def list_solution(list1, list2):
    #1. Take input of two integer lists and Concatenate two lists index-wise
        # code will also execute if we enter two list with different length
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
    print ("Concatenated list is: ", conc_list)

    #2. Reverse a list 
    conc_list = conc_list [::-1]
    print ("Reverse the Concatenated list: ", conc_list)

    #3 insert 20 in index 3 in the list:
    if len(conc_list)>=3:
        conc_list.insert(3,20)
    else:
        conc_list.append(20)
    print("Add item 20 in index 3 or at the end:", conc_list)

    #4 Remove specific item form the list
    remove_list = [i for i in input("Enter list value to remove item: ").split()]
    remove_item= input("Enter element that have to remove from the list: ")
    n=remove_list.count(remove_item)
    for i in range(n):
        remove_list.remove(remove_item)
    print ("Item removed:",remove_list)
    

list1 = list(map(int,input("Enter values for first list: ").split()))
list2 = list(map(int,input("Enter values for second list: ").split()))
list_solution(list1, list2)