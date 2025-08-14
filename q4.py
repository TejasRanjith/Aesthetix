# ----1
# ---222
# --33333
# -4444444
# 555555555

def pattern(n):
    for i in range(1,n+1):
        print("-"*(n-i),end="")
        for j in range(1,2*i):
            print(i,end='')
        print()

pattern(5)