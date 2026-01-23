new_dictionary = {"Student name" : "Arka Bhattacharya", 
                  "Enrollment No" : "ADT25SOCB0210", 
                  "Division" : "SOC 14", 
                  "Course" : "B.Tech",
                  "Branch" : "Computer Science and Engineering"}
print(f"My Dictionary: {new_dictionary}")

#ACCESSING DICTIONARY
student_name = new_dictionary["Student name"]
enrollment_no = new_dictionary["Enrollment No"]
print(f"1. Student Name: {student_name}\n2. Enrollment No: {enrollment_no}")

#UPDATING DICTIONARY
new_dictionary["Division"] = "SOC 15"
print(f"Updated dictionary : {new_dictionary}")

#ADDTION OF NEW KEY-VALUE PAIR
new_dictionary["Year"] = "1st Year"
print(f"Dictionary after adding new key-value pair: {new_dictionary}")

#REMOVE
new_dictionary.pop("Division")
print(f"Dictionary after removing Division: {new_dictionary}")

#Merging DICTIONARY
dictionary1 = {"A": 10, "B": 89, "C": 45}
dictionary2 = {"D": "Mango", "E": "Apple", "F": "Orange"}
print(f"Dictionary 1: {dictionary1}\nDictionary 2: {dictionary2}")
merged_dictionary = {**dictionary1, **dictionary2}
print(f"Merged Dictionary: {merged_dictionary}")
