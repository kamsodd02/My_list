#Create an empty list called My_list
My_list = []
print("My_list has been created as an empty list.")

#Append some items to My_list
My_list.append("10")
My_list.append("20")
My_list.append("30")
My_list.append("40")
print("After Append:",My_list)

#Insert an item at the at the second position of My_list.
My_list.insert(1, '15')
print("After Insert:", My_list)
print("The second item in My_list is:", My_list[1])

#create a new list called My_list2
My_list2 = ['50', '60', '70']

#Extend My_list with My_list2
My_list.extend(My_list2)
print("After Extend:", My_list)

#Remove the last item from My_list.
My_list.pop()
print("After Pop:", My_list)

#Sort My_list in ascending order.
My_list.sort()
print("After Sort:", My_list)

#Find and print the index of the value '30' in My_list.
index_of_30 = My_list.index('30')
print("The index of '30' in My_list is:", index_of_30)




