# ----1
# ---123
# --12345
# -12345667
# 123456789

def pattern(n):
    for i in range(1,n+1):
        print("-"*(n-i),end="")
        for j in range(1,2*i):
            print(j,end='')
        print()

pattern(5)