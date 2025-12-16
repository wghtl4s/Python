def find_primes(n, output_format):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    if output_format == 'list':
        return primes
    elif output_format == 'column':
        for p in primes:
            print(p)
        return None
    elif output_format == 'count':
        return len(primes)

n = int(input("n: "))
fmt = input("format (list/column/count): ")
res = find_primes(n, fmt)
if res is not None:
    print(res)