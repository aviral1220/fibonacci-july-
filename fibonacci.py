def fib (n):
    f = []
    f[0], f[1] = 0, 1
    if n==1:
        return 1
    if n==0:
        return 0
    for i in range (2,n):
        f.append(f[i-1]+f[i-2])
        return f




        '''
            0(2^n) => :c
            0(N) n> :D
            N = 1000
            1000ms = 1s
            2^1000
        '''      