"""
DIA 9
"""
from days.day import Day


class Day9(Day):

    def result_puzzle1(self):
        if self.input1 is None:
            return -1
        return self.get_first_no_valid(self.input1, 25)

    def result_puzzle2(self):
        if self.input2 is None:
            return -1
        number_no_valid = self.get_first_no_valid(self.input2, 25)
        return self.break_XMAS(self.input2, number_no_valid)

    def get_first_no_valid(self, encryptedFile, preamble):
        # Abre fichero
        with open(encryptedFile) as encryptedFile:
            numbers = []
            # Por cada linea comprueba si el valor es valido
            for index, line in enumerate(encryptedFile):
                number = int(line)
                if index < preamble:
                    numbers.append(number)
                else:
                    if not self.is_valid(number, numbers[index-preamble:]):
                        return number
                    numbers.append(number)
        return 0

    def is_valid(self, number, numbers_list):
        # Busca si la suma de dos numeros de la lista es igual al numero
        for i in range(len(numbers_list)):
            for j in range(i+1, len(numbers_list)):
                if numbers_list[i] + numbers_list[j] == number:
                    return True
        return False

    def break_XMAS(self, encryptedFile, number_no_valid):
        # Abre fichero
        with open(encryptedFile) as encryptedFile:
            numbers = []
            # Por cada linea comprueba hasta llegar si el valor es valido
            for index, line in enumerate(encryptedFile):
                number = int(line)
                if number != number_no_valid:
                    numbers.append(number)
                else:
                    break
            for i in range(len(numbers)):
                adition = numbers[i]
                summands = [numbers[i]]
                for j in range(i + 1, len(numbers)):
                    adition += numbers[j]
                    summands.append(numbers[j])
                    if adition == number_no_valid:
                        return min(summands) + max(summands)
        return 0



