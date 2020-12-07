"""
DIA 2
"""
from days.day import Day


class Day2(Day):
    def result_puzzle1(self):
        valids_pass = 0
        if self.input1 is None:
            return 0
        # Abre fichero
        with open(self.input1) as file:
            # Parseamos los tokens de cada linea y validamos si es valida
            for line in file:
                policy, password = line.split(':')
                # obtemos los limites de la politica
                range_policy, letter = policy.split()
                limits = range_policy.split('-')
                # valida contraseña
                counts_letter = password.count(letter)
                if int(limits[0]) <= counts_letter <= int(limits[1]):
                    valids_pass += 1
        return valids_pass

    def result_puzzle2(self):
        valids_pass = 0
        if self.input1 is None:
            return 0
        # Abre fichero
        with open(self.input1) as file:
            # Parseamos los tokens de cada linea y validamos si es valida
            for line in file:
                policy, password = line.split(':')
                # obtemos los limites de la politica
                range_policy, letter = policy.split()
                limits = range_policy.split('-')
                lowest = int(limits[0])
                highest = int(limits[1])
                # valida contraseña
                if password[lowest] != password[highest]:
                    if password[lowest] == letter or password[highest] == letter:
                        valids_pass += 1
        return valids_pass
