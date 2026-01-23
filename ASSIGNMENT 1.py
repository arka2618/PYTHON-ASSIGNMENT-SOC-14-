my_list = [23, 45, 12, 67, 34, 89, 10]
print("My list:", my_list)

#ACCESSING
first_element = my_list[0]
second_element = my_list[1]
last_element = my_list[-1]
print(f"1. First element: {first_element}\n2. Second element: {second_element}\n3. Last element: {last_element}")

#INDEXING
Index1 = my_list.index(67)
Index2 = my_list.index(10)
print(f"1. Index value of 67: {Index1}\n2. Index value of 10: {Index2}")

#SLICING
slice = my_list[::-1]
print(f"Sliced OF list: {slice}")

#ADDING ELEMENT IN LIST
my_list.append(50)
print(f"List after adding value ussing append(): {my_list}")

my_list.insert(3, 99)
print(f"List after adding value ussing insert(): {my_list}")

#REMOVE ELEMENT
my_list.remove(89)
print(f"List after removing value using remove(): {my_list}")

my_list.pop()
print(f"List after removing last element using pop(): {my_list}")

#SORTING
my_list.sort()
print(f"List after sorting : {my_list}")

#REVERSE
my_list.reverse()
print(f"List after reversing : {my_list}")
