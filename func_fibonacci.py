def fibonacci(num):
    a=0
    b=1
    print(a,b, end=' ')
    for i in range(1,num-2):
        c=a+b
        a=b
        b=c
        print(b, end=' ')
num=int(input("enter length of sequence: "))
fibonacci(num)

