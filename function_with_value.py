def factorial(num):
    """
    Compute num!
    :param num:
    :return: int, the value of num!
    """
    p = 1
    for i in range(1, num+1):
        p *= i
    return p


print(factorial(4))


result = factorial(10)
print(f"10! = {result}")