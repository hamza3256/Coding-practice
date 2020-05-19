class ProductOfNumbers:

    def __init__(self, lst=[]):
        self.lst = lst

    def add(self, num: int) -> None:
        self.lst += [num]
        return

    def getProduct(self, k: int) -> int:
        return math.prod(self.lst[-k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)