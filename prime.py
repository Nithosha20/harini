def prime(num):
    if num<=1:
        print("No Prime Number")
    for i in range(2,num):
        if num%i==0:
            print("Not Prime Number")
    print("prime number")
prime(3)
