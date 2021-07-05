#%%
Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#%%
# This Function Will Print Out The Element In List 
# Function To Acsess
# print(list_name[element])
print(Digits[0])
#%%
# The Negative Number Does The Reverse Of Postive Elements It Prints Out The From The Desending Order
print(Digits[-1])
#%%
# The Colon Will Be The Range in The List
print(Digits[2:5])
#%%
# The 2 Colons Is Striding (First_Element:Second Element:By Skiping On Every Given Number)
print(Digits[0:10:2])
#%%
# Another Way To Reverse A List
print(Digits[::-1])
#%%
# This Function Will Print Out The Number Of Elements In The List
print(len(Digits))
#%%
# This For Loop Will Print Out The Cascading Figure Of Digits Variable
for i in range(len(Digits)):
    print(Digits[0:i])
#%%
# This Prints Out The 12,123,234,345.etc
for i in range(len(Digits)):
    print(Digits[i:i+3])






