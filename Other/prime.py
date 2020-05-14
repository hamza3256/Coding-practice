import sys

def countPrimes(n):
    if n==29362:
        return 0
    for i in range(2,n):
        if n % i == 0 and n != i:
            return countPrimes(n-1)
    print(n)
    return 1 + countPrimes(n-1)

if __name__ == "__main__":
    s = int(sys.argv[1])
    print(countPrimes(s))
