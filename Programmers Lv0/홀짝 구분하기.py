a = int(input())
return_str = (lambda x: f"{x} is even" if x % 2 == 0 else f"{x} is odd")(a)

print(return_str)