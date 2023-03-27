def prime(*numbers):
    max_value=max(numbers)
    for n in numbers:
        flag = True
        if n < 2:
            print(n, ' is not prime')
        else:
            for i in range(2, n):
                if(n%i == 0):
                    flag=False
                    break
            if flag:
                print(n, ' is prime')
            else:
                print(n, ' is not prime')

prime(0, 1, 2, 3, 4, 5)