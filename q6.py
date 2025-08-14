# ----1
# ---123
# --12345
# -12345667
# 123456789

def pattern(n):
    for i in range(1,n+1):
        print("-"*(n-i),end="")
        for j in range(1,int((2*i)/2)+1):
            print(j,end='')
        for k in range(int((2*i)/2)-1,0,-1):
            print(k,end="")
        print()

pattern(5)