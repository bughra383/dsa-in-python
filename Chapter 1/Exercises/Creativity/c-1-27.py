
def factors(n):
    k = 1
    large_factors = []  

    while k * k < n:  
        if n % k == 0:  
            yield k                    
            large_factors.append(n // k)  
        k += 1
    
    if k * k == n:  
        yield k
    
    for factor in reversed(large_factors):
        yield factor


test_numbers = [10, 15, 16, 20, 100]
for number in test_numbers:
    print(f"{number}: {list(factors(number))}")