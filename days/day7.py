from days.day import Day


class Day7(Day):

    def result_puzzle1(self):
        if self.input1 is None:
            return 0
        return self.get_num_bags_contain_color(self.input1, 'shiny gold')

    def result_puzzle2(self):
        if self.input2 is None:
            return 0
        return self.get_individual_bags(self.input2, 'shiny gold')

    def get_num_bags_contain_color(self, rulesFile, color_bag):
        last_count = 0
        contains = self.get_contains(rulesFile)
        bags = [color_bag]
        while len(bags) != last_count:
            last_count = len(bags)
            bags = self.add_bags(contains, bags)
        return len(bags) - 1

    def add_bags(self, contains, bags_colors):
        """
        Añade a la lista de bolsas las bolsas que han de contener alguna bolsa
        de la lista
        """
        for bag in contains:
            # Si no ha de contener ninguna bolsa se ignora
            if contains[bag] is None:
                continue
            for bag_color in contains[bag]:
                if bag_color in bags_colors and bag not in bags_colors:
                    bags_colors.append(bag)
        return bags_colors


    def get_contains(self, rulesFile):
        """
        Genera un diccionario que almacena que bolsas que de contener cada bolsa
        clave:bolsa
        valor: diccionario{
            clave:bolsa
            valor:numero que ha de contener
        }
        """
        contains = {}
        with open(rulesFile) as rules:
            # Lee linea linea y comprueba si la regla dice que puede contener el color buscado
            for rule in rules:
                # Split linea a partir de la palabra "contain"
                rule = rule.split('contain')
                holds = rule[1]
                bag = rule[0].split(' bags')[0]  # obtiene la bola
                # Se busca si la regla permite contetender de manera indirecta la bolsa de color buscada
                if 'no other bags' in holds:
                    contains[bag] = None
                    continue
                contains[bag] = {}
                holds = holds.split(',')
                for hold in holds:
                    # Obtienen toda la informacion de cada bolsa a contener
                    hold = hold.strip(' ')
                    number = hold.split(' ')[0]
                    hold = hold.split(number)[1]
                    hold_bag = hold.split('bag')[0]
                    hold_bag = hold_bag.strip(' ').strip('\n')
                    contains[bag][hold_bag] = int(number)
        return contains

    def get_individual_bags(self, rules_file, bag):
        total_bags = 0
        stack = []
        # Obtiene dicionario que almacena que bolas tiene que contener cada bolsa
        contains = self.get_contains(rules_file)
        # Elemento pila (bolsa, multiplicador)
        stack = [(bag, 1)]
        while len(stack) != 0:
            bag, multiplicator = stack.pop()
            init_bag = contains[bag]
            if init_bag is None:
                continue
            for bag in init_bag:
                total_bags += init_bag[bag] * multiplicator
                stack.append((bag, multiplicator * init_bag[bag]))
        return total_bags









