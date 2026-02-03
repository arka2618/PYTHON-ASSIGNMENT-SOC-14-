my_set = {10, 20, 15, 35, 30, 25}
print(f"My Set: {my_set}")

#ADDING ELEMENT
my_set.add(40)
print(f"Set after adding element using add(): {my_set}")

#UNION and INTERSECTION OF SET
set1 = {46, 48, 50, 52}
set2 = {46, 54, 56, 52}
print(f"Set 1: {set1}\nSet 2: {set2}")
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")

#DIFFERENCE IN SET
difference_set = set1 - set2
print(f"Difference of set1 and set2: {difference_set}")
