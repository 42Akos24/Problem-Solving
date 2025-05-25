class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"A szám értéke: {self.value}"

    def __add__(self, other):
        return Number(self.value + other.value)


number1 = Number(5)
number2 = Number(1)

print(number1)

number3 = number1 + number2
print(number3)
