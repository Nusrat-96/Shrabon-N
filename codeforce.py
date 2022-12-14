# input_string = input()
# s_capital =''
# s_lower =''
# s_numeric =''
# s_others =''
# for i in input_string:
#     if 65<=ord(i)<=90:
#         s_capital = s_capital+i
#     elif 97<=ord(i)<=122:
#         s_lower= s_lower+i
#     elif 48<=ord(i)<=57:
#         s_numeric = s_numeric+i
#     else:
#         s_others=s_others+i
# print(s_capital,s_lower,s_numeric,s_others, sep="\n")
# c=0
# while True:
#     try:
#         string2 = input()
#     except EOFError:
#             break
        
#     string1=""
#     for i in string2:
#         if i=="\"" and c==0:
#             new_char = "``"
#             string1 = string1 + new_char
#             c=1
#         elif i=="\"" and c==1:
#             new_char = "''"
#             string1 = string1 + new_char
#             c=0
#         else:
#             string1 = string1 + i
#     print (string1)


        


for i in range(int(input())):
    input_value_ = input()
    input_value = list(input_value_)
    reverse = input_value[::-1]
    count=0
    for i in range (len(reverse)):
        if reverse[i]==input_value[i]:
            count=count+1 
            continue
        else:
            break
    if count==len(reverse):
        print('wins')
    else:
        print('loses')


    

    