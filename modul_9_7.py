def is_prime(func):
    def wrapper(a, b, c):
        result2 = func(a, b, c)
        count = 0
        for i in range(2,result2//2):
            if result2 % i == 0:
                count +=1
                break
        if count == 0:
            print ('Простое')
        else:
            print ('Составное')
        return result2
    return wrapper

@is_prime
def sum_three(a, b, c):
    result1 = a + b + c
    return result1


result = sum_three(1, 4, 3)
print(result)