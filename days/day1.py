"""
DIA 1
"""
from days.day import Day


class Day1(Day):
    def result_puzzle1(self, excepted=2020):
        if self.input1 is None:
            return "No se ha introducido input1"
        return self.find_result(excepted, n_adding=2)

    def result_puzzle2(self, excepted=2020):
        if self.input1 is None:
            return "No se ha introducido input2"
        return self.find_result(excepted, n_adding=3)

    def find_result(self, excepted=2020, n_adding=2):
        numbers = [number for number in open(self.input1)]
        addings = [[index, [int(number)]] for index, number in enumerate(numbers)]
        while len(addings):
            index = addings[0][0]
            current_adding = addings[0][1]
            for j in range(index + 1, len(numbers)):
                n1 = int(numbers[j])
                if len(current_adding) == n_adding - 1 and sum(current_adding) + n1 == excepted:
                    # Encontro solucion
                    product = 1
                    for x in current_adding + [n1]:
                        product *= x
                    return product
                elif current_adding != n_adding - 1 and sum(current_adding) + n1 < excepted:
                    new_possible_adding = [j, current_adding + [n1]]
                    addings.append(new_possible_adding)
            del addings[0]
        return 0
