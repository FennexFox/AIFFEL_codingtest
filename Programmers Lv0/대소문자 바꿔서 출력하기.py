str = input()
return_str = ""

for i in str:
    if i == i.lower():
        return_str += i.upper()
    else:
        return_str += i.lower()

print(return_str)