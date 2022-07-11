result = 0
first = 0
second = 1
while second <= 4000000:
    first, second = second, first+second
    if second%2==0:
        result+=second
print(result)