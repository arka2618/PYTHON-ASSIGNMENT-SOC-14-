my_tuple = (20, 40, 60, 80, 100, 65)
print("My tuple:", my_tuple)
#ACCESSING
print(f"1. First element: {my_tuple[0]}\n2. Third element: {my_tuple[2]}\n3. Last element: {my_tuple[-1]}")

#SLICING
sliced_tuple = my_tuple[1:4]
print(f"Sliced tuple from Index 1 to 4: {sliced_tuple}")

#NESTED TUPLE
new_tuple = (10, 20, "Arka Bhattacharya", (15, 78, 67), "Python Programming")
print(f"Nested Tuple: {new_tuple}")

#ACCESSING NESTED TUPLE
access_tuple = new_tuple[2][0]
print(f"Accessed element from nested tuple: {access_tuple}")

#REPETITION
repeated_tuple = my_tuple * 5
print(f"Tuple after repetition: {repeated_tuple}")

#ADDITION OF TUPLE
tuple1 = ("Arka", "Lakshya", "Satish", "Swaroop")
tuple2 = (145, 56, 890, 60)
Tuple = tuple1 + tuple2
print(f"Tuple after addition: {Tuple}")