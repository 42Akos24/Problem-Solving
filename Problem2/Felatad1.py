class GradeCalculator:
    def __init__(self, dev_score, test_score):
        self.dev_score = dev_score
        self.test_score = test_score

    def get_avg(self):
        return (self.dev_score + self.test_score) / 2

    def get_score(self):
        avg = self.get_avg()

        if avg >= 90:
            return '5'
        elif avg >= 80:
            return '4'
        elif avg >= 70:
            return '3'
        elif avg >= 60:
            return '2'
        else:
            return '1'


Calculator = GradeCalculator(80, 70)
print(Calculator.get_score())
