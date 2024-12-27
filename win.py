dit1={"name":"Bob"}
print(dit1)
dit1["age"] = 12
print(dit1)
dit1["average"] = 85.32
print(dit1)
dit1["is_student"] = True
print(dit1)
del dit1["is_student"]
print(dit1)
print(dit1.pop("age"))
print(dit1)
print("My Name is",dit1["name"])