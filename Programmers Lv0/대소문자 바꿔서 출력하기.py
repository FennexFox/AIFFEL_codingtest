str = input()
return_str = ""

for letter in str:
    str_append = (lambda x: x.lower() if x == x.upper() else x.upper())(letter)
    return_str += str_append

print(return_str)