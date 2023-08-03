"""4. Write a program that takes a list and splits into smaller lists of given size.
 For example, if lst = [1, 2, 3, 4, 5, 6], size = 2, it should return [[1, 2], [3,4], [5,6]] 
 and if lst = [1,2,3,4,5,6,7,8,9], size = 4 then it should return [[1,2,3,4],[5,6,7,8],[9]]."""

lst = [1,2,3,4,5,6,7,8,9]
size = int(input("enter size:"))
lst_new = []
splits = (len(lst)//size)+1

for i in range(0,len(lst),size):
    sub_list = lst[i:i+size]
    lst_new.append(sub_list)
    
print(lst_new) 