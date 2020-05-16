print("enter element,position and array")
element=input()                             #input the element need to insert
position=int(input())-1                     #position no.
array=list(input().split())                 #input the array
temp_array_first=array[:position]           #seperate the array at position number
temp_array_last=array[position:]
array=temp_array_first+[element]+temp_array_last    #adding all array using  
print(array)
