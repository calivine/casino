from math import sqrt

class IntegerStatistics(list):
    pass

    def mean(self):
        return sum(self) / len(self)


    def stdDeviation(self):
        return sqrt(sum((x-self.mean())**2 for x in self) / (len(self) - 1))
