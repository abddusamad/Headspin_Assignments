print("enter element,position and array")

element=input()                             #input the element need to insert
position=int(input())-1                     #position no.
array=list(input().split())                 #input the array
arr1=array[:position]                       #seperate the array by position number
arr2=array[position:]
array=arr1+[element]+arr2                   #adding all array using concatenation 
print(array)
