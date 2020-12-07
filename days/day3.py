"""
DIA 3
"""
from days.day import Day


class Day3(Day):
    def result_puzzle1(self):
        return self.count_trees(self.input1, (3, 1))

    def result_puzzle2(self):
        slopes = [(1, 1), (3, 1), (5, 1), [7, 1], [1, 2]]
        multiplication = 1
        for slope in slopes:
            multiplication *= self.count_trees(self.input2, slope)
        return multiplication

    def count_trees(self, input, slopes=(1, 1)):
        trees = 0
        # Abre fichero que contiene el mapa
        with open(input) as zone_map:
            x = slopes[0]
            next_y = slopes[1]
            # Por cada linea buscamos si en las posicion 3 derecha hay un arbol
            for y, line in enumerate(zone_map):
                # Si esta en la posicion correcta comprueba si hay un arbol
                if y == next_y:
                    # Elimina '\n' de cada linea
                    line = line.rstrip('\n')
                    # Mira si en la pos x hay un arbol teniendo en cuenta que se repite el patron
                    if line[x % len(line)] == '#':
                        trees += 1
                    x += slopes[0]
                    next_y += slopes[1]
            return trees
