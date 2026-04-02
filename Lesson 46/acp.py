def countDigit(n):
    if n == 0 :
        return 1
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count

n = 58964
print(countDigit(n))