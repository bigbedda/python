def print_num(x):
    for i in range(x):
        print(i)
        return
print_num(10)

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(func(4))
