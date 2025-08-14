def addDigits(self, num: int) -> int:
    digits=[]
    while int(num) != 0:
        digits.append(int(num%10))
        num = num/10
    num = sum(digits)
    digits=[]
    if num > 9:
        return addDigits(1,num)
    else:
        return num

print(addDigits(1,48))