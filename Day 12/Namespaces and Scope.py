num = int(input("Enter a number to check if it is prime: "))
def is_prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num == 1:
        return False
    else:
        return True

print(is_prime(num))

def prime_2(num):
    if num == 2:
        return True
    elif num == 1:
        return False
    for a in range(2, num):
        if num % a == 0:
            return False
    return True

print(prime_2(num))