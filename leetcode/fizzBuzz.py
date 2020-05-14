class Solution(object):
    def fizzBuzz(self, n):
        arr=[-1]*(n+1)
        for c in range(n+1):
            if c==0: continue
            elif c % 3 == 0 and c % 5 == 0:
                arr[c]="FizzBuzz"
            elif c % 3 == 0:
                arr[c]="Fizz"
            elif c % 5 == 0:
                arr[c]="Buzz"
            else:
                arr[c] = str(c)
        return arr[1:]

        