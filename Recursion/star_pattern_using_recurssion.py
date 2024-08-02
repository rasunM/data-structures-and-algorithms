def starPattern(n):
    if n==0:
        return None
    print(n*"*")
    starPattern(n-1)
    print(n*"*")
    
starPattern(5)
