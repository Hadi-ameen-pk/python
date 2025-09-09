class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def even_check(n):
        return n % 2 == 0


# You can call without creating an object
print(MathOperations.add(4, 6))        # 10
print(MathOperations.even_check(8))   # True
