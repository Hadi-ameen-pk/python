class MathOperations:
    @classmethod
    def check(cls, total):
        if total % 2 == 0:
            print(total, "is Even")
        else:
            print(total, "is Odd")
MathOperations.add_and_check(7)
