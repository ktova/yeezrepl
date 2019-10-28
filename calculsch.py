from datastock import Datas

class Calculator:

    def __init__(self, number):
        self.number = number

    def color(self):
        if self.number == 0:
            return 0
        elif (self.number >= 1 and self.number <= 10) or (
            self.number >= 19 and self.number <= 28
        ):
            if self.number % 2 == 0:
                return "black"
            else:
                return "red"
        elif (
            self.number >= 11
            and self.number <= 18
            or (self.number >= 29 and self.number <= 36)
        ):
            if self.number % 2 == 0:
                return "red"
            else:
                return "black"

    def column(self):
        if self.number == 0:
            return 0
        else:
            result_of_division = self.number % 3
            if result_of_division == 0:
                return 3
            else:
                return result_of_division

    def is_even(self):
        if self.number == 0:
            return 0
        else:
            return self.number % 2 == 0

    def dozens(self):
        if self.number == 0:
            return 0
        elif self.number >= 1 and self.number <= 12:
            return 1
        elif self.number >= 13 and self.number <= 24:
            return 2
        elif self.number >= 25 and self.number <= 36:
            return 3

    def square(self):
        if self.number == 0:
            return 0
        else:
            if self.number == 1:
                self.sqr1 = Datas.spr1
                return self.sqr1
            elif self.number == 3:
                self.sqr1 = Datas.spr3
                return self.sqr1
            elif self.number == 34:
                self.sqr1 = Datas.spr34
                return self.sqr1
            elif self.number == 36:
                self.sqr1 = Datas.spr36
                return self.sqr1
            else:
                if self.number in Datas.f1:
                    self.sqr1 = [self.number]
                    self.sqr1.append(self.number - 2)
                    self.sqr1.append(self.number - 3)
                    self.sqr1.append(self.number + 1)
                    self.sqr2 = [self.number]
                    self.sqr2.append(self.number + 1)
                    self.sqr2.append(self.number + 3)
                    self.sqr2.append(self.number + 4)
                    return self.sqr1, self.sqr2
                elif self.number in Datas.f2:
                    self.sqr1 = [self.number]
                    self.sqr1.append(self.number - 1)
                    self.sqr1.append(self.number + 2)
                    self.sqr1.append(self.number + 3)
                    self.sqr2 = [self.number]
                    self.sqr2.append(self.number + 1)
                    self.sqr2.append(self.number + 3)
                    self.sqr2.append(self.number + 4)
                    return self.sqr1, self.sqr2
                elif self in Datas.f3:
                    self.sqr1 = [self.number]
                    self.sqr1.append(self.number - 1)
                    self.sqr1.append(self.number - 3)
                    self.sqr1.append(self.number + 4)
                    self.sqr2 = [self.number]
                    self.sqr2.append(self.number - 1)
                    self.sqr2.append(self.number + 2)
                    self.sqr2.append(self.number + 3)
                    return self.sqr1, self.sqr2