def reverse(num):
    digits,result,sign=[],0,1
    if num < 0:
        num = abs(num)
        sign = -1
    while int(num) != 0:
        digits.append(int(num%10))
        num = num/10
    print(digits)
    digits.reverse()
    for i in range(len(digits)):
        result += digits[i]*(10**i)
    if result < 2147483648:
        return result*sign
    else:
        return 0

print(reverse(int(input("Enter number: "))))
