import json
f = open("JS.json", "w")
def record(name, roll_no, marks):
    data = [{"Subject": name, "Roll No": roll_no, "Marks": marks}]
    json.dump(data, f)
record("Mathematical Foundation of Computing", 49, 20)
record("Materials of Computing Devices", 49, 25)
record("Digital Electronics and  Logic Design", 49, 24)
f.close()