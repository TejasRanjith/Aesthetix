# ----A
# ---BBB
# --CCCCC
# -DDDDDDD
# EEEEEEEEE

def pattern(n):
    alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1,n+1):
        print("-"*(n-i),end="")
        for j in range(0,2*i-1):
            print(alphas[i%26-1],end='')
        print()

pattern(5)