sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(sqs[4:7])

# print alternate with below

print(sqs[::2])

print(sqs[2:8:3])       # elements starting 2nd, up to 8th with a jump of 3 steps

print(sqs[1::4])

print(sqs[1:-1])    # 0 starts at other end for - numbers

print(sqs[::-1])        # prints the numbers starting at 81 to 0 this way

print(sqs[7:5:-1])
