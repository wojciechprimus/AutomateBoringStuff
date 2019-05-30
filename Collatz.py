def collatz():
    c0=int(input("What is the value?"))
    while True:
        if c0==1:
            break
        elif c0%2==0:
            c1=c0/2
            print(c1)
            c0=c1
        else:
            c1=3*c0+1
            print(c1)
            c0=c1

collatz()
